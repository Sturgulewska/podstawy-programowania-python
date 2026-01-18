# ============================================
# Laboratorium –
####################################################

imie = input("Podaj swoje imie: ")

nazwisko = input ("Podaj swoje nazwisko: ")

email = input ("Podaj swoje email: ")

plik = open('dane.txt', 'a');

plik.write(imie + " " + nazwisko + " " + email);

plik.close();