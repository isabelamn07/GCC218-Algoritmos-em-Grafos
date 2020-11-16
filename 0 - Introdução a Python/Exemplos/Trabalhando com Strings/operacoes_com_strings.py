# Convertendo uma string em lista
L = list("Alô mundo")
L[0] = "a"
print(L)
print(L[0])
s = "".join(L)
print(s)

# Verificação parcial de srings
nome = "João da Silva"
print(nome.startswith("João"))
print(nome.startswith("joão"))
print(nome.endswith("Silva"))

# Exemplos de conversão em maiúsculas e minúsculas
s = " O rato roeu a roupa do Rei de Roma"

print(s.lower())
print(s.upper())
print(s.lower().startswith(" o rato"))
print(s.upper().startswith(" O RATO"))

s = "Maria Amélia Souze"
print("Amélia" in s)
print("maria" in s)
print("a A" in s)

# Pesquisa de palavras em uma string usando not in
s = "Todos os caminhos levam a Roma"
print("levam " not in s)


# Combinação de lower e upper com in e not in
s = "João comprou um carro"
print("joão" in s.lower())

# Contagem de letra e palavras
t = "um tigre, dois tigres, três tigres"
print(t.count("tigre"))
print(t.count("tigres"))
print(t.count("t"))
print(t.count("z"))


# Pesquisa de strings com find
s = "Hello darkness my old friend"
print(s.find("dar"))
print(s.find("ok"))

# Pesquisa de strings com rfind
s = " Um dia de sol"
print(s.rfind("d"))
print(s.find("d"))

# Pesquisa de strings, limitando o início ou o fim
s = "um tigre, dois tigres, três tigres"
print(s.find("tigres"))
print(s.rfind("tigres"))
print(s.find("tigres", 7))  # Início 7
print(s.find("tigres", 30))  # Início 30
print(s.find("tigres", 0, 10))  # Início = 0, fim = 10

# Pesquisa de todas as ocorrências
s = "um tigre, dois tigres, três tigres"
p = 0
while(p > -1):
    p = s.find("tigre", p)
    if p >= 0:
        print("Posição: %d" % p)
        p += 1

# Pesquisa de strings, limitando o início ou o fim
s = "um tigre, dois tigres, três tigres"
print(s.find("tigres"))
print(s.rfind("tigres"))
print(s.find("tigres", 7))  # Início 7
print(s.find("tigres", 30))  # Início 30
print(s.find("tigres", 0, 10))  # Início = 0, fim = 10

# Pesquisa de todas as ocorrências
s = "um tigre, dois tigres, três tigres"
p = 0
while(p > -1):
    p = s.find("tigre", p)
    if p >= 0:
        print("Posição: %d" % p)
        p += 1

# Preenchimento de strings com espaços
s = "tigre"
print(s.ljust(20))
print(s.rjust(20))
print(s.ljust(20, "."))

# Separação de strings
s = "um tigre, dois tigres, três tigres"
print(s.split(","))
print(s.split(" "))
print(s.split())

# Substituição de strings
s = "um tigre, dois trigres, três tigres"
print(s.replace("tigre", "gato"))

# Quebra de strings de várias linhas
m = "Uma linha\noutralinha\ne mais uma\n"
print(m.splitlines())

# Remoção de espaços em branco com strip, lstrip e rstrip
t = "       Hi      "
print(t.strip())
print(t.rstrip())

# Validação de strings com números
print("771".isdigit())
print("10.4".isdigit())
print("+10".isdigit())
print("-5".isdigit())

# Validação de strings por seu conteúdo
s = "125"
p = "alô mundo"
print(s.isalnum())
print(p.isalnum())
print(s.isalpha())
print(p.isalpha())

# Diferenciação de isnumeric de isdit
umterço = "\u2153"
novetibetano="\u0f29"
print(umterço.isdigit())
print(umterço.isnumeric())
print(novetibetano.isdigit())
print(novetibetano.isnumeric())

# Verificação de maiúsculas e minúsculas
s = "ABC"
p = "abc"
e = "aBc"

print(s.isupper())
print(s.islower())
print(p.isupper())
print(p.islower())
print(p.islower())
print(e.isupper())
print(e.islower())

# Verificação se a string contém apenas caracteres de espaçamento
print("\t\n\r       ".isspace())
print("\tAlô".isspace())

# Formatação de strings com o método format
print("{0} {1}".format("Hello", "bithes"))
print("{0} x {1} R${2}".format(5, "maçã", "1.20"))

# verificação se a string pode ser impresa
print("\n\t".isprintable())
print("\nAlô".isprintable())
print("Alô mundo".isprintable())

# uso do parâmetro mais de uma vez
print("{0} {1} {0}".format("-","x"))

# Alteração da ordem de utilização dos parâmetros
print("{1} {0}".format("-", "x"))

# Limitação do tamanho de impressão dos parâmetros
print("{0:10} {1}".format("123", "456"))
print("X{0:10}X".format("123"))
print("X{0:10}X".format("12345678912345"))

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 