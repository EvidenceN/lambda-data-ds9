import unittest
from acme import Product
from acme_report import generate_products, adjectives, nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_weight(self):
        prod = Product('test weight')
        self.assertEqual(prod.weight, 20)

    def ratio(self):
        prod = Product('test weight and price')
        self.assertLessEqual(prod.price/prod.weight, 0.5)

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        self.assertEqual(generate_products(num_products=30), 30)

    def test_legal_names(self):
        self.assertListEqual([adjectives], [nouns], dtype = 'string')

if __name__ == '__main__':
    unittest.main()
