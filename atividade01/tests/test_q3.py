import unittest
from atividade01.classes.q3 import Triangulo


class TestTriangulo(unittest.TestCase):
    def test_triangulo_escaleno_valido(self):
        triangulo = Triangulo(3, 4, 5)
        self.assertEqual(triangulo.tipo(), "Triângulo escaleno")

    def test_triangulo_isosceles_valido(self):
        triangulo = Triangulo(3, 3, 5)
        self.assertEqual(triangulo.tipo(), "Triângulo isósceles")

    def test_triangulo_equilatero_valido(self):
        triangulo = Triangulo(5, 5, 5)
        self.assertEqual(triangulo.tipo(), "Triângulo equilátero")

    def test_lado_zero(self):
        triangulo = Triangulo(0, 4, 5)
        self.assertEqual(triangulo.tipo(), "Não é um triângulo válido")

    def test_lado_negativo(self):
        triangulo = Triangulo(-3, 4, 5)
        self.assertEqual(triangulo.tipo(), "Não é um triângulo válido")

    def test_soma_2_lados_igual_3_lado(self):
        triangulo = Triangulo(1, 2, 3)
        self.assertEqual(triangulo.tipo(), "Não é um triângulo válido")


if __name__ == '__main__':
    unittest.main()
