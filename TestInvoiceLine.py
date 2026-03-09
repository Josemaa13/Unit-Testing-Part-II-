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
        

    
    
        
        
          
        
    






    # ==========================================
    # 2. GESTIÓN DE RELACIONES (Métodos add_*)
    # ==========================================

    #def test_add_credit_note_item_enforces_bidirectional_link(self):
     #   """
      #  Objetivo: Añadir un CreditNoteBillItem usando add_credit_note_item().
       # Verificar que el ítem está en la lista self.credit_note_items Y que 
        #la propiedad 'target' del ítem apunta a esta misma línea.
        #"""
        #pass

    #def test_add_price_adjustment_item_enforces_bidirectional_link(self):
    #    """
    #    Objetivo: Añadir un PriceAdjustmentBillItem. Verificar que se guarda en 
    #    self.price_adjustment_items Y que el 'target' del ítem es esta línea.
    #    """
    #    pass

    # ==========================================
    # 3. LÓGICA DE NEGOCIO: kilos_to_bill()
    # ==========================================
    #def test_kilos_to_bill_without_modifiers_returns_base_qty(self):
    #    """
    #    Objetivo: Si no hay facturas parciales ni notas de crédito, 
    #    kilos_to_bill() debe ser igual a qtyKg.
    #    """
    #    pass
#
    #def test_kilos_to_bill_subtracts_partial_billings(self):
    #    """
    #    Objetivo: Añadir uno o varios PartialBilling y comprobar que 
    #    kilos_to_bill() resta esos kilos de la cantidad base.
    #    """
    #    pass
#
    #def test_kilos_to_bill_applies_credit_note_deltas(self):
    #    """
    #    Objetivo: Añadir un CreditNoteBillItem (con un delta negativo o positivo) 
    #    y verificar que kilos_to_bill() refleja esa suma/resta.
    #    """
    #    pass
#
    #def test_kilos_to_bill_is_clamped_at_zero(self):
    #    """
    #    Objetivo: CASO LÍMITE. Si los PartialBilling suman más kilos que el 
    #    qtyKg base, kilos_to_bill() debe devolver 0, no un número negativo.
    #    """
    #    pass

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