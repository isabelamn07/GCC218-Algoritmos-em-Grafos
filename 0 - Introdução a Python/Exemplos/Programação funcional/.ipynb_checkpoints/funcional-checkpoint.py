def pot2(x):
    return x ** 2
pot2_ = lambda x: x **2

print(pot2(5))
print(pot2_(10))

def fat(n):
    if(n == 0):
        return 1
    else:
        return (n* fat(n -1))

print(fat(5))

fat_ = lambda n: n * fat_(n -1) if n > 1 else 1
print(fat_(4))

# map

lista = [1, 2, 3]
m = map(lambda x: x **2, lista)
for i in m:
    print(i)

# reduce 

import functools

print(functools.reduce(lambda x,y: x + y, [1,2,3,4]))

f = filter(lambda x: x%2 == 0, range(10))
for i in f:
    print(i)

#fibonacci 
def fib(n):
    if (n ==1 or n == 2):
        return 1
    return fib(n -1) + fib(n - 2)
print("Fibonacci de 6 = ", fib(6))

# Functional programming

def apply_twice(func, arg):
    return func(func(arg))
def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 