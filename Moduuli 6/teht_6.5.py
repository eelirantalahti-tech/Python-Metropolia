luvut = [1,2,3,4,5,6,7,8,9,10]

def summa(luvut):
    vastaus = []
    for i in luvut:
        if i % 2 == 0:
            vastaus.append(i)
    return vastaus
parilista = summa(luvut)

print(parilista, luvut)

