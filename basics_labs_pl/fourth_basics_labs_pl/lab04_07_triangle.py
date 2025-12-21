# Zadanie 7 – trójkąt

def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Nie można zbudować trójkąta"
    if a == b == c:
        return "Trójkąt równoboczny"
    elif a == b or a == c or b == c:
        return "Trójkąt równoramienny"
    else:
        return "Trójkąt różnoboczny"

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

print(triangle_type(a, b, c))
# Ten program określa typ trójkąta na podstawie długości jego boków.
# Definiuje funkcję 'triangle_type', która przyjmuje długości trzech boków jako argumenty i zwraca informację o typie trójkąta lub czy trójkąt nie może zostać zbudowany.
# Następnie pobiera długości boków od użytkownika i wyświetla wynik.