# random
import random

# random - escolhe um número aleatório entre 0 e 1
value = random.random()
print(value)

# uniform
value = random.uniform(1, 10)
print(value)

greetings = ['Hello', 'darkness', 'my', 'old', 'friend']

value = random.choice(greetings)
print(value + ', Josefa!')

value = random.randint(1, 6)
print(value)

cores = ['Vermelho', 'Azul', 'Verde']
resultados = random.choices(cores, k=11)
print(resultados)

another_colors = ['Yellow', 'Orange', 'Pink']
results_colors = random.choices(another_colors, weights=[19, 19, 6], k=12)
print(results_colors)

deck = list(range(1, 53))
random.shuffle(deck)

hand = random.sample(deck, k=5)
print(deck)
print(hand)

print(random.randrange(4))
