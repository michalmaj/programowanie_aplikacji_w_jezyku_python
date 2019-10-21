# Identyfikator zmiennej:

print(help(id))

x = 2 # zmiennej x przypisz wartość 2
print(id(x)) # wyświetl jej id
y = 2
print(id(y)) # to samo id co x
print(x is y) # zmienne x i y wskazują w to samo miejsce

# id dla list:
x = [1, 2, 3] # lista
y = [1, 2, 3] # taka sama lista

print(x == y) # rzeczywiście takie samo porównanie
print(x is y) # ale inne id
print(id(x), id(y)) # listy mają różne id
print(x[0] is y[0]) # ale elementy już nie

'''
Operator is porównuje id dwóch obiektów, podczas gdy operator == porównuje wartości dwóch obiektów.
Istnieje różnica w znaczeniu między równością a id.
'''

x = y # przypisz zmiennej x obieky y

print(x is y) # teraz x i y wskazują to samo

'''
Mutable vs Immutable kolejny raz:
    immutable: int, float, complex, str, tuple, (frozen set, bytes)
        przypisanie zmiennej nowej wartości tworzy nowy obiekt w pamięci
    mutable: list, (set, dict, byte array)
        możliwa modyfikacja obiektu
'''
# proszę zwrócić uwagę na zmianę id
x = 2
print(id(x))
x = 3
print(id(x))
x = [2]
print(id(x))
# i teraz:
x.append(3)
print(id(x))

# Wynikające konsekwencje:
x = 2 # uwtórz obiekt typu int
y = x # y wskazuje na to samo co x
y = 5 # zmieniam y - nowe miejsce w pamięci
print(x) # x dalej wskazuje na 2
# jednak w przypadku:
x = [1, 2, 3] # utwórz obiekt typu list
y = x # y wskazuje na to samo co x (więc jest to jeden obiekt)
print(id(x), id(y))
# więc modyfikując:
y[0] = 4 # modyfikuję y
print(x) # a zmienia się x...
# w związku z tym zaleca się użycia copy():
x = [1, 2, 3] # utwórz obiekt typu list
y = x.copy()  # stwórz kopię tego obiektu
print(id(x), id(y)) # teraz są to dwa różne obiekty