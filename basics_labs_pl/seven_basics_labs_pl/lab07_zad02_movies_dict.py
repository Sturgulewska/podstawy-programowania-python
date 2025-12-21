filmy = {
    "Matrix": [1999, "Lana i Lilly Wachowski", 8.7],
    "Inception": [2010, "Christopher Nolan", 8.8],
    "Skazani na Shawshank": [1994, "Frank Darabont", 9.3]
}

for tytul, dane in filmy.items():
    print(f"Tytuł: {tytul}")
    print(f"Rok: {dane[0]}, Reżyser: {dane[1]}, Ocena: {dane[2]}")
    print()
# Ten program definiuje słownik 'filmy', gdzie kluczami są tytuły filmów,
# a wartościami są listy zawierające rok produkcji, reżysera i ocenę filmu.
# Następnie iteruje przez słownik i wyświetla informacje o każdym filmie w czytelnej formie.