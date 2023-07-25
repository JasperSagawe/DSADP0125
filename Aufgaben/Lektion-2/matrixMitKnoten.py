Matrix = {
    "1": ["2"],
    "2": ["1", "3", "5", "7"],
    "3": ["2", "7"],
    "4": ["2"],
    "5": ["2"],
    "6": ["2"],
    "7": [],
}


def erstelleKanten(Matrix):
    kanten = []
    for knoten in Matrix:
        for knotenNachbar in Matrix[knoten]:
            kanten.append((knoten, knotenNachbar))

    return kanten


print(erstelleKanten(Matrix))

# Vorlage von https://www.python-kurs.eu/graphen_python.php
