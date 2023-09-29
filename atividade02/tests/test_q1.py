import unittest
from atividade02.classes.q1 import Livro, Biblioteca


class LivroTeste(unittest.TestCase):

    def test_get_nome(self):

        livro = Livro('Memórias Póstumas de Brás Cubas', 1881, 'Machado de Assis', '9780451524935')

        expected = 'Memórias Póstumas de Brás Cubas'

        self.assertEqual(livro.get_nome(), expected)

    def test_get_edicao(self):

        livro = Livro('Memórias Póstumas de Brás Cubas', 1881, 'Machado de Assis', '9780451524935')

        expected = 1881

        self.assertEqual(livro.get_edicao(), expected)

    def test_get_autor(self):

        livro = Livro('Memórias Póstumas de Brás Cubas', 1881, 'Machado de Assis', '9780451524935')

        expected = 'Machado de Assis'

        self.assertEqual(livro.get_autor(), expected)

    def test_get_IBSN(self):

        livro = Livro('Memórias Póstumas de Brás Cubas', 1881, 'Machado de Assis', '9780451524935')

        expected = '9780451524935'

        self.assertEqual(livro.get_IBSN(), expected)

    def test_set_nome(self):

        livro = Livro('Memórias Póstumas de Brás Cubas', 1572, 'Luís de Camões', '1234567890')

        expected = 'Os Lusíadas'

        livro.set_nome('Os Lusíadas')

        self.assertEqual(livro.get_nome(), expected)

    def test_get_edicao(self):

        livro = Livro('Os Lusíadas', 1881, 'Luís de Camões', '1234567890')

        expected = 1572

        livro.set_edicao(1572)

        self.assertEqual(livro.get_edicao(), expected)

    def test_set_autor(self):
        livro = Livro('Os Lusíadas', 1881, 'Luís de Camarões', '1234567890')

        expected = 'Luís de Camões'

        livro.set_autor('Luís de Camões')

        self.assertEqual(livro.get_autor(), expected)

    def test_set_IBSN(self):
        livro = Livro('Os Lusíadas', 1881, 'Luís de Camarões', '9780451524935')

        expected = '1234567890'

        livro.set_IBSN('1234567890')

        self.assertEqual(livro.get_IBSN(), expected)

    def test_livro_velho(self):
        livro = Livro('Os Lusíadas', 1881, 'Luís de Camarões', '1234567890')
        self.assertFalse(livro.verifica_lancamento(), 'Livro não foi lançado antes de 2022')

    def test_livro_novo(self):
        livro = Livro('Cabeça Fria, Coração Quente', 2023, 'Abel Ferreira', '9876543210')
        self.assertTrue(livro.verifica_lancamento(), 'Livro foi lançado em de 2022 ou posteriormente')


class BibliotecaTest(unittest.TestCase):
    def test_get_nome(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 1975)
        expected = "Biblioteca Municipal"
        self.assertEqual(biblioteca.get_nome(), expected)

    def test_set_nome(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 1975)
        biblioteca.set_nome("Biblioteca Aves")
        expected = "Biblioteca Aves"
        self.assertEqual(biblioteca.get_nome(), expected)

    def test_get_cnpj(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 1975)
        expected = "1234567890"
        self.assertEqual(biblioteca.get_cnpj(), expected)

    def test_set_cnpj(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 1975)
        biblioteca.set_cnpj("0987654321")
        expected = "0987654321"
        self.assertEqual(biblioteca.get_cnpj(), expected)

    def test_get_ano_fundacao(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 2000)
        expected = 2000
        self.assertEqual(biblioteca.get_ano_fundacao(), expected)

    def test_patrimonio_historico_true(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 1970)
        self.assertTrue(biblioteca.patrimonio_historico())

    def test_patrimonio_historico_false(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 2000)
        self.assertFalse(biblioteca.patrimonio_historico())

    def test_acervo_premium_true(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 2000)
        novos_livros = [
            Livro("Aventuras em Python", 2023, "João Silva", "978-1234567890"),
            Livro("Introdução à Inteligência Artificial", 2023, "Maria Santos", "978-9876543210"),
            Livro("Python Avançado", 2024, "Carlos Oliveira", "978-5678901234"),
            Livro("História da Ciência", 2024, "Ana Pereira", "978-0123456789"),
            Livro("Programação Web Moderna", 2023, "Pedro Almeida", "978-3456789012")
        ]
        for nl in novos_livros:
            biblioteca.add_livro(nl)
        self.assertTrue(biblioteca.acervo_premium())

    def test_acervo_premium_false(self):
        biblioteca = Biblioteca("Biblioteca Municipal", "1234567890", 2000)
        novos_livros = [
            Livro("A Revolução dos Livros", 1500, "Autor Desconhecido", "978-1234567890"),
            Livro("Aventuras de Sherlock Holmes", 1892, "Arthur Conan Doyle", "978-9876543210"),
            Livro("Dom Quixote", 1605, "Miguel de Cervantes", "978-5678901234"),
            Livro("Romeu e Julieta", 1597, "William Shakespeare", "978-0123456789"),
            Livro("Programação Web Moderna", 2023, "Pedro Almeida", "978-3456789012")

        ]
        for nl in novos_livros:
            biblioteca.add_livro(nl)
        self.assertFalse(biblioteca.acervo_premium())


if __name__ == '__main__':
    unittest.main()
