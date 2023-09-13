alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

buchstabenWert = {buchstabe: nummer // 2 for nummer, buchstabe in enumerate(alphabet)}


def stringZuWert(string):
    wert = 0
    for i in string:
        if i in buchstabenWert:
            wert += buchstabenWert[i]
    return wert


textstring = "PythonP"
quersumme = stringZuWert(textstring)

print(f"Die Quersumme vom String \"{textstring}\" beträgt {quersumme}")
