import unittest
from scortest.myfirst import square_function


class TestMyFirst(unittest.TestCase):

    def test_square_function(self):
        r = square_function(2,3,4)
        self.assertEqual(r, 29)


if __name__ == '__main__':
    unittest.main()        