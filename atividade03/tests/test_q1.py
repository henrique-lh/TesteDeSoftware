import unittest
from atividade03.classes.q1 import Triangulo


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

    def test_area_triangulo_equilatero(self):
        triangulo = Triangulo(5, 5, 5)
        expected = 10.625
        self.assertAlmostEqual(triangulo.calculaArea(), expected, delta=0.3)

    def test_area_triangulo_isosceles(self):
        triangulo = Triangulo(15, 18, 15)
        expected = 108
        self.assertEqual(triangulo.calculaArea(), expected)

    def test_area_triangulo_escaleno(self):
        triangulo = Triangulo(14, 9, 7)
        expected = 12 * 5 ** 0.5
        self.assertAlmostEqual(triangulo.calculaArea(), expected)

    def test_perimetro_triangulo_equilatero(self):
        triangulo = Triangulo(5, 5, 5)
        expected = 15
        self.assertEqual(triangulo.calculaPerimetro(), expected)

    def test_perimetro_triangulo_isosceles(self):
        triangulo = Triangulo(15, 18, 15)
        expected = 48
        self.assertEqual(triangulo.calculaPerimetro(), expected)

    def test_perimetro_triangulo_escaleno(self):
        triangulo = Triangulo(14, 9, 7)
        expected = 30
        self.assertAlmostEqual(triangulo.calculaPerimetro(), expected)


if __name__ == '__main__':
    unittest.main()
