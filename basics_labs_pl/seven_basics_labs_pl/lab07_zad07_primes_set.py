def liczby_pierwsze(n):
    liczby = set(range(2, n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if i in liczby:
            liczby -= set(range(i * i, n + 1, i))
    return liczby

print(liczby_pierwsze(50))
# Ten program definiuje funkcję 'liczby_pierwsze', która znajduje wszystkie liczby pierwsze mniejsze lub równe podanej liczbie n.
# Używa algorytmu Sita Eratostenesa, aby efektywnie wyeliminować liczby złożone z zestawu liczb od 2 do n, pozostawiając tylko liczby pierwsze.