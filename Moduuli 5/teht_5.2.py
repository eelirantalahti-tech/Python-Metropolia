from operator import truediv
from tokenize import TokenInfo
luvut = []

while True:
    luku = input("Anna luku")
    if luku == "":
        break
    luvut.append(int(luku))

luvut.sort(reverse=True)

print(luvut[:5])

