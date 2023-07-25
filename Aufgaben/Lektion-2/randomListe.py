import random


def erstelleListe(n):
    liste = []
    for i in range(1, n + 1):
        liste.append(random.randint(0, 100))
    return liste


print("Zufällige Liste:", erstelleListe(25))
