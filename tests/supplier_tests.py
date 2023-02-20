import unittest
from models.supplier import Supplier 

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.name = "Buchanan's"
        self.contact_info = "(Phone: 01475 722271), (Address: Fort Matilda Industrial Estate, Greenock, Inverclyde, Scotland)"
        self.supplier = Supplier(self.name, self.contact_info)

    def test_supplier_has_name(self):
        self.assertEqual("Buchanan's", self.supplier.name)

