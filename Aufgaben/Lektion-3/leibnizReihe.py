def piBerechnen(anzahl):
    pi = 0
    # In der Leibniz-Reihe rechnet man pi/4 = 1 - 1/3 + 1/5 - 1/7...
    # Dadurch muss das vorzeichen nach jeder generierten Zahl umgedreht werden.
    vorzeichenUmdrehen = 1

    # Hier wird die Zahl unterm Bruchstrich, basierend auf die Leibniz-Reihe in Zweierschritten generiert.
    for i in range(1, anzahl * 2, 2):
        pi += vorzeichenUmdrehen * (1 / i)
        vorzeichenUmdrehen *= -1

    pi *= 4
    return pi


# Je mehr Brüche in der Leibniz-Reihe, desto nöher kommt man an Pi.
anzahlBrueche = 10000
pi = piBerechnen(anzahlBrueche)

print(f"Annäherung an Pi: {pi:.10f}")
