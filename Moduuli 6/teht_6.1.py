import random
def sluku():
    return random.randint(1,6)

while True:
    luku = sluku()
    print(luku)
    if luku == 6:
        break