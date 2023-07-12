# Überprüft ob die Zahl eine Primzahl ist.
def istPrimzahl(nummer):
# Überorüft ob die Zahl größer als Eins ist. jede kleinere ist keine Primzahl.
    if nummer > 1:
    # Führt eine Schleife von 2 bis nummer/2 aus.
        for i in range(2, int(nummer/2)+1):
        # Wenn die Zahl durch 2 oder nummer/2 ohne Rest teilbar ist, dann ist sie keine Primzahl.
            if (nummer % i) == 0:
                return False
        else:
            return True


# Zählt die nte Primzahl
def zaehlePrimzahl(n):
    anzahlPrimzahlen = 0
# Beginnt bei 1 mit der Funktion, zum Überprüfen ob die Zahl eine Primzahl ist (Startet basierend der Aufgabenstellung bei 1, obwohl 1 keine Primzahl ist).
    nummer = 1
    while anzahlPrimzahlen < n:
# Wenn es eine Primzahl ist, dann wird die Anzahl der Primzahlen um 1 erhöht.
        if istPrimzahl(nummer):
            anzahlPrimzahlen += 1
# Sollte danach die Anzahl der Primzahlen mit der Parameter-Zahl übereinstimmen, wird die letzte erhaltene Nummer als n ausgegeben.
        if anzahlPrimzahlen == n:
            return nummer
# Sollten nicht beide der zwei vorigen ausgeführt werden, wird die Nummer um 1 erhöht und die Schleife wiederholt, bis n = anzahlPrimzahlen ist.
        nummer += 1


# Gibt die 1000. Primzahl im Log aus.
print(zaehlePrimzahl(1000))
