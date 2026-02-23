pituus = float (input("Mikä on kuhan pituus?" ) )
minimi= 37.0

print("Kuhan pituus on",pituus,"minimi on",minimi)
if pituus < minimi:
    Erotus = (pituus-minimi)
    print("Kuha pitää laskea veteen, koska se on",Erotus ,"cm alle minimi pituuden" )