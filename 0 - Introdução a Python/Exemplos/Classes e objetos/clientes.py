# Classe Clientes (clientes.py)
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria Silva", "555-4321")
print(joão.nome)
print(joão.telefone)
print(maria.nome)
print(maria.telefone)

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 