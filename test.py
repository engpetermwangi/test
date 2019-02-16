import unittest

from calc import add

class TestCalc(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(add(5,5), 10)

if __name__ == "__main()":
  unittest.main()
