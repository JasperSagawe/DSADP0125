import random

liste = []

# Fülle die Liste mit n-Werte.
def erstelleListe(n):
    for i in range(1, n+1): 
        liste.append(random.randint(1, 1000))
    return liste

# Verschiebung um n-stellen nach rechts.
def schieberegisterRechts(n):
    for i in range(1, n+1): 
        liste.pop()
        liste.insert(0, random.randint(1, 1000))
    return liste

# Verschiebung um n-stellen nach links.
def schieberegisterLinks(n):
    for i in range(1, n+1): 
        liste.pop(0)
        liste.append(random.randint(1, 1000))
    return liste


print("\nListe nach dem Erstellen:", erstelleListe(50))
print("\nListe nach links verschoben:", schieberegisterLinks(25))
print("\nListe nach rechts verschoben:", schieberegisterRechts(25))
