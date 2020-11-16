#  Adição de métodos para mudar o canal

class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def muda_canal_para_baixo(self):
        self.canal -= 1
    def muda_canal_para_cima(self):
        self.canal += 1

tv = Televisão()
print(tv.muda_canal_para_cima())
print(tv.muda_canal_para_cima())
print(tv.canal)
print(tv.muda_canal_para_baixo())
print(tv.canal)

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 