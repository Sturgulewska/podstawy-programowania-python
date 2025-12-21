# Obliczanie średniej ocen

n = int(input("Ile ocen chcesz podać? "))
suma = 0

for i in range(n):
    ocena = float(input(f"Podaj ocenę {i + 1}: "))
    suma += ocena

srednia = suma / n
print("Średnia ocen:", srednia)
# Ten program oblicza średnią ocen podanych przez użytkownika.
# Najpierw pyta, ile ocen użytkownik chce wprowadzić, a następnie w pętli pobiera każdą ocenę, sumuje je i na końcu dzieli sumę przez liczbę ocen, aby uzyskać średnią, którą następnie wyświetla.