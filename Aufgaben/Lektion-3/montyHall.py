import random


def montyHall(anzahl):
    gewinnBleiben = 0
    gewinnWechsel = 0

    for _ in range(anzahl):
        tueren = [1, 2, 3]

        preisTuer = random.choice(tueren)
        ausgewaehlteTuer = random.choice(tueren)

        tueren.remove(preisTuer)
        if ausgewaehlteTuer != preisTuer:
            tueren.remove(ausgewaehlteTuer)

        geoeffneteTuer = random.choice(tueren)

        tueren = [1, 2, 3]
        tueren.remove(geoeffneteTuer)

        if ausgewaehlteTuer == preisTuer:
            gewinnBleiben += 1
        if ausgewaehlteTuer != preisTuer:
            gewinnWechsel += 1

    gewinnchanceBleiben = (gewinnBleiben / anzahl) * 100
    gewinnchanceWechsel = (gewinnWechsel / anzahl) * 100

    print(f"Gewinnchance beim Bleiben: {gewinnchanceBleiben:.2f}%")
    print(f"Gewinnchance beim Wechsel: {gewinnchanceWechsel:.2f}%")


nummerDurchlaufe = 10000
montyHall(nummerDurchlaufe)
