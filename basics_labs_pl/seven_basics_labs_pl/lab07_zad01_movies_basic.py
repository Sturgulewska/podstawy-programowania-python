# ============================================
# Laboratorium – słowniki (filmy)
# ============================================

# Dane pojedynczych filmów
film1 = {
    "rok": 1999,
    "rezyser": "Lana i Lilly Wachowski",
    "ocena": 8.7
}

film2 = {
    "rok": 2010,
    "rezyser": "Christopher Nolan",
    "ocena": 8.8
}

film3 = {
    "rok": 1994,
    "rezyser": "Frank Darabont",
    "ocena": 9.3
}

# Lista filmów (tytuł + słownik z danymi)
filmy_lista = [
    ("Matrix", film1),
    ("Incepcja", film2),
    ("Skazani na Shawshank", film3)
]

# Funkcja tworząca jeden zbiorczy słownik filmów
def utworz_slownik_filmow(filmy_dane):
    filmy = {}

    for tytul, dane in filmy_dane:
        filmy[tytul] = dane

    return filmy

# Utworzenie słownika filmów
filmy = utworz_slownik_filmow(filmy_lista)

# Wyświetlenie wszystkich filmów
print("Zestawienie filmów:")

for tytul, dane in filmy.items():
    print(f"\nTytuł: {tytul}")
    for klucz, wartosc in dane.items():
        print(f"  {klucz}: {wartosc}")
