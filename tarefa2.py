# Definição da classe Jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0  # começa com 0 pontos

    def adicionar_pontos(self, valor):
        self.pontos += valor

    def exibir_pontos(self):
        print(f"Jogador: {self.nome}")
        print(f"Pontos: {self.pontos}")

# Importando a classe Jogador do arquivo01
from arquivo01 import Jogador

# Criando um objeto da classe Jogador
jogador1 = Jogador("Carlos")

# Adicionando pontos
jogador1.adicionar_pontos(10)
jogador1.adicionar_pontos(5)
jogador1.adicionar_pontos(20)

# Exibindo o resultado final
jogador1.exibir_pontos()