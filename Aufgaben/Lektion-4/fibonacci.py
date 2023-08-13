def fibonacci(n):
    a = 0
    b = 1
    c = 0

    if n < 1:
        c = a
    elif n == 2:
        c = b
    else:
        for _ in range(n - 2):
            c = a + b
            a = b
            b = c
    return c


def naechstePrimzahl(nummer):
    if nummer < 1:
        return False
    elif nummer > 1:
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
