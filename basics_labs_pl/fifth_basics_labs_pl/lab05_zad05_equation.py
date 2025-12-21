# Sprawdzanie rozwiązania równania x^2 - 2 = 0

while True:
    x = float(input("Podaj liczbę: "))
    if abs(x**2 - 2) <= 1e-4:
        print("Podana liczba spełnia równanie")
        break
    else:
        print("Nie spełnia równania, spróbuj ponownie")
# Ten program sprawdza, czy podana przez użytkownika liczba spełnia równanie x^2 - 2 = 0 z dokładnością do 0.0001.
# Używa pętli while, aby wielokrotnie prosić użytkownika o podanie liczby, aż do momentu, gdy wprowadzi liczbę spełniającą równanie.