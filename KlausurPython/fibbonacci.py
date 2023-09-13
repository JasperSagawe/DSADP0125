def fibonacciBerechnen(n):
    if n <= 1:
        c = n

    else:
        a = 0
        b = 1
        for _ in range(1, n):
            c = a + b
            a = b
            b = c
    return c


nFibonacci = 115
fibonacci = fibonacciBerechnen(nFibonacci)
print(f"Die {nFibonacci}. Fibonacci Zahl betragt: {fibonacci}")


