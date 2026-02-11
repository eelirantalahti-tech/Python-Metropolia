Leiviska = float(input("Anna leiviskät:"))
Naula =float(input("Anna Naulat:"))
Luoti  =float(input("Anna luodit:"))

Luoti_grammoina =  Luoti * 13.3
Naula_grammoina = 32 * Luoti * Naula
Leiviska_grammoina = Leiviska * 20 * 32

kokonais_grammat = Luoti_grammoina + Naula_grammoina + Leiviska_grammoina
kilot = kokonais_grammat//1000
grammat = kokonais_grammat%1000
print(f"kilot: {kilot:.2f}, grammat: {grammat:.2f}")

