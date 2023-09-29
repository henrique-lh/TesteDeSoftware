class Livro:

    def __init__(self, nome, edicao, autor, ISBN):
        self.nome = nome
        self.edicao = edicao
        self.autor = autor
        self.IBSN = ISBN

    def get_nome(self):
        return self.nome

    def get_edicao(self):
        return self.edicao

    def get_autor(self):
        return self.autor

    def get_IBSN(self):
        return self.IBSN

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_edicao(self, nova_edicao):
        self.edicao = nova_edicao

    def set_autor(self, novo_autor):
        self.autor = novo_autor

    def set_IBSN(self, novo_IBSN):
        self.IBSN = novo_IBSN

    def verifica_lancamento(self):
        return self.edicao > 2022


class Biblioteca:
    def __init__(self, nome, cnpj, anoFundacao, lista_livros=None):
        self.nome = nome
        self.cnpj = cnpj
        self.anoFundacao = anoFundacao

        if lista_livros is None:
            self.lista_livro = []
        else:
            self.lista_livro = lista_livros

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cnpj(self):
        return self.cnpj

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj

    def get_ano_fundacao(self):
        return self.anoFundacao

    def patrimonio_historico(self):
        return self.anoFundacao < 1980

    def add_livro(self, novo_livro):
        self.lista_livro.append(novo_livro)

    def remove_livro(self, nome_livro):
        self.lista_livro = [livro for livro in self.lista_livro if nome_livro != livro.nome]

    def busca_livro(self, nome_livro):
        return nome_livro in set([livro.nome for livro in self.lista_livro if livro.nome == nome_livro])

    def acervo_premium(self):
        return len([livro.edicao for livro in self.lista_livro if livro.verifica_lancamento()]) >= 5
