# Średni dzienny opad

suma = 0
licznik = 0

while True:
    opad = float(input("Podaj dzienny opad (liczba ujemna kończy): "))
    if opad < 0:
        break
    suma += opad
    licznik += 1

if licznik > 0:
    print("Średni opad:", suma / licznik)
else:
    print("Brak danych")
# Ten program oblicza średni dzienny opad na podstawie danych wprowadzonych przez użytkownika.
# Użytkownik wprowadza wartości opadów dla kolejnych dni, a wprowadzenie liczby ujemnej kończy zbieranie danych.
# Program następnie oblicza i wyświetla średni opad, jeśli wprowadzono jakiekolwiek dane.