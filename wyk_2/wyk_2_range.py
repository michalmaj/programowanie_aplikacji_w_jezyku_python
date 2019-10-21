'''
Range:
    w Pythonie 3 jest to typ danych (klasa)
    reprezentuje sekwencję liczb
    przechowuje tylko informację o początku, końcu i kroku
'''

x = range(10) # druga wersja x = range(0,10)
print(x)
print(list(x)) # zrzutujemy, żeby wyświetlić w formie listy

x[0] = 1 # range jest immutable, podobnie jak krotka