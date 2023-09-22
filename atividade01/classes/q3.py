
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
