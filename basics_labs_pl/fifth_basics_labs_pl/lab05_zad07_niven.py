# Sprawdzanie liczby Nivena (Harshada)

n = int(input("Podaj liczbę: "))
system = int(input("Podaj system liczbowy (np. 10): "))

cyfry = []
temp = n

while temp > 0:
    cyfry.append(temp % system)
    temp //= system

suma_cyfr = sum(cyfry)

if suma_cyfr != 0 and n % suma_cyfr == 0:
    print("Liczba Nivena")
else:
    print("To nie jest liczba Nivena")
# Ten program sprawdza, czy podana przez użytkownika liczba jest liczbą Nivena (Harshada) w określonym systemie liczbowym.
# Liczba Nivena to taka liczba, która jest podzielna przez sumę swoich cyfr w danym systemie liczbowym.
# Program najpierw rozbija liczbę na poszczególne cyfry w wybranym systemie, oblicza sumę tych cyfr, a następnie sprawdza podzielność oryginalnej liczby przez tę sumę.