# ============================================
# Laboratorium –
####################################################


nazwa = input("Podaj nazwę pliku:")
liczba_1 = int(input("Podaj pierwszą liczbę: "))

liczba_2 = int(input("Podaj drugą liczbę: "))

liczba_3 = int(input("Podaj trzecią liczbę: "))

plik = open(nazwa, "w")

# def sum(liczba_1, liczba_2, liczba_3):
if liczba_1 > 0 and liczba_2 > 0 and liczba_3 > 0:
    sum = liczba_1 + liczba_2 + liczba_3

plik.write(str(sum))
plik.write('\n')
plik.close()

plik = open(nazwa, "r")

updata = plik.read()
plik.close()

print(f"Zawartosc pliku: " , {nazwa} , "zostanie wyswietlona")
print(updata)
