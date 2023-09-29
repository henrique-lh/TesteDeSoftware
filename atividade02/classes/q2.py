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


class Aplicacao:

    def __init__(self, flag):
        self.flag = flag
        self.calculadora = Calculadora()

    def realiza_calculo(self, n1, n2):
        if self.flag == 'soma':
            return self.calculadora.somar(n1, n2)
        elif self.flag == 'subtração':
            return self.calculadora.subtrair(n1, n2)
        elif self.flag == 'multiplicação':
            return self.calculadora.multiplicar(n1, n2)
        elif self.flag == 'divisão':
            return self.calculadora.dividir(n1, n2)
        else:
            return 'Operação não foi realizada pois não está disponível'
