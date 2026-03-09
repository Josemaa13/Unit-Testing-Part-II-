import unittest
from unittest.mock import MagicMock
from decimal import Decimal
from datetime import date
from UnitTesting2 import Invoice

class TestInvoiceWithStubs(unittest.TestCase):
    def test_total_calculation_with_line_stubs(self):
        # 1. Setup: Creamos la factura
        inv = Invoice(number="INV-001", date=date.today(), currency="EUR")
        
        # 2. CREACIÓN DE STUBS:
        line_stub1 = MagicMock()
        line_stub1.lineAmount = Decimal("100.00")
        
        line_stub2 = MagicMock()
        line_stub2.lineAmount = Decimal("50.50")
        
        # 3. Añadimos los stubs a la factura
        inv.add_line(line_stub1)
        inv.add_line(line_stub2)
        
        # 4. Verificación:
        # 100.00 + 50.50 = 150.50
        self.assertEqual(inv.total, Decimal("150.50"))
    
    def test_kilos_to_bill(self):
        inv = Invoice(number="INV-003", date=date.today(), currency="USD")
        
        line_stub3 = MagicMock()
        line_stub3.kilos_to_bill.return_value = Decimal("3.55")
        
        line_stub4 = MagicMock()
        line_stub4.kilos_to_bill.return_value = Decimal("1.35")
        
        inv.add_line(line_stub3)
        inv.add_line(line_stub4)
        
        self.assertEqual(inv.kilos_to_bill(), Decimal("4.90"))
        
    def test_unit_price(self):
        inv = Invoice(number="INV-003", date=date.today(), currency="USD")
        
        line_stub5 = MagicMock()
        line_stub5.kilos_to_bill.return_value = Decimal("1")
        line_stub5.unit_price.return_value = Decimal("2.0")
        
        line_stub6 = MagicMock()
        line_stub6.kilos_to_bill.return_value = Decimal("3.0")
        line_stub6.unit_price.return_value = Decimal("5.0")
        
        inv.add_line(line_stub5)
        inv.add_line(line_stub6)
        
        self.assertEqual(inv.unit_price(), Decimal("4.25"))
        

