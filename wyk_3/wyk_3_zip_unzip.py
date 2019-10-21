# "Odpakowywanie" (unzip):
lista = [1, 2]
a, b = lista # a = lista[0], b = lista[1]
print(a, b)

# splat (inaczej asterisk):
x = [1, 2, 3]
print(x)  # drukuje listę (1 argument)
print(*x) # drukuje "rozpakowaną" listę (3 argumenty)
print(x[0], x[1], x[2]) # równoważny zapis

x = "Python"
print(x)
print(*x) # zip/unzip działa na wszystkich sekwencjach
print(*x, sep='\t') # unzip z tabulatorem jako separatorem pomiędzy literami

# unzip i splat:
a, *b = lista # a = lista[0], b = reszta
print(a, b)

lista = [1, 2, 3, 4, 5]
a, *b, c = lista # a, b[0], b[1], b[2], c
print(a, b, c)

# "pakowanie" (zip)
x = [1, 2, 3]
y = ['a', 'b', 'c']
zipped = zip(x, y) # pary (x[i], y[i])
print(*zipped)

x = [1, 2, 3, 4]
y = ['a', 'b', 'c'] # długość nie ma znaczenia - ucina do listy o najmniejszej długości
zipped = zip(x, y) # pary (x[i], y[i])
print(*zipped)

# zip / unzip:
x = [1, 2, 3]
y = [4, 5, 6]
x_copy, y_copy = zip(*zip(x, y))
print(x == list(x_copy) and y == list(y_copy))

print(list(zip(x,y)))
print(*zip(x,y))
print(list(zip(*zip(x, y))))