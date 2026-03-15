import random
lukumäärä = int(input("Anna arpakuutioiden lukumäärä"))
summa = 0

for i in range( lukumäärä ):
    randomnumber = random.randint(1,6)
    summa += randomnumber
    print(randomnumber)

print("Kuutioiden summa on",summa)