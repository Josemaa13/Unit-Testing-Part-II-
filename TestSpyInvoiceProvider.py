import unittest
from unittest.mock import MagicMock
from decimal import Decimal
from UnitTesting2 import Provider, Invoice

class TestSpyInvoiceInProvider(unittest.TestCase):
    def test_spy_avg_unit_price_interactions(self):
        # 1. Setup: Creamos el proveedor
        provider = Provider(name="Spy Provider")
        
        # 2. Setup: Creamos nuestro Spy (usando MagicMock)
        # Actuará como un Stub devolviendo valores, pero lo usaremos como Spy
        # para registrar las interacciones.
        spy_invoice_1 = MagicMock(spec=Invoice)
        spy_invoice_1.kilos_to_bill.return_value = Decimal("10.0")
        spy_invoice_1.unit_price.return_value = Decimal("5.0")
        
        spy_invoice_2 = MagicMock(spec=Invoice)
        spy_invoice_2.kilos_to_bill.return_value = Decimal("20.0")
        spy_invoice_2.unit_price.return_value = Decimal("2.0")
        
        # Añadimos las facturas (spies) al proveedor
        provider.add_bill(spy_invoice_1)
        provider.add_bill(spy_invoice_2)
        
        # 3. Acción: Llamamos al método que queremos probar
        provider.avg_unit_price()
        
        # 4. Verificación (Spying):
        # A) Verificar que avg_unit_price() invoca kilos_to_bill() en CADA factura
        spy_invoice_1.kilos_to_bill.assert_called()
        spy_invoice_2.kilos_to_bill.assert_called()
        
        
        # B) Verificar cuántas veces se llama kilos_to_bill() por factura
        # Sabiendo cómo está escrito el código en UnitTesting2.py,
        # se llama una vez para el total_kilos y otra para el weighted_sum.
        # Por tanto, esperamos que call_count sea exactamente 2.
        self.assertEqual(spy_invoice_1.kilos_to_bill.call_count, 2, 
                         "kilos_to_bill() debió llamarse 2 veces en la factura 1")
                         
        self.assertEqual(spy_invoice_2.kilos_to_bill.call_count, 2, 
                         "kilos_to_bill() debió llamarse 2 veces en la factura 2")
                         
        # Como extra, también podemos verificar que unit_price() se llamó exactamente 1 vez
        self.assertEqual(spy_invoice_1.unit_price.call_count, 1)
        self.assertEqual(spy_invoice_2.unit_price.call_count, 1)

if __name__ == '__main__':
    unittest.main()