# Sprawdzanie liczby Armstronga

n = int(input("Podaj liczbę: "))
cyfry = [int(c) for c in str(n)]
k = len(cyfry)

suma = 0
for c in cyfry:
    suma += c ** k

if suma == n:
    print("Liczba Armstronga")
else:
    print("To nie jest liczba Armstronga")
# Ten program sprawdza, czy podana przez użytkownika liczba jest liczbą Armstronga.
# Liczba Armstronga to taka liczba, która jest równa sumie swoich cyfr podniesionych do potęgi równej liczbie cyfr w tej liczbie.
# Program najpierw rozbija liczbę na poszczególne cyfry, a następnie oblicza sumę tych cyfr podniesionych do odpowiedniej potęgi i porównuje ją z oryginalną liczbą.