# Zadanie 6 – rok przestępny

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

year = int(input("Podaj rok: "))

if is_leap_year(year):
    print("Rok przestępny")
else:
    print("Rok nieprzestępny")
# Ten program sprawdza, czy podany rok jest rokiem przestępnym.
# Definiuje funkcję 'is_leap_year', która przyjmuje rok jako argument i zwraca wartość logiczną wskazującą, czy rok jest przestępny.
# Następnie pobiera rok od użytkownika i wyświetla odpowiedni komunikat.