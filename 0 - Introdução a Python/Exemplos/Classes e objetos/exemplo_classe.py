
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
tv = Televisao()
print(tv.ligada)
print(tv.canal)
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
print(tv.canal)
print(tv_sala.canal)

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 