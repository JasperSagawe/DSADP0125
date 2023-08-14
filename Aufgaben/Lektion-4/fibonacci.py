def fibonacci(n):
    if n <= 1:
        c = n

    else:
        a = 0
        b = 1
        for _ in range(n - 1):
            c = a + b
            a = b
            b = c
    return c


def naechstePrimzahl(nummer):
    # Für jede Zahl kleiner als 2, ist die nächste Primzahl 2, da 2 die erste Primzahl ist.
    if nummer <= 2:
        return 2
    elif nummer > 2:
        for i in range(2, int(nummer / 2) + 1):
            if (nummer % i) == 0:
                return naechstePrimzahl(nummer + 1)
        else:
            return nummer


# die n-te Fibonacci-Zahl wird gesucht
n = 25
nFibonacci = fibonacci(n)
fibonacciPrimzahl = naechstePrimzahl(nFibonacci)


print(f"Die {n}. Fibonacci-Zahl lautet {nFibonacci}.")
print(f"Die erste Primzahl danach ist {fibonacciPrimzahl}.")
