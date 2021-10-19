# https://docs.python.org/3/library/random.html
import random

i = random.randint(23, 42)

films = ["Die Hard", "Back to the Future", "Interstellar", "Cinema Paradiso"]

film = random.choice(films)

print(i)
print(film)


height = random.uniform(103, 219)
print(height)
