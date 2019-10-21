'''
Krotka (tuple):
    sekwencja zmiennych dowolnego typu
    stały rozmiar
    inicjowana jest:
        nawiasy okrągłe
        ciąg elementów oddzielonych przecinkiem
        konstruktor klasy tuple
'''

krotka = (1, 2, 3, "Python") # jak lista, ale () zamiast []
print(krotka)

krotka = 1, 2, 3, "Python" # brak nawiasów = tuple
print(krotka)

x,y,z,h = krotka # forma rozpakowywania krotki, pod warunkiem, że ilość zadeklarowanych zmiennych jest taka sama jak długość krotki
print(x,y,z,h)

lista = list("Python") # lista ze stringa
krotka = tuple(lista)  # krotka z listy
print(lista)
print(krotka)

'''
Lista vs Krotka:
    krotka ma stały rozmiar a lista jest dynamiczna
    krotka jest immutable w przeciwieństwie do listy mutable
    jeśli sekwencja obiektów jest stała w czasie działania programu, lepiej używać krotek
        szybsze
        bezpieczniejsze
        mogą być kluczami w słowniku
'''

# w listach można podmieniać wartości używając indeksu
lista = [1, 2, 3]
print(lista)
lista[0] = 2
print(lista)

krotka = (1, 2, 3)
krotka[1] = 2 # nie można przypisywać, krotka jest "niezmienna"