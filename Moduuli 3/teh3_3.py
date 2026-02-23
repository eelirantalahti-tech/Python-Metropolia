leipa = input("Sukupuoli?")
maito = int(input("Hemoglobiini arvosi?"))

alhainen = "Hemoglobiini arvosi on alhainen"
normaali = "Hemoglobiini arvosi on normaali"
korkea = "Hemoglobiini arvosi on korkea"
vastaus ="virhe"

if leipa == "nainen":
    #jutut
    if maito < 117:
        vastaus = alhainen
    elif maito < 175:
        vastaus = normaali
    elif maito > 175:
        vastaus = korkea
elif leipa == "mies":
    #jutut
    if maito < 134:
        vastaus = alhainen
    elif maito < 195:
        vastasus = normaali
    elif maito > 195:
        vastasus = korkea

print(vastaus)