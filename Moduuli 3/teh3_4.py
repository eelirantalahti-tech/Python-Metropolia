vuosi = int(input("Mikä vuosi on?"))
vastaus = "vuosi ei ole karkausvuosi"
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        vastaus = "vuosi on karkausvuosi"

elif vuosi % 4 == 0:
   vastaus = "vuosi on karkausvuosi"

print(vastaus)