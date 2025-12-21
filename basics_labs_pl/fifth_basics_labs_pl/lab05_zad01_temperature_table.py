# Tabela temperatur Celsjusz -> Fahrenheit

print(f"{'Celsius':>10} | {'Fahrenheit':>12}")
print("-" * 25)

for c in range(0, 41, 2):
    f = (c * 9 / 5) + 32
    print(f"{c:>10} | {f:>12.2f}")
# Ten program generuje i wyświetla tabelę konwersji temperatur z Celsjusza na Fahrenheita.
# Wykorzystuje pętlę for do iteracji przez wartości temperatur od 0 do 40 stopni Celsjusza z krokiem co 2 stopnie,
# oblicza odpowiadające wartości w stopniach Fahrenheita i formatuje wyjście w czytelnej tabeli.