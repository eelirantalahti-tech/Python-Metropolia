kanta_str = input("Anna kanta: ")
korkeus_str = input("Anna korkeus: ")

kanta = float (kanta_str)
korkeus = float (korkeus_str)

pintaala = (kanta * korkeus)
piiri = (2*kanta + 2*korkeus)

print("Pinta-ala ja piiri ovat: "+ str(pintaala) + " ja " + str(piiri))
