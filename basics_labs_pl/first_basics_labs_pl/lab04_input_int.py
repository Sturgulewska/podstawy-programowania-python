# Zadanie 4 – input i konwersja typu

string_value = input("Podaj liczbę całkowitą: ")
print(type(string_value))

x = int(string_value)
print(type(x))
# To jest program, który pobiera od użytkownika wartość za pomocą funkcji input,
# wyświetla jej typ (który jest zawsze stringiem), a następnie konwertuje tę wartość na liczbę całkowitą za pomocą funkcji int i ponownie wyświetla jej typ.

try:
    string_value = input("Podaj liczbę całkowitą: ")
    x = int(string_value)
    print(f"Podano liczbę: {x}")
except ValueError:
    print("To nie jest liczba całkowita!")
# Dodatkowo program obsługuje sytuację, gdy użytkownik nie poda prawidłowej liczby całkowitej,
# wyświetlając odpowiedni komunikat o błędzie.