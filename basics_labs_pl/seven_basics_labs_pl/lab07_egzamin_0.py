def pobierz_punkty_studentow():
    punkty_studentow = []
    while True:
        try:
            liczba_studentow_str = input("Podaj liczbę studentów: ")
            liczba_studentow = int(liczba_studentow_str)
            if liczba_studentow <= 0:
                continue
            break
        except ValueError:
            print("Nieprawidłowe dane.")

    print("\nPodaj punkty dla każdego studenta: (0-100)")
    for i in range(liczba_studentow):
        while True:
            try:
                punkt_str = input(f"Student {i + 1}: ")
                punkt = int(punkt_str)
                if 0 <= punkt <= 100:
                    punkty_studentow.append(punkt)
                    break
                else: print("Podaj poprawne dane")
            except ValueError:
                print("Nieprawidłowe dane.")

    return punkty_studentow


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
    if lista_punktow:
        najwyzszy_wynik = max(lista_punktow)
        najnizszy_wynik = min(lista_punktow)
        liczba_zaliczonych = 0
        for p in lista_punktow:
            if p >= 50:
                liczba_zaliczonych += 1

        print(f"Najwyższy wynik: {najwyzszy_wynik}")
        print(f"Najniższy wynik: {najnizszy_wynik}")
        print(f"Liczba studentów, którzy zaliczyli (min. 50 pkt): {liczba_zaliczonych}")
    else:
        print("Brak danych do obliczeń (0 studentów).")
# Główna część programu
if __name__ == "__main__":
    punkty = pobierz_punkty_studentow()
    wyswietl_wyniki(punkty)
    wyswietl_wyniki_zadanie_2(punkty)