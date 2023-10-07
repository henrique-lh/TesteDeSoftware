from math import pow, sqrt


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def eh_valido(self):
        if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
            return False
        if self.lado1 + self.lado2 <= self.lado3 or self.lado1 + self.lado3 <= self.lado2 or self.lado2 + self.lado3 <= self.lado1:
            return False
        return True

    def tipo(self):
        if not self.eh_valido():
            return "Não é um triângulo válido"
        if self.lado1 == self.lado2 == self.lado3:
            return "Triângulo equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"

    def calculaPerimetro(self):
        if not self.eh_valido():
            return 'Triângulo não é válido'
        return self.lado1 + self.lado2 + self.lado3

    @staticmethod
    def encontrar_lados_iguais(lado1, lado2, lado3):
        if lado1 == lado2:
            return lado1, lado3
        elif lado1 == lado3:
            return lado1, lado2
        return lado2, lado1

    @staticmethod
    def pitagoras(hip, cateto):
        return sqrt(pow(hip, 2) - pow(cateto, 2))

    def calcula_semiperimetro(self):
        return self.calculaPerimetro() / 2

    def calculaArea(self):
        if not self.eh_valido():
            return "Triângulo não é válido"

        if self.tipo() == "Triângulo equilátero":
            return (pow(self.lado1, 2) * sqrt(3)) / 4
        elif self.tipo() == "Triângulo isósceles":
            l1, l3 = self.encontrar_lados_iguais(self.lado1, self.lado2, self.lado3)
            altura = self.pitagoras(l1, l3 / 2)
            return l3 * altura / 2
        p = self.calcula_semiperimetro()
        return sqrt(p * (p - self.lado1) * (p - self.lado2) * (p - self.lado3))
