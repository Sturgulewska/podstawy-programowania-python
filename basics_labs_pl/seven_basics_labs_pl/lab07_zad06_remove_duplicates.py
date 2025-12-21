def usun_duplikaty(lista):
    return list(set(lista))

dane = [1, 2, 2, 3, 4, 4, 5]
print(usun_duplikaty(dane))
# Ten program definiuje funkcję 'usun_duplikaty', która usuwa duplikaty z podanej listy, zwracając nową listę zawierającą tylko unikalne elementy.
# Używa zbioru (set) do eliminacji duplikatów, a następnie konwertuje go z powrotem na listę.