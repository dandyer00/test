import unittest
from testApp import do_it

class TestDoIt(unittest.TestCase):

    def test_do_it1(self):
        result = do_it.do_it1("bob")
        self.assertEqual(result, "bob")

if __name__ == '__main__':
    unittest.main()