import unittest
import testing.testing_function as testFunc

class TestMain(unittest.TestCase):
  def setUp(self):
    print('about to run a function')

  def testNum(self):
    '''this is comment that will pop up when we test'''
    testParam = 10
    result = testFunc.doStuff(testParam)
    self.assertEqual(result, 15)

  def testString(self):
    testParam = 'alskdjf'
    result = testFunc.doStuff(testParam)
    self.assertIsInstance(result, ValueError)

  def testNoneType(self):
    testParam = None
    result = testFunc.doStuff(testParam)
    self.assertEqual(result, 'please enter a number')
  
  def testEmptyString(self):
    testParam = ''
    result = testFunc.doStuff(testParam)
    self.assertEqual(result, 'please enter a number')

# not very common: tearDown
  def tearDown(self):
    print('cleaning up')




#  run this unittest.main() file if this is the main file being ran
if __name__ == '__main__':
  unittest.main() 

'''
in CLI:

recommended when we have larger applications, multiple modules, and want to run one unit test for all those modules:

python3 -m unittest

python3 -m unittest -v 
v: verbose, gives us more information about the tests that we ran, which tests are run and which fail etc

vs what we have been doing before, running the testing-lesson.py file that contains our unittests:

python3 testing-lesson.py
'''