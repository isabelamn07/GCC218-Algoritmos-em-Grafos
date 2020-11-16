# Criando os objetos

from clientes import Cliente
from bancos import Banco
from contas import Conta
joão = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "9721-3040")
josé = Cliente("José Vargas","9724-3040")
contaJM = Conta([joão, maria], 100)
contaJ = Conta([josé], 10)
tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 