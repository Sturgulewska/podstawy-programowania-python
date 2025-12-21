# Zadanie 3 – przeliczanie punktów na ocenę

def grade(avg):
    if avg >= 4.75:
        return 5.0
    elif avg >= 4.25:
        return 4.5
    elif avg >= 3.75:
        return 4.0
    elif avg >= 3.25:
        return 3.5
    elif avg >= 3.0:
        return 3.0
    else:
        return 2.0

average = float(input("Podaj średnią: "))
print("Ocena:", grade(average))
# Ten program przelicza średnią punktów na ocenę według określonej skali.
# Definiuje funkcję 'grade', która przyjmuje średnią jako argument i zwraca odpowiednią ocenę.
# Następnie pobiera średnią od użytkownika i wyświetla obliczoną ocenę.