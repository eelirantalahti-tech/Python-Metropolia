lentoasemat = {}

while True:
    toiminto = input("valitse toiminto (uusi, hae, lopeta): ")

    if toiminto == "lopeta":
        break

    if toiminto == "uusi":
        koodi = input("anna ICAO-koodi: ")
        nimi = input("anna lentoaseman nimi: ")
        lentoasemat[koodi] = nimi

    if toiminto == "hae":
        koodi = input("anna ICAO-koodi: ")
        print(lentoasemat[koodi])