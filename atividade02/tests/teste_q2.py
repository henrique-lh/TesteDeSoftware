import unittest
from atividade02.classes.q2 import Aplicacao

class TestAplicacao(unittest.TestCase):
    def test_soma(self):
        app = Aplicacao('soma')
        expected = 8
        result = app.realiza_calculo(5, 3)
        self.assertEqual(result, expected)

    def test_subtracao(self):
        app = Aplicacao('subtração')
        expected = 6
        result = app.realiza_calculo(10, 4)
        self.assertEqual(result, expected)

    def test_multiplicacao(self):
        app = Aplicacao('multiplicação')
        expected = 42
        result = app.realiza_calculo(6, 7)
        self.assertEqual(result, expected)

    def test_divisao(self):
        app = Aplicacao('divisão')
        expected = 4
        result = app.realiza_calculo(8, 2)
        self.assertEqual(result, expected)

    def test_operacao_nao_disponivel(self):
        app = Aplicacao('potencia')
        expected = 'Operação não foi realizada pois não está disponível'
        result = app.realiza_calculo(2, 3)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
