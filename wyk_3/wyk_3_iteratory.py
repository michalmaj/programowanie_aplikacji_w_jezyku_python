'''
Iteratory:
    iterator wskazuje element sekwencji oraz umożliwia dostęp do następnego
'''

lista = ['a', 'b', 'c', 'd'] # zwykła lista
it = iter(lista) # iterator listy (wskazuje na początek)
print(next(it)) # zwraca 1 element i przesuwa "wskaźnik"
print(next(it)) # zwraca 2 element i przesuwa "wskaźnik"
print(next(it)) # zwraca 3 element i przesuwa "wskaźnik"
print(next(it)) # zwraca 4 element i przesuwa "wskaźnik"

print()


i = 0

def funkcja():
    """Z każdym wywołaniem zwraca kolejną liczbę całkowitą."""
    global i # użyj globalnej zmiennej i
    i += 1   # zwiększ
    return i # i zwróć

# kolejne wartości zwracane przez funkcję
# iterowane aż zwróci 4
it = iter(funkcja, 4)

print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # StopIteration