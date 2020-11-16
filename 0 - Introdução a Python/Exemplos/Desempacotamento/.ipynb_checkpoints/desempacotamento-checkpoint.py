lista = [1, 2, 3]

a, b, c = lista

print(a)
print(b)
print(c)

def func (x, y):
    return x ** 2, y ** 2

print(func(4,6))

r1, r2 = func(2, 3)
print(r1)
print(r2)

def drop_first_last(grades):
    first, *middle, last = grades
    return middle


lista2 = [1, 2, 3, 5, 7, 9, 1]
print(drop_first_last(lista2))

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 