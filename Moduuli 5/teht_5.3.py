luku = int(input("Anna kokonaisluku!"))
vastaus = "On alkuluku"
for i in range( 2, luku ):
    if luku % i == 0:
        vastaus = "Ei ole alkuluku"
        break

print(luku,vastaus)