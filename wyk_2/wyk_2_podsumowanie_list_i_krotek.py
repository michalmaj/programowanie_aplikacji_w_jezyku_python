'''
Sekwencyjne typy danych:
    list - dynamiczny ciąg zmiennych dowolnego typu
    tuple - niezmienniczy ciąg zmiennych dowolnego typu
    range - niezmienniczy ciąg liczba całkowitych
    str - niezmienniczy ciąg znaków
'''

'''
Operacje na sekwencjach:
'''

'''
    in - prawda jeśli element należy do sekwencji, inaczej fałsz
    not in - fałsz jeśli element należy do sekwencji, inaczej prawda
'''

slowo = "Python"
print("t" in slowo)
print("p" not in slowo)

'''
    concatenation
'''
poczatek = "Python "
srodek = "jest "
koniec = "świetny!"
print(poczatek + srodek + koniec)

lista = [1, 2, 3, 4]
dodatek = [5, 6, 7, 8]
print(dodatek + lista) # kolejność ma znaczenie

'''
    mnożenie przez liczbę calkowitą
'''
znak = '+'
print(znak * 10)

krotka = (1, 2, 3)
print(2 * krotka)

lista = [1, 2, 3, "Python"]
print(3*lista)

'''
    wycinki
'''
lista = [1, 2, 3, "Python"]
print(lista[:2]) # dwa pierwsze
print(lista[3][-2:]) # dwa ostatnie ostatniego

print(range(3, 15, 3)[:2]) # dla range też działa

'''
Wbudowane funkcje dla sekwencji:
    len - długość sekwencji
    min, max - najmniejszy, największy element
'''
print(len([1,2,-3])) # liczba elementów
print(len([1,2,-3])) # minimum

print(max("Python")) # maximum
print(min("Python")) # czemu nie działa, tak jak zakładamy!?
# naprawa problemu:
print(min("Python".lower())) # kodowanie znaków
print(ord(u"P")) # przykład dla "P"
print(ord(u"h")) # przykład dla "h"

'''
Wspólne funkcje klasowe sekwencji:
    index - indeks pierwszego znalezionego elementu
    count - ilość wystąpień elementu
'''
x = [1, 2, 3, 4, 5] * 2
print(x)
print(x.count(4)) # liczba 4 pojawia się 2 razy
print(x.index(4)) # pierwszy raz dla i=3

'''
Operacje na sekwencjach "zmiennych" (mutable):
    znana mutable: list
    sekwencje "niezmienne" (immutable): tuple, range i str
'''
lista = [1, 2, 3]
lista[1] = 4 # zamień wartość drugiego elementu
print(lista)

lista = [1, 2, 3]
lista[1:2] = [5, 5] # zamień wycinek
print(lista)

lista = [1, 2, 3]
del lista[1:2] # usuń wycinek
print(lista)

lista = list(range(10))
del lista[::2] # usuń co drugi element
print(lista)

'''
Funkcje klasowe sekwencji "zmiennych" (mutable)
'''
lista = [1, 2, 3, 4, 5]
lista.append(6) # append dodaje element na koniec listy
print(lista)
lista.append([7, 8, 9]) # lista dodana jako element - append() dodaje tylko JEDEN element
print(lista)

lista = [1, 2, 3, 4, 5]
lista.extend([6, 7, 8, 9]) # extend rozwija listę
print(lista)

lista = [1, 2, 3]
lista.clear() # usuwa wszystkie elementy
print(lista)

lista = [1, 2, 3]
kopia = lista.copy() # kopiuje całą listę
print(kopia)

lista = [1, 2, 3]
lista.insert(1, 4) # wstaw 4 pod indeks 1
print(lista)

lista = [1, 2, 3]
print(lista.pop(1)) # zwróć i usuń *i*-ty element
print(lista)

lista = ['a', 'b', 3] * 3

print(lista)
lista.remove('b') # usuń element (pierwsze wystąpienie)
print(lista)

lista = [1, 2, 3]
lista.reverse() # odwróć kolejność
print(lista)

'''
Funkcja sort - tylko dla list:
'''
print(help(list.sort))

lista = ['e', 'D', 'a', 'b', 'C']
lista.sort() # sortuj
print(lista)
lista.sort(key=str.lower) # sortuj wg funkcji key
print(lista)