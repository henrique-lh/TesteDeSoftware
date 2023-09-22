import unittest
from atividade01.classes.q2 import Calculadora


class TestCalculadora(unittest.TestCase):
    def test_soma_numeros_positivos(self):
        calc = Calculadora()
        expected = 33
        self.assertEqual(calc.somar(15, 18), expected)

    def test_soma_numeros_negativos(self):
        calc = Calculadora()
        expected = -33
        self.assertEqual(calc.somar(-15, -18), expected)

    def test_soma_numero_positivo_com_zero(self):
        calc = Calculadora()
        expected = 15
        self.assertEqual(calc.somar(15, 0), expected)

    def test_soma_numeros_negativo_com_zero(self):
        calc = Calculadora()
        expected = -15
        self.assertEqual(calc.somar(-15, 0), expected)

    def test_soma_numero_positivo_com_negativo(self):
        calc = Calculadora()
        expected = 3
        self.assertEqual(calc.somar(18, -15), expected)

    def test_subtrai_numeros_positivos(self):
        calc = Calculadora()
        expected = 3
        self.assertEqual(calc.subtrair(18, 15), expected)

    def test_subtrai_numeros_negativos(self):
        calc = Calculadora()
        expected = 3
        self.assertEqual(calc.subtrair(-15, -18), expected)

    def test_subtrai_numero_positivo_com_zero(self):
        calc = Calculadora()
        expected = 15
        self.assertEqual(calc.subtrair(15, 0), expected)

    def test_subtrai_numeros_negativo_com_zero(self):
        calc = Calculadora()
        expected = -15
        self.assertEqual(calc.subtrair(-15, 0), expected)

    def test_subtrai_numero_positivo_com_negativo(self):
        calc = Calculadora()
        expected = 3
        self.assertEqual(calc.subtrair(18, 15), expected)

    def test_multplica_numeros_positivos(self):
        calc = Calculadora()
        expected = 10
        self.assertEqual(calc.multiplicar(2, 5), expected)

    def test_multiplica_numeros_negativos(self):
        calc = Calculadora()
        expected = 10
        self.assertEqual(calc.multiplicar(-2, -5), expected)

    def test_multiplica_numero_positivo_com_negativo(self):
        calc = Calculadora()
        expected = -10
        self.assertEqual(calc.multiplicar(-2, 5), expected)

    def test_multiplica_numero_positivo_com_zero(self):
        calc = Calculadora()
        expected = 0
        self.assertEqual(calc.multiplicar(100, 0), expected)

    def test_multiplica_numero_negativo_com_zero(self):
        calc = Calculadora()
        expected = 0
        self.assertEqual(calc.multiplicar(-100, 0), expected)

    def test_multiplica_numero_positivo_com_um(self):
        calc = Calculadora()
        expected = 100
        self.assertEqual(calc.multiplicar(100, 1), expected)

    def test_multiplica_numero_negativo_com_um(self):
        calc = Calculadora()
        expected = -100
        self.assertEqual(calc.multiplicar(-100, 1), expected)

    def test_divisao_numeros_positivos(self):
        calc = Calculadora()
        expected = 5
        self.assertEqual(calc.dividir(10, 2), expected)

    def test_divisao_numeros_negativos(self):
        calc = Calculadora()
        expected = 5
        self.assertEqual(calc.dividir(-10, -2), expected)

    def test_divisao_numero_positivo_com_negativo(self):
        calc = Calculadora()
        expected = -5
        self.assertEqual(calc.dividir(10, -2), expected)

    def test_divisao_por_um(self):
        calc = Calculadora()
        expected = 10
        self.assertEqual(calc.dividir(10, 1), expected)

    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ZeroDivisionError):
            calc.dividir(10, 0)


if __name__ == '__main__':
    unittest.main()
