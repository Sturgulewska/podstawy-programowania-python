filmy = {
    "Matrix": {
        "rok": 1999,
        "rezyser": "Lana i Lilly Wachowski",
        "ocena": 8.7
    },
    "Incepcja": {
        "rok": 2010,
        "rezyser": "Christopher Nolan",
        "ocena": 8.8
    },
    "Skazani na Shawshank": {
        "rok": 1994,
        "rezyser": "Frank Darabont",
        "ocena": 9.3
    }
}

# Wyświetlenie informacji o filmach
print("Zestawienie filmów:")

for tytul, dane in filmy.items():
    print(f"\nTytuł: {tytul}")

    for klucz, wartosc in dane.items():
        print(f"  {klucz}: {wartosc}")

# Ten program definiuje słownik 'filmy', gdzie kluczami są tytuły filmów,
# a wartościami są listy zawierające rok produkcji, reżysera i ocenę filmu.
# Następnie iteruje przez słownik i wyświetla informacje o każdym filmie w czytelnej formie.
