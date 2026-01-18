# ============================================
# Laboratorium –
####################################################

nazwa = input("Podaj nazwę pliku:")
n = int(input("Podaj liczbę n: "))

plik = open(nazwa, "w")

for i in range(n):
    ocena = int(input(f"Podaj ocene nr {i + 1}: "))

    plik.write(f'{ocena}\n')

plik.close()

plik = open(nazwa, "r")

updata = plik.read()
plik.close()

print(f"Zawartosc pliku: ", {nazwa}, "zostanie wyswietlona")
print(updata)
