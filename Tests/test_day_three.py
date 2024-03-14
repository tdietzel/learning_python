import sys
sys.path.append('../DailyPractice')
import day_three #ignore
import unittest

class UnitTest(unittest.TestCase):

  # Use below to run code before & after tests. @classmethod happens once not after every test

  # @classmethod
  # def setupClass(cls):
  #   print('setupClass')

  # @classmethod
  # def tearDownclass(cls):
  #   print('tearDownClass')

  # def setUp(self):
  #   num1 = 5
  #   num2 = 10

  # def tearDown(self):
  #   pass

  # must prefix name with 'test' to run correctly
  def test_add(self):
    self.assertEqual(day_three.add(10, 15), 25)

  def test_subtract(self):
    self.assertEqual(day_three.subtract(10, 5), 5)

  def test_multiply(self):
    self.assertEqual(day_three.multiply(15, 3), 45)
  
  def test_divide(self):
    self.assertEqual(day_three.divide(15, 3), 5)

# allows test file to be ran using 'python _fileName.py_'
if __name__ == '__main__':
  unittest.main()

# Assert methods & description
# https://www.tutorialspoint.com/unittest_framework/unittest_framework_assertion.htm#:~:text=Python%20testing%20framework%20uses%20Python's,identify%20the%20test%20as%20Failure.