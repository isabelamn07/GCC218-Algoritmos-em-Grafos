# Módulo soma

import entrada
L = []
for x in range(10):
    L.append(entrada.valida_inteiro("Digite um numero: ", 0, 20))
print(" Soma: %d " % (sum(L)))
