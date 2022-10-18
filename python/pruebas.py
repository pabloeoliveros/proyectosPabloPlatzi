import unittest

class cajaNegra(unittest.TestCase):
    def suma(self):
        num1 = 9
        num2 = 5
        
        resultado = suma(num1,num2)
        self.assertEqual(resultado, 15)



if __name__ == '__main__':
    unittest.main()