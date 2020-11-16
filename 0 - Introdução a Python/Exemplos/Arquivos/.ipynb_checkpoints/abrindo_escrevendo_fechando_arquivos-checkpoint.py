# Abrindo, escrevendo e fechando um arquivo

# arquivo de escrita números.txt
arquivo = open("números.txt","w")

# escreve números de 1 a 100 por linha no arquivo 
for linha in range(1,101):
    arquivo.write("%d\n" % linha)
arquivo.close()

# Abrindo, lendo e fechando um arquivo
arquivo = open("números.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

# Impressão dos parâmetros passados na linha de comando
import sys
print("Número de parâmetros: %d " % len(sys.argv))
for n, p in enumerate(sys.argv):
    print("Parâmetro %d = %s" % (n, p))

# Gravação de números pares e ímpares em arquivos diferentes
ímpares = open("ímpares.txt", "w")
pares = open("pares.txt", "w")
for n in range(0, 1000):
    if n % 2 == 0:
        pares.write("%d\n" % n)
    else:
        ímpares.write("%d\n" % n)
ímpares.close()
pares.close()

# Filtragem exclusiva dos múltiplos de quatro

multiplos4 = open("múltiplos de 4.txt", "w")
pares = open("pares.txt")
for l in pares.readlines():
    if int(l) % 4 == 0:
        multiplos4.write(l)
pares.close()
multiplos4.close()

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 