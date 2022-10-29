import unittest
import csv

def obtener_monto(file_csv):
  with open(file_csv) as f:
    reader = csv.reader(f)
    next(reader) #omite las cabeceras
    suma = 0
    cont = 0
    for i in reader:
      suma += int(i[0])
      cont += 1
  return round(suma/cont, 2)

#print(obtener_monto('ejemplo.csv'))

class test_csv(unittest.TestCase):
    
    def testunitEqual(self):
        amount = obtener_monto('ejemplo.csv')
        self.assertAlmostEqual(amount, 146633.33)
    def test_unitNotEqual(self):
        amount = obtener_monto('ejemplo.csv')
        self.assertNotAlmostEqual(amount, 146633)

if __name__ == "__main__":
    unittest.main()

#unittest.main(argv=[''], verbosity = 2, exit = False)
