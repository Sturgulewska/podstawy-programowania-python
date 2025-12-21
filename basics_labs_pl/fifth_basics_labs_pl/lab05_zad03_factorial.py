# Obliczanie silni

n = int(input("Podaj dodatnią liczbę całkowitą: "))
silnia = 1

for i in range(1, n + 1):
    silnia *= i

print(f"{n}! = {silnia}")
# Ten program oblicza silnię podanej przez użytkownika dodatniej liczby całkowitej n.
# Używa pętli for do mnożenia kolejnych liczb od 1 do n i wyświetla wynik w formacie "n! = silnia".