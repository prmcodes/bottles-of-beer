import BottlesofBeer
import unittest

class TestAdd(unittest.TestCase):
  def test_initial_bottles_of_beer(self):
      result = BottlesofBeer.bottles_of_beer
      self.assertEqual(result, 99)

if __name__ == '__main__':
    unittest.main()
