import unittest
from unittest.mock import MagicMock
from decimal import Decimal
from UnitTesting2 import Provider, Invoice

class TestMockInvoiceInProvider(unittest.TestCase):
    def test_provider_aggregations_with_mocks(self):
        
        provider = Provider(name="Mocked Provider")
      
        inv_mock1 = MagicMock(spec=Invoice)
        inv_mock1.kilos_to_bill.return_value = Decimal("10.0")
        inv_mock1.unit_price.return_value = Decimal("2.0")
        inv_mock1.total = Decimal("20.0")

        inv_mock2 = MagicMock(spec=Invoice)
        inv_mock2.kilos_to_bill.return_value = Decimal("10.0")
        inv_mock2.unit_price.return_value = Decimal("4.0")
        inv_mock2.total = Decimal("40.0")

        provider.add_bill(inv_mock1)
        provider.add_bill(inv_mock2)
        
        # Total kilos: 10 + 10 = 20.0
        self.assertEqual(provider.total_kilos_to_bill(), Decimal("20.0"))
        
        # Precio medio ponderado: ((10*2) + (10*4)) / 20 = 3.0
        self.assertEqual(provider.avg_unit_price(), Decimal("3.0"))
        
        # Total facturado: 20 + 40 = 60.0
        self.assertEqual(provider.total_invoice_amount(), Decimal("60.0"))

    def test_provider_with_zero_kilos_mock(self):
        provider = Provider(name="Empty Provider")
        
        inv_mock = MagicMock(spec=Invoice)
        inv_mock.kilos_to_bill.return_value = Decimal("0")
        
        provider.add_bill(inv_mock)
        
        self.assertEqual(provider.avg_unit_price(), Decimal("0"))

if __name__ == '__main__':
    unittest.main()