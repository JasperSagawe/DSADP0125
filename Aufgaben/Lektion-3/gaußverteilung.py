import random
import statistics

# Bestimmt den Umfang der Gaußverteilungen
zahlenProListe = 5
anzahlListen = 1000
mittelwert = 5
standardabweichung = 3

listenArray = [
    [random.gauss(mittelwert, standardabweichung) for _ in range(zahlenProListe)]
    for _ in range(anzahlListen)
]

summeDerListenArray = [sum(liste) for liste in listenArray]

mittelwertSummen = sum(summeDerListenArray) / anzahlListen

standardabweichungSummen = statistics.stdev(summeDerListenArray)

print("Mittelwert der Summen:", mittelwertSummen)
print("Standardabweichung der Summen:", standardabweichungSummen)
