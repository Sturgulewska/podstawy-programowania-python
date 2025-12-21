przedrostki = {
    "kilo": "10^3",
    "mega": "10^6",
    "giga": "10^9"
}

def wyswietl():
    for k, v in przedrostki.items():
        print(k, "=", v)

def dodaj_lub_edytuj(nazwa, wartosc):
    przedrostki[nazwa] = wartosc

wyswietl()
dodaj_lub_edytuj("mili", "10^-3")
wyswietl()
# Ten program definiuje słownik 'przedrostki', który mapuje nazwy przedrostków na ich wartości potęgowe.
# Zawiera funkcję 'wyswietl', która wyświetla wszystkie przedrostki i ich wartości,
# oraz funkcję 'dodaj_lub_edytuj', która pozwala na dodanie nowego przedrostka lub edycję istniejącego.