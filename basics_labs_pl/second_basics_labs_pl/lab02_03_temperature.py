# Zadanie 3 – konwersja temperatury

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

fahrenheit = float(input("Podaj temperaturę w stopniach F: "))
celsius = fahrenheit_to_celsius(fahrenheit)

print("Temperatura w Celsjuszach:", celsius)
# Ten program konwertuje temperaturę podaną w stopniach Fahrenheita na stopnie Celsjusza.
# Definiuje funkcję 'fahrenheit_to_celsius', która wykonuje konwersję,
# a następnie pobiera wartość od użytkownika, dokonuje konwersji i wyświetla wynik.