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