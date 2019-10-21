'''
Pętla for:
    pętla po sekwencji
    pętla po (ayrtmetycznym) ciągu liczb
'''

'''
Pętla for w Pythonie:
    for po liście:
'''
lista = ['a', 'b', 'c', 'd']
for element in lista: # pętla po liście, w każdym kroku
    print(element)    # element zmienia swoją wartość

# for "krok po kroku":
lista = ['a', 'b', 'c', 'd']
it = iter(lista)
element = next(it)
print(element)
element = next(it)
print(element)
element = next(it)
print(element)
element = next(it)
print(element)

lista = ['a', 'b', 'c', 'd']
it = iter(lista)
# pętla po iteratorze it
# wewnątrz "ręcznie" wywołujemy next()
for i in it:
    print("i = " + str(i))
    print("next(it) = " + str(next(it)))

# for po wycinkach:
lista = ['a', 'b', 'c', 'd']
for element in lista[-2:]:
    print(element, end=' ')

for i in range(10)[::2]:
    print(i, end=' ')

# for po krotce:
krotka = ('a', 'b', 'c', 'd')
for element in krotka: # pętla po krotce
    print(element)     # działa jak po liście

# for po stringu:
slowo = "Python"
for litera in slowo: # pętla po stringu
    print(litera)    # iteruje po literach

# for po range:
for liczba in range(5): # pętla po range
    print(liczba)       # "odpowiednik" for (i = 0; ...)
