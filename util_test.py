import unittest
from util import *

class TestUtil(unittest.TestCase):

    def test_is_string(self):
        self.assertTrue(is_string('"x"'))
        self.assertFalse(is_string("x"))
    
    def test_is_number(self):
        self.assertTrue(is_number("1"))
        self.assertFalse(is_number('"1"'))

    def test_to_string(self):
        x = read_string('"x"')
        self.assertTrue(isinstance(x, String))
        self.assertFalse(isinstance(x, Symbol))
        self.assertEqual("x", x)

    def test_to_symbol(self):
        x = read_symbol('x')
        self.assertTrue(isinstance(x, Symbol))
        self.assertFalse(isinstance(x, String))
        self.assertEqual(Symbol('x'), x)

    def test_toNumber(self):
        x = read_number('1')
        self.assertTrue(isinstance(x, Number))
        self.assertFalse(isinstance(x, String))
        self.assertEqual(Number(1), x)

    def test_list_to_pair(self):
        p = list_to_pair([1, 2, 3])
        self.assertEqual(cons(1, cons(2, cons(3, None))), p)

    def test_pair_to_list(self):
        p = cons(1, cons(2, cons(3, None)))
        self.assertEqual(pair_to_list(p), [1, 2, 3])

    def test_map(self):
        p = cons(1, cons(2, cons(3, None)))
        print(pair_map(lambda x: x * 2, p))
        self.assertEqual(pair_map(lambda x: x * 2, p), list_to_pair([2, 4, 6]))

if __name__ == '__main__':
    unittest.main()