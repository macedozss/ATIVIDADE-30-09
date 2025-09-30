# Definição da classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")


# Definição da classe Usuario
class Usuario:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Código: {self.codigo}")


# Importando as classes do arquivo01
from arquivo01 import Livro, Usuario

# Criando um objeto da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis")

# Criando um objeto da classe Usuario
usuario1 = Usuario("Maria", 123)

# Exibindo os dados do livro
livro1.exibir_dados()
print()  # só para dar espaço na saída

# Exibindo os dados do usuário
usuario1.exibir_dados()