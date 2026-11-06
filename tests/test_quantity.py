import unittest

from warehouse.quantity import parse_quantity


class QuantityParserTests(unittest.TestCase):
    def test_valid_positive(self):
        self.assertEqual(parse_quantity("5"), 5)
        self.assertEqual(parse_quantity("  12  "), 12)

    def test_zero(self):
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_negative_large_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-100")
