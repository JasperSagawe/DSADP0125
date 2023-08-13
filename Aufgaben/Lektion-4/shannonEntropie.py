import math

alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

buchstabenWert = {buchstabe: nummer // 2 for nummer, buchstabe in enumerate(alphabet)}


def stringZuWert(string):
    wert = 0
    for i in string:
        if i in buchstabenWert:
            wert += buchstabenWert[i]
    return wert


textstring = "Eine alte Dame geht heute einkaufen."

wert = stringZuWert(textstring)

haeufigkeiten = {}
for buchstabe in textstring:
    if buchstabe != "." and buchstabe != " ":
        if buchstabe in haeufigkeiten:
            haeufigkeiten[buchstabe] += 1
        else:
            haeufigkeiten[buchstabe] = 1

stringLaenge = len(textstring)
wahrscheinlichkeiten = {
    buchstabe: haeufigkeiten / stringLaenge
    for buchstabe, haeufigkeiten in haeufigkeiten.items()
}

shannonEntropie = -sum(pi * (math.log2(pi)) for pi in wahrscheinlichkeiten.values())

print(shannonEntropie)
