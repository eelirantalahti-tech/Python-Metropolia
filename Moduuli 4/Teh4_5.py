yritykset = 0
while yritykset < 5:
    tunnus = input("anna käyttäjätunnus")
    salasana = input("anna salasana")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    else:
        yritykset += 1

if yritykset == 5:
    print("pääsy evätty")