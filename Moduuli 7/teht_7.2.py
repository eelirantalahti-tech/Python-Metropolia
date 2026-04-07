nimet = set()

nimi = input("anna nimi: ")

while nimi != "":
    if nimi in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)

    nimi = input("anna seuraava nimi: ")

for nimi in nimet:
    print(nimi)