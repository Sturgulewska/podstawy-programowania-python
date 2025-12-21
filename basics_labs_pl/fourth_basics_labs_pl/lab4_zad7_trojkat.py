# Zadanie 7 – sprawdzanie trójkąta

def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Nie można zbudować trójkąta"
    elif a == b == c:
        return "Trójkąt równoboczny"
    elif a == b or a == c or b == c:
        return "Trójkąt równoramienny"
    else:
        return "Trójkąt różnoboczny"

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

print(triangle(a, b, c))
# Ten program określa typ trójkąta na podstawie długości jego boków.
# Definiuje funkcję 'triangle', która przyjmuje długości trzech boków jako argumenty i zwraca informację o typie trójkąta lub czy trójkąt nie może zostać zbudowany.
# Następnie pobiera długości boków od użytkownika i wyświetla wynik.