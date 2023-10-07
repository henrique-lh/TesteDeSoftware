class Mecanico:

    def __init__(self, matricula, nome, especialidades):
        self.matricula = matricula
        self.nome = nome
        self.especialidades = especialidades

    def get_matricula(self):
        return self.matricula

    def get_nome(self):
        return self.nome

    def get_especialidades(self):
        return self.especialidades

    def set_matricula(self, new_value):
        self.matricula = new_value

    def set_nome(self, new_value):
        self.nome = new_value

    def set_especialidades(self, new_value):
        self.especialidades = new_value

    def funcionarioPremium(self):
        return len(self.especialidades) > 1


class Veiculo:

    def __init__(self, placa, tipo, numOcorrencias, ano):
        self.placa = placa
        self.tipo = tipo
        self.numOcorrencias = numOcorrencias
        self.ano = ano

    def get_placa(self):
        return self.placa

    def get_tipo(self):
        return self.tipo

    def get_numOcorrencias(self):
        return self.numOcorrencias

    def get_ano(self):
        return self.ano

    def set_placa(self, new_value):
        self.placa = new_value

    def set_tipo(self, new_value):
        self.tipo = new_value

    def set_numOcorrencias(self, new_value):
        self.numOcorrencias = new_value

    def set_ano(self, new_value):
        self.ano = new_value

    def calculaGarantia(self):
        return 2


class Servico:

    def __init__(self, identificador, motivo, mecanico, veiculo):
        self.identificador = identificador
        self.motivo = motivo
        self.mecanico = mecanico
        self.veiculo = veiculo

    def get_identificador(self):
        return self.identificador

    def set_identificador(self, new_value):
        self.identificador = new_value

    def get_motivo(self):
        return self.motivo

    def set_motivo(self, new_value):
        self.motivo = new_value

    def get_mecanico(self):
        return self.mecanico

    def set_mecanico(self, new_value):
        self.mecanico = new_value

    def get_veiculo(self):
        return self.veiculo

    def set_veiculo(self, new_value):
        self.veiculo = new_value

    def ordemServico(self, motivo):
        self.motivo.append(motivo)
        self.veiculo.set_numOcorrencias(self.veiculo.get_numOcorrencias() + 1)

