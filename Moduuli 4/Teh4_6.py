import random
N = int(input("Anna pisteiden määrä"))

n = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y > 1:
        n += 1

pi_arvio = 4 * n / N

print("piin arvio on:",pi_arvio)