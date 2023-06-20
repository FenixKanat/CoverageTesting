import unittest;
from Coverage.operations import compute
from Coverage.operations import compute2

#Fenix Kanat
class TestApp(unittest.TestCase):
    def setUp(self):
        self.a = 25
        self.b = 0
        self.c = 25
       
    def test_subtraction(self):
        result = compute(self.a, self.b, 'subtract')
        self.assertEqual(result, 25)
    def test_add(self):
        result = compute(self.a, self.b, 'add' )
        self.assertEqual(result,25)
    def test_multiply(self):
        result = compute(self.a, self.b, 'multiply')
        self.assertEqual(result, 0)
    def test_divide(self):
        result = compute2(self.a, self.c, 'divide')
        self.assertEqual(result, 1)
def suite():
   suites = unittest.TestSuite()
   suites.addTests(
      unittest.TestLoader().loadTestsFromTestCase(TestApp)
    )
   return suites
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())