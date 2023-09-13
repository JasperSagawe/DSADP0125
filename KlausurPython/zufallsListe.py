import random


def erstelleListe(n):
    liste = []
    for i in range(1, n + 1):
        liste.append(random.randint(0, 26))
    return liste

anzahlZahlen = 5
print("Zufällige Liste:", erstelleListe(anzahlZahlen))


