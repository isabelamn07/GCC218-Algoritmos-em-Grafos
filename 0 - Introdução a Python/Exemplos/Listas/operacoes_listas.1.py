# lista vazia 
L = []

# Criando uma lista de inteiros Z
Z = [25,8,9]
print(Z)

# Mostrando a lista Z da listagem anterior por posição

Z = [25, 8, 9]
print(Z[0])
print(Z[1])
print(Z[2])


# Modificação de uma lista

Z = [25, 8, 9]
print(Z[0])
Z[0] = 7
print(Z[0])
print(Z)


# Operação simples com listas

nota = [6, 7, 8, 9, 5]
soma = 0
x = 0
while x < 5:
    soma += nota[x]
    x += 1
print(" Média: %5.2f " % (soma/x))


# Operações simples com listas

números = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    números[x] = float(input("Número %d: " % (x+1)))
    x += 1
while True:
    escolhido = int(input(" Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(" Você escolheu o número: %d " % (números[escolhido - 1]))


L1 = [1, 2, 3, 4, 5, 6]

# A lista V não recebeu uma cópia de L e sim começou a apontar par a mesma posição
V = L1
print(V)
print(L1)

V[0] = 7

print(V)
print(L)

# Para copiar uma lista

L = [1,2,3,4,5]
V = L[:]
V[0] = 6
print(L)
print(V)

# Como acessar posições em uma lista

L = [1, 2, 3, 4, 5]
print(L[0:5])
print(L[:5])
print(L[:-1])
print(L[1:3])
print(L[1:4])
print(L[3:])
print(L[:3])
print(L[-1])
print(L[-2])

# Tamanho de listas
L = [12, 9, 5]
print(len(L))
V = []
print(len(V))

# Adicionar elementos em uma lista

L3 = []
print(L3)
L3.append("a")
print(L3)
L3.append("b")
print(L3)
L3.append("c")
print(L3)
print(len(L3))

# Adição de listas
L = []
L = L+[1]
print(L)
L += [2]
print(L)
L += [3, 4, 5]
print(L)

# Extend 

L = ["a"]
L.append("b")
print(L)
L.extend(["c"])
print(L)
L.append(["d","e"])
print(L)
L.extend(["e","f","g"])
print(L)


# Criar lista em um intervalo de inteiros

L = list(range(101))
print(L)
del L[1:99]
print(L)

#Usando o for
L = [8, 9, 15]
for e in L:
    print(e)


# Range
for v in range(10):
    print(v)

# Uso da função range com intervalos

for v in range(5, 8):
    print(v)

for t in range(3, 33, 3):
    print(t, end=" ")
print()

# Transformação do resultado de range em uma lista
L = list(range(100, 1100, 50))
print(L)

# listas com string, acessando letras

S = ["maças", "peras", "kiwis"]
print(S[0][0])
print(S[0][1])
print(S[2][2])
print(S[2][0])


##Dicionarios

# Criação de um dicionario

dicionario = {}
print(dicionario)

dicionario = {"laranja": 1.49}
print(dicionario)

# Acesso a uma chave inexistente
tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

#print(tabela["Manga"])

# Verificação da existência de uma chave

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}

print("Manga" in tabela)
print("Batata" in tabela)

# Obtenção de uma lista de chaves e valores

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}
print(tabela.keys())
print(tabela.values())

# Tuplas

tupla = ("a", "b", "c")
print(tuple)

print(tupla[0])
print(tupla[2])
print(tupla[1:])
tupla * 2
print(tupla * 2)
print(len(tupla))

# tuple[0] = "A"
for elemento in tupla:
    print(elemento)
tupla = 100, 200, 300
print(tupla)
a, b = 10, 20
print(a)
print(b)
t1 = (1)
print(t1)
t2 = (1,)
print(t2)
t3 = 1,
print(t3)
t4 = ()
print(t4)
len(t4)

L = [1, 2, 3]
print(L)
T = tuple(L)
print(T)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1+t2)

tupla = ("a", ["b", "c", "d"])
print(tupla)
len(tupla)
tupla[1].append("e")
print(tupla)

lista = [1, 3.14, 'Jose']

print(lista[:2])

lista2 = ['eusebio',57]

lista3 = lista + lista2
print(lista3)

lista.pop(len(lista) -1 )
print(lista)

lista.remove(1)
print(lista)
lista.append(1)
lista.append('rojas')
lista.extend('rojas')
print(lista)

t_lista = tuple(lista)

lista.insert(0,1)
print(lista)

lista.reverse()
print(lista)

print(lista[::-1])
