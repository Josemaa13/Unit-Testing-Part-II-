import unittest
from decimal import Decimal
from UnitTesting2 import *

class TestInvoiceLine(unittest.TestCase):
    def setUp(self):
        self.line = InvoiceLine(
            seq = 1,
            description = "prueba line 1",
            unitPriceEURPerKg=Decimal("2.25"),
            qtyKg=Decimal("10.5") 
        )
    
    def test_invoiceline_creates_with_correct_initial_state(self):
        
        self.assertEqual(len(self.line.partials),0)
        self.assertEqual(len(self.line.credit_note_items),0)
        self.assertEqual(len(self.line.price_adjustment_items),0)
        
        self.assertEqual(self.line.kilos_to_bill(), Decimal("0"))
        self.assertEqual(self.line.unit_price(), Decimal("0"))
        self.assertEqual(self.line.lineAmount, Decimal("23.625"))
        
    def test_add_partial_billing(self):
        p = PartialBilling(Decimal("10.50"))
        self.line.add_partial_billing(p)
        self.assertEqual(len(self.line.partials), 1)
        
    
          
        
    

if __name__ == '__main__':
    unittest.main()