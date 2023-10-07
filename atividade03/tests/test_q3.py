import unittest
from atividade03.classes.q3 import Mecanico, Veiculo, Servico
from datetime import datetime


class TestOficina(unittest.TestCase):
    def test_funcionario_eh_premium(self):
        mecanico = Mecanico('00-1111-22-3', 'Henrique', ['Conserto de motor', 'Conserto de ar-condicionado', 'Manutenção de freios'])
        self.assertEqual(mecanico.funcionarioPremium(), True)

    def test_funcionario_nao_eh_premium(self):
        mecanico = Mecanico('00-1111-22-3', 'Henrique', ['Manutenção de freios'])
        self.assertEqual(mecanico.funcionarioPremium(), False)

    def test_esta_na_garantia_pickup(self):
        carro = Veiculo('ABC1B34', 'PICKUP', 5, 2022)
        years_later = datetime.now().year - carro.get_ano()
        self.assertLessEqual(years_later, carro.calculaGarantia())

    def test_nao_esta_na_garantia_pickup(self):
        carro = Veiculo('ABC1B34', 'PICKUP', 5, 2010)
        years_later = datetime.now().year - carro.get_ano()
        self.assertGreater(years_later, carro.calculaGarantia())

    def test_esta_na_garantia_suv(self):
        carro = Veiculo('ABC1B34', 'SUV', 5, 2021)
        years_later = datetime.now().year - carro.get_ano()
        self.assertLessEqual(years_later, carro.calculaGarantia())

    def test_nao_esta_na_garantia_suv(self):
        carro = Veiculo('ABC1B34', 'SUV', 5, 2019)
        years_later = datetime.now().year - carro.get_ano()
        self.assertGreater(years_later, carro.calculaGarantia())

    def test_esta_na_garantia_popular(self):
        carro = Veiculo('ABC1B34', 'POPULAR', 5, 2021)
        years_later = datetime.now().year - carro.get_ano()
        self.assertLessEqual(years_later, carro.calculaGarantia())

    def test_nao_esta_na_garantia_popular(self):
        carro = Veiculo('ABC1B34', 'POPULAR', 5, 2019)
        years_later = datetime.now().year - carro.get_ano()
        self.assertGreater(years_later, carro.calculaGarantia())


class TestServico(unittest.TestCase):
    def test_orde_servico(self):
        mecanico = Mecanico('00-1111-22-3', 'Henrique', ['Conserto de ar-condicionado', 'Manutenção de freios'])
        carro = Veiculo('ABC1B34', 'POPULAR', 0, 2019)

        servico = Servico('1', [], mecanico, carro)
        servico.ordemServico('Freios não funcionam')
        servico.ordemServico('Para-choque traseiro quebrou')

        expected_motivos = ['Freios não funcionam', 'Para-choque traseiro quebrou']
        expected_num_ocorrencias = 2

        self.assertEqual(servico.get_motivo(), expected_motivos)
        self.assertEqual(carro.get_numOcorrencias(), expected_num_ocorrencias)


if __name__ == '__main__':
    unittest.main()
