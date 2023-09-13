import random


def erstelleListe(n):
    liste = []
    for i in range(1, n + 1):
        liste.append(random.randint(0, 26))
    return liste


anzahlZahlen = 5
# Ich habe hier die Liste noch in eine Variable getan, um sie beim Sortieren zu nutzen.
zufallsListe = erstelleListe(anzahlZahlen)
print("Zufällige Liste unsortiert: ", zufallsListe)


def listeSortieren(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            print(zufallsListe)

            if array[j] > array[j + 1]:
                temp = array[j]

                array[j] = array[j + 1]
                array[j + 1] = temp


listeSortieren(zufallsListe)
print("Zufällige Liste sortiert: ", zufallsListe)
