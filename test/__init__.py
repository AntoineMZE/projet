import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
