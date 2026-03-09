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
        
        self.assertEqual(self.line.kilos_to_bill(), Decimal("10.5"))
        self.assertEqual(self.line.unit_price(), Decimal("2.25"))
        self.assertEqual(self.line.lineAmount, Decimal("23.625"))
        
    def test_add_partial_billing(self):
        p = PartialBilling(Decimal("10.50"))
        self.line.add_partial_billing(p)
        self.assertEqual(len(self.line.partials), 1)
        self.assertEqual(self.line.kilos_to_bill(), Decimal("0"))
        self.assertEqual(self.line.unit_price(), Decimal("2.25"))
        
    def test_add_credit_note_item(self):
        note = CreditNoteBillItem(1, Decimal("2.5"), "test", self.line)
        self.line.add_credit_note_item(note)
        self.assertEqual(len(self.line.credit_note_items),1)
        self.assertIs(note.target, self.line)
        
    
    def test_add_price_adjustment_item(self):
        adj = PriceAdjustmentBillItem(1, Decimal("1.5"), Decimal("2"), Decimal("1"), "test", self.line)
        self.line.add_price_adjustment_item(adj)
        self.assertEqual(len(self.line.price_adjustment_items),1)
        self.assertIs(adj.target, self.line)
        

    def test_kilos_to_bill_without_modifiers_returns_base_qty(self):
        self.assertEqual(self.line.kilos_to_bill(), Decimal("10.5"))

    def test_kilos_to_bill_subtracts_partial_billings(self):
        """Resta los kilos de los PartialBilling de la cantidad base."""
        self.line.add_partial_billing(PartialBilling(Decimal("2.0")))
        self.line.add_partial_billing(PartialBilling(Decimal("3.5")))
        # 10.5 - 2.0 - 3.5 = 5.0
        self.assertEqual(self.line.kilos_to_bill(), Decimal("5.0"))

    def test_kilos_to_bill_applies_credit_note_deltas(self):
        """Aplica deltas (positivos o negativos) de notas de crédito."""
        # Restamos 2kg mediante una nota de crédito
        CreditNoteBillItem(1, Decimal("-2.0"), "Devolución", self.line)
        # 10.5 - 2.0 = 8.5
        self.assertEqual(self.line.kilos_to_bill(), Decimal("8.5"))

    def test_kilos_to_bill_is_clamped_at_zero(self):
        """CASO LÍMITE: No permite que los kilos a facturar sean negativos."""
        # Añadimos facturación parcial mayor a la cantidad original
        self.line.add_partial_billing(PartialBilling(Decimal("20.0")))
        # Aunque 10.5 - 20 = -9.5, el método debe devolver 0
        self.assertEqual(self.line.kilos_to_bill(), Decimal("0"))
        
    def test_kilos_to_bill_integration_mixed_modifiers(self):
        """Combinación de parciales y notas de crédito."""
        self.line.add_partial_billing(PartialBilling(Decimal("5.0"))) # 10.5 - 5 = 5.5
        CreditNoteBillItem(1, Decimal("-1.5"), "Ajuste", self.line)    # 5.5 - 1.5 = 4.0
        CreditNoteBillItem(2, Decimal("2.0"), "Error previo", self.line) # 4.0 + 2.0 = 6.0
        
        self.assertEqual(self.line.kilos_to_bill(), Decimal("6.0"))
        
    
    def test_unit_price_without_modifiers_returns_base_price(self):
        self.line.add_partial_billing(PriceAdjustmentBillItem(1, Decimal('0'), Decimal('2'), Decimal('1'), ":)", self.line))
        self.assertEqual(self.line.unit_price(), Decimal("2.25"))
    
    def test_unit_price_with_delta(self):
        self.line.add_partial_billing(PriceAdjustmentBillItem(1, Decimal('1'), Decimal('2'), Decimal('0.7'), ":)", self.line))
        self.line.add_partial_billing(PriceAdjustmentBillItem(2, Decimal('1.5'), Decimal('2'), Decimal('1'), ":(", self.line))
        self.assertEqual(self.line.unit_price(), Decimal("4.75")) # 2.25 + 1 + 1.5 = 4.75
        
    


    
    
        
        
          
    # ==========================================
    # 4. LÓGICA DE NEGOCIO: unit_price()
    # ==========================================
   # def test_unit_price_without_modifiers_returns_base_price(self):
   #     """
   #     Objetivo: Si no hay ajustes de precio, unit_price() debe 
   #     devolver el unitPriceEURPerKg original.
   #     """
   #     pass
#
   # def test_unit_price_applies_price_adjustments(self):
   #     """
   #     Objetivo: Añadir varios PriceAdjustmentBillItem con diferentes deltas 
   #     y verificar que unit_price() devuelve la suma correcta (base + deltas).
   #     """
   #     pass
#
   # # ==========================================
   # # 5. LÓGICA DE NEGOCIO: lineAmount (Propiedad)
   # # ==========================================
   # def test_lineAmount_calculates_correctly_with_mixed_modifiers(self):
   #     """
   #     Objetivo: TEST DE INTEGRACIÓN. Crear una línea, añadirle un PartialBilling, 
   #     una nota de crédito y un ajuste de precio. Verificar que lineAmount es 
   #     exactamente el resultado de kilos_to_bill() * unit_price().
   #     """
   #     pass

if __name__ == '__main__':
    unittest.main()