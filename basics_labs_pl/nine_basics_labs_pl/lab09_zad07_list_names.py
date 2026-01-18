# ============================================
# Laboratorium –
####################################################

nazwa = input("Podaj nazwę pliku:")
zawartosc = input(":")

def sort_of():
    zawartosc = []
    while True:
        try:
            if zawartosc <= 0:
                continue
            break
        except ValueError:
            print("Nieprawidłowe dane.")

    print("")
    for i in range(liczba):
        while True:
            try:
                punkt_str = input(f"Student {i + 1}: ")
                punkt = int(punkt_str)
                if 0 <= punkt <= 100:
                    punkty_studentow.append(punkt)
                    break
                else:
                    print("Podaj poprawne dane")
            except ValueError:
                print("Nieprawidłowe dane.")

    return punkty_studentow


plik = open(nazwa, "w")
update = plik.read()
plik.close()
plik = open(nazwa, "r")
updata = plik.read(pobierz_punkty_studentow)
plik.close()

print(f"Zawartosc pliku: ", {nazwa}, "zostanie wyswietlona")
print(updata)
