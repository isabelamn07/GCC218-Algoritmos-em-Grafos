# Verificação se é diretório ou arquivo
import os
import os.path
for a in os.listdir("."):
    if os.path.isdir(a):
        print("%s/" % a)
    elif os.path.isfile(a):
        print("%s" % a)        
        
# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 