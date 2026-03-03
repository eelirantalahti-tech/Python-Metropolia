eka = True
s = input("ensimmäinen numero")
while s != "":
    luku = int(s)

    if eka:
        pienin = luku
        suurin = luku
        eka = False
    else:
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku
    s = input(" anna uusi numero")
if eka:
    print("ei annttu lukuja")
else:
    print(pienin, "on pienin numero")
    print(suurin, "on suurin numero")

