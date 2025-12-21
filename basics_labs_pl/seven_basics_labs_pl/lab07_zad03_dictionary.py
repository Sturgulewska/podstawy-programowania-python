slownik = {}

def dodaj_slowo(pl, en):
    slownik[pl] = en

def wyswietl_slownik():
    for pl, en in slownik.items():
        print(pl, "->", en)

def wyszukaj_slowo(pl):
    if pl in slownik:
        print("Tłumaczenie:", slownik[pl])
    else:
        print("Brak takiego słowa")

def usun_slowo(pl):
    if pl in slownik:
        del slownik[pl]

# Przykładowe użycie
dodaj_slowo("kot", "cat")
dodaj_slowo("pies", "dog")
wyswietl_slownik()
wyszukaj_slowo("kot")
usun_slowo("pies")
wyswietl_slownik()