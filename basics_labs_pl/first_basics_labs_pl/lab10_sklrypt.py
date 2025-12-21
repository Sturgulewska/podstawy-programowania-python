# Program wykonujący podstawowe operacje matematyczne na dwóch liczbach całkowitych

a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))

print("Dodawanie:", a + b)
print("Odejmowanie:", a - b)
print("Mnożenie:", a * b)

# Dzielenie
if b != 0:
    print("Dzielenie:", a / b)
    print("Dzielenie całkowite:", a // b)
    print("Reszta z dzielenia:", a % b)
else:
    print("Dzielenie: nie można dzielić przez zero")
    print("Dzielenie całkowite: nie można dzielić przez zero")
    print("Reszta z dzielenia: nie można dzielić przez zero")

print("Potęgowanie:", a ** b)
# Ten program pobiera od użytkownika dwie liczby całkowite i wykonuje na nich podstawowe operacje matematyczne: dodawanie, odejmowanie, mnożenie, dzielenie, dzielenie całkowite, resztę z dzielenia oraz potęgowanie.
# Program obsługuje również przypadek dzielenia przez zero, wyświetlając odpowiedni komunikat.