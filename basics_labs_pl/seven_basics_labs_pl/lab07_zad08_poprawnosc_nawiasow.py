def czy_poprawne_nawiasy(tekst):
    stos = []
    nawiasy_otwierajace = "([{"
    nawiasy_zamykajace = ")]}"
    pary = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for znak in tekst:
        if znak in nawiasy_otwierajace:
            stos.append(znak)

        elif znak in nawiasy_zamykajace:
            if not stos:
                return False
            if stos.pop() != pary[znak]:
                return False

    return len(stos) == 0


# Test działania
napis = input("Podaj ciąg znaków z nawiasami: ")

if czy_poprawne_nawiasy(napis):
    print("Nawiasy są poprawnie wstawione.")
else:
    print("Nawiasy są NIEpoprawne.")
# Ten program definiuje funkcję 'czy_poprawne_nawiasy', która sprawdza, czy nawiasy w podanym ciągu znaków są poprawnie zagnieżdżone i zamknięte.
# Używa stosu do śledzenia otwierających nawiasów i sprawdza, czy każdy zamykający nawias odpowiada ostatniemu otwierającemu nawiasowi.