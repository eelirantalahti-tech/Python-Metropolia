import random
a = 1
b = 10

oikea_luku = random.randint(a, b)
arvaus = int(input("Anna arvaus"))

while arvaus != oikea_luku:
    if arvaus < oikea_luku:
        print(" arvaus liian pieni")
    elif arvaus > oikea_luku:
        print(" arvaus liian suuri")
    arvaus = int(input("Anna uusi arvaus"))
print(oikea_luku,"on oikea arvaus!")