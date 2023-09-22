class Calculadora:

    def __init__(self):
        self.resultado = 0

    def somar(self, n1, n2):
        self.resultado = n1 + n2
        return self.resultado

    def subtrair(self, n1, n2):
         self.resultado = n1 - n2
         return self.resultado

    def multiplicar(self, n1, n2):
        self.resultado = n1 * n2
        return self.resultado

    def dividir(self, n1, n2):
        self.resultado = n1 / n2
        return self.resultado
