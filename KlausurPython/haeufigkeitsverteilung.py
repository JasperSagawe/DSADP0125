def sucheBuchstabenHaeufigkeit(string, suche):
    buchstabenHaeufigkeit = 0

    for buchstabe in string:
        if buchstabe == suche:
            buchstabenHaeufigkeit += 1

    return buchstabenHaeufigkeit


string = "Python ist eine moderne Programmiersprache."
buchstabe = "P"
# String und Buchstabe in lowercase, damit er sowohl nach Groß- als auch Kleinschreibung sucht.
buchstabenHaeufigkeit = sucheBuchstabenHaeufigkeit(string.lower(), buchstabe.lower())

print(f'Der Buchstabe "{buchstabe}" ist {buchstabenHaeufigkeit} mal im String "{string}"')
