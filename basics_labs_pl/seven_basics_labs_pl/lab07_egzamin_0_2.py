def pobierz_punkty_():
    punkty = []
    while True:
        try:
            liczba_str = input("Wprowadz ile chcesz liczb: ")
            liczba = int(liczba_str)
            if liczba <= 0:
                continue
            break
        except ValueError:
            print("Nieprawidłowe dane.")

    for i in range(liczba):
        while True:
            try:
                punkt_str = input(f"Student {i + 1}: ")
                punkt = int(punkt_str)
                if 0 <= punkt <= 100:
                    punkty.append(punkt)
                    break
                else:
                    print("Podaj poprawne dane")
            except ValueError:
                print("Nieprawidłowe dane.")

    return punkty


def wyswietl_wyniki(lista_punktow):
    if not lista_punktow:
        print("Nie podano zadnych danych")
        return

    print("\n--- Wyniki ---")
    print(f"Lista punktów: {lista_punktow}")

    suma_punktow = 0
    for punkt in lista_punktow:
        suma_punktow += punkt

    srednia_punktow = suma_punktow / len(lista_punktow)
    print(f"Średnia liczba punktów: {srednia_punktow:.2f}")


def wyswietl_wyniki_zadanie_2(lista_punktow):
    if(lista_punktow):
        najwyzszy_wynik = max(lista_punktow)
        najnizszy_wynik = min(lista_punktow)
        dodatnie = 0
        ujemne = 0
        zero = 0
    for p in lista_punktow:
        if p > 0:
            dodatnie += 1

        elif p < 0:
            ujemne += 1
    else:
        zero += 1


    print(f"Najwyższy wynik: {najwyzszy_wynik}")
    print(f"Najniższy wynik: {najnizszy_wynik}")
    print(f"ilosc liczb: {lista_punktow}")


# Główna część programu
if __name__ == "__main__":
    punkty = pobierz_punkty_()
    wyswietl_wyniki(punkty)
    wyswietl_wyniki_zadanie_2(punkty)
