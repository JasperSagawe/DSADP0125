import random
import math

Matrix = {}


# Knoten ohne Verbindungen von 1 bis kn werden erstellt.
def erstelleKnoten(kn):
    for i in range(1, kn + 1):
        Matrix[str(i)] = []
    return Matrix


# Jedem Knoten werden zufällige Knoten-Nachbarn zugeschrieben.
def erstelleNachbarn():
    for knoten in Matrix:
        # Jeder Knoten hat mindestens 3 Nachbarknoten, aber maximal 5.
        anzahlNachbarn = random.randint(3, 5)

        # Ausschließen des aktuellen Knotens von den potenziellen Nachbarn.
        moeglicheNachbarn = [
            ausgewaehlterKnoten
            for ausgewaehlterKnoten in Matrix.keys()
            if ausgewaehlterKnoten != knoten
        ]

        # Zufällige Auswahl von Nachbarn aus den potenziellen Nachbarn.S
        nachbarn = random.sample(moeglicheNachbarn, anzahlNachbarn)
        Matrix[knoten] = nachbarn
    return Matrix


# Für alle benachbarten Knoten werden Kanten erstellt und zufällige Werte zugewiesen.
def erstelleKanten(Matrix):
    kanten = []
    for knoten in Matrix:
        for knotenNachbar in Matrix[knoten]:
            # Weißt der Kante einen zufälligen Wert zu.
            wert = int(random.gauss(50, math.sqrt(50)))
            kanten.append((knoten, knotenNachbar, wert))
    return kanten


erstellteKnoten = erstelleKnoten(35)
erstellteNachbarn = erstelleNachbarn()
erstellteKanten = erstelleKanten(Matrix)

# Aus allen Kanten werden 100 zufällig ausgewählt.
zufaelligeKanten = random.sample(erstellteKanten, 100)


# Finde die Kante mit dem kleinsten Wert für den gegebenen Knoten.
# Um den Graphen ungerichtet zu machen, überprüft er alle Kanten,
# an denen der Knoten an erster oder zweite Stelle steht.
def findeKanteMitKleinstenWert(knoten):
    kantenVonKnoten = []
    for kante in zufaelligeKanten:
        if kante[0] == knoten or kante[1] == knoten:
            kantenVonKnoten.append(kante)
    if not kantenVonKnoten:
        return None
    return min(kantenVonKnoten, key=lambda wert: wert[2])


anzahlSchritte = 50

# Wähle einen den Start-Knoten aus.
ausgewählterKnoten = "1"

gesamtWertSchritte = 0

for i in range(anzahlSchritte):
    if ausgewählterKnoten is not None:
        # Finde die Kante mit dem kleinsten Wert für den ausgewählten Knoten.
        kanteMitKleinstenWert = findeKanteMitKleinstenWert(ausgewählterKnoten)
        if kanteMitKleinstenWert is not None:
            print("Zurzeit ausgewählter Knoten:", ausgewählterKnoten)
            print("Kante mit dem kleinsten Wert:", kanteMitKleinstenWert)

            gesamtWertSchritte += kanteMitKleinstenWert[2]

            # Wenn die Kante mit den kleinsten Wert den startKnoten an erster Stelle hat,
            # dann ist der neue Startknoten, der Knoten an zweiter Stelle der Kante.
            # Ansonsten wird der erste Knoten als startKnoten gesetzt.
            if kanteMitKleinstenWert[0] == ausgewählterKnoten:
                ausgewählterKnoten = kanteMitKleinstenWert[1]
            else:
                ausgewählterKnoten = kanteMitKleinstenWert[0]
        else:
            # Tritt nur auf, sofern die zufällig ausgewählten Kanten den Startknoten 1 nicht beinhalten.
            # Die Chance ist sehr gering, aber möglich.
            print("Keine Kanten sind für diesen Knoten verfügbar.")
            break

print("Kumulativer Wert während des Pfades:", gesamtWertSchritte)
