#struktury danych

#Lista:
# każdy element listy można zastąpić
x = [1,2,3,4,5,6]
print(len(x)) # pokaże ilośc elementów

print(x[2])# dostęp do konkretnego elementu

print(x[:3])# Wyświetli elementy od zerowego indeksu do trzeciego

print(x[3:])# to samo co powyżej ale od trzeciego indeksu

print(x[1:3])# ponieważ python jest lewostronnie domknięty
# wyświetli elementy od indeksu <1 do 3) do drugiego włącznie : pierwszy, drugi

print(x[-2:])# chcemy dwa ostatnie elementy listy

x.extend([7,8])# roszerzanie lsity o kolejne elementy
print(x)

x.append(9)# dodanie do listy jednego elementu
print(x)

# Można także mieć złożone struktury
y = [10,11,12]
listaList = [x,y]
print(listaList)

# sortowanie listy
z = [3,1,2]
z.sort()
print(z)
# odwrotność sortowania
z.sort(reverse=True)
print(z)

# dodatek do list
przyjaciele = ["Paweł", "Partycja", "Marek", "Marta"]
print(przyjaciele)

# dodanie osoby na konkretny index
przyjaciele.insert(1,"Tomasz")
print(przyjaciele)

# sprawdzenie czy osoba jest na liście, zwraca index
print(przyjaciele.index("Tomasz"))

# zlicza ile razy wystąpi dany ciąg
print(przyjaciele.count("paweł"))

# usuwa osobę o danym indeksie, jeżli będą () to usunie ostatnią
przyjaciele.pop()
print(przyjaciele)
