import math

def pizza(halkaisija ,hinta):
    r = halkaisija / 200
    a = math.pi * r * r
    vastike = hinta / a
    return vastike

halkasija = int(input("Anna ensimmäisen pizzan halkasija"))
hinta = int(input("Anna ensimmäisen pizzan hinta"))

halkasija_2 = int(input("Anna toisen pizzan halkasija"))
hinta_2 = int(input("Anna toisen pizzan hinta"))



p1 = pizza(halkasija,hinta)
p2 = pizza(halkasija_2,hinta_2)

if p1 > p2:
    print(p2, "pizza kaksi on parempi!")
elif p2 == p1:
    print ("molemmat pizzat ovat yhtä hyviä.")
else:
    print(p1, "pizza yksi on parempi!")

