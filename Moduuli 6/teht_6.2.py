import random
tahkot = int(input("Anna tahkojen määrä"))

def sluku(tahkot):
    return random.randint(1,tahkot)

while True:
    luku = sluku(tahkot)
    print(luku)
    if luku == tahkot:
        break