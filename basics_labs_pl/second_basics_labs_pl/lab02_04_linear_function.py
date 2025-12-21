# Zadanie 4 – funkcja liniowa

def linear_function(a, b, x):
    return a * x + b

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
x = float(input("Podaj x: "))

result = linear_function(a, b, x)
print("Wynik f(x):", result)
# Ten program definiuje funkcję liniową f(x) = a*x + b.
# Pobiera od użytkownika wartości a, b oraz x, a następnie oblicza i wyświetla wynik funkcji dla podanych wartości.