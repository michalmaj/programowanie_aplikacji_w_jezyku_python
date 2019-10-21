# kontrola przepływu przykłady:
# Przykład pierwszy:
lista = [1, 2.0, 'Python', 4, 1j]
for element in lista:
    if type(element) is not str:
        print(element)

# Przykład drugi:
lista = [1, 2.0, 'Python', 4, 1j]
for element in lista:
    if type(element) is str:
        for litera in element:
            print(litera)

# Przykład trzeci
lista = [1, 2.0, 'Python', 4, 1j]
for i in range(len(lista)):
    print(str(i + 1) + ". " + str(lista[i]))

# unzip i for:
lista = [[1, 'a'], [2, 'b'], [3, 'c']]
for cyfra, litera in lista:
    print(str(cyfra) + ". " + litera)

cyfry = [1, 2, 3]
litery = ['a', 'b', 'c']
for cyfra, litera in zip(cyfry, litery):
    print(str(cyfra) + ". " + litera)

# enumerate:
lista = ['a', 'b', 'c']
list(enumerate(lista))

for index, element in enumerate(lista):
    print(str(index + 1) + ". " + element)