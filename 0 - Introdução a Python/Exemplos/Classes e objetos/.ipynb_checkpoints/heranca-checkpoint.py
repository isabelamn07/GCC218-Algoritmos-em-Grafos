# Uso de herança para definir ContaEspecial
from contas import Conta

class ContaEspecial(Conta):
    def __init__(self, clientes, numeros, saldo = 0, limite = 0):
        Conta.__init__(self, clientes, numeros, saldo)
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 