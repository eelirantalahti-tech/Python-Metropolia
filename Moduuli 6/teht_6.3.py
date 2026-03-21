def litra(määrä):
    vastaus = määrä * 3.785
    return vastaus

while True:
    määrä = int(input("Anna gallonoiden määrä"))
    if määrä < 0:
        break
    print(litra(määrä))
