# Zadanie 5 – funkcja kwadratowa

def quadratic_function(a, b, c, x):
    return a * x**2 + b * x + c

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
x = float(input("Podaj x: "))

print("Wynik f(x):", quadratic_function(a, b, c, x))
# Ten program definiuje funkcję kwadratową f(x) = a*x^2 + b*x + c.
# Pobiera od użytkownika wartości a, b, c oraz x, a następnie oblicza i wyświetla wynik funkcji dla podanych wartości.