dzielniki = {}

for i in range(1, 101):
    lista = []
    for j in range(1, i + 1):
        if i % j == 0:
            lista.append(j)
    dzielniki[i] = lista

print(dzielniki)
# Ten program tworzy słownik, w którym kluczami są liczby od 1 do 100, a wartościami są listy ich dzielników.
# Używa zagnieżdżonych pętli for do znalezienia dzielników każdej liczby i wyświetla końcowy słownik.