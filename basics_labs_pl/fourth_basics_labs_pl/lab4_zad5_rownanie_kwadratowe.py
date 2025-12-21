# Zadanie 5 – równanie kwadratowe

import math

def solve(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return "Brak rozwiązań"
    elif delta == 0:
        x = -b / (2*a)
        return f"Jedno rozwiązanie: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Dwa rozwiązania: x1 = {x1}, x2 = {x2}"

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

print(solve(a, b, c))
# Ten program rozwiązuje równanie kwadratowe postaci ax^2 + bx + c = 0.
# Definiuje funkcję 'solve', która przyjmuje współczynniki a, b i c jako argumenty i zwraca rozwiązania równania w zależności od wartości delty.
# Następnie pobiera współczynniki od użytkownika i wyświetla wynik.