# Pure and impure function

# Pure function
def pure_function(x,y):
    temp = x + 2 * y
    return temp/(2 * x + y)

print(pure_function(13, 2))

# Impure function
some_list = []
def impure(arg):
    some_list.append(arg)

impure(5)
impure(4)
print(some_list)

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 