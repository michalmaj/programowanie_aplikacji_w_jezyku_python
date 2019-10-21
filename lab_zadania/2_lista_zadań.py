# zadanie 1:
print("zadanie 1.")
krotka = (*range(5), "pięć", "sześć", "siedem", "osiem", "dziewięć")
print(krotka)
lista = krotka[:2]
print(lista)
druga_krotka = krotka[-3:]
print(druga_krotka)
druga_lista = krotka[1::2]
print(druga_lista)
print(len(krotka[5]))

# zadanie 2:
print("\nzadanie 2.")
lista_studentow = ["Janusz", "Grażyna", "Seba", "Karyna"]
lista_studentow.append("Jessica")
print(lista_studentow)
lista_studentow.extend(["Kłentin", "Dżordż"])
print(lista_studentow)
print(f"Wyświetlenie listy studentów od końca: {lista_studentow[::-1]}")
lista_studentow.sort()
print(lista_studentow)
lista_studentow.sort(reverse=True)
print(lista_studentow)
sorted(lista_studentow)
print(lista_studentow[1])
print(lista_studentow[4:6])
print(lista_studentow[-3:])
lista_studentow.pop(len(lista_studentow)-2)
print(lista_studentow)
krotka = tuple(lista_studentow)
print(krotka)

# zadanie 3:
print("\nzadanie 3.")
lista_liczba = []
for i in range(1,101):
    if i%3:
        pass
    else:
        lista_liczba.append(i)

print(lista_liczba)
del lista_liczba[4::2]
print(lista_liczba)
srednia = sum(lista_liczba)/len(lista_liczba)
print(srednia)

# zadanie 4:
print("\nzadanie 4.")
krotka_litery = ('x','y','h','w')
print("".join(krotka_litery))
print(" ".join(krotka_litery))
print(",".join(krotka_litery))

# zadanie 5:
print("\nzadanie 5.")
# pierwsza wersja
print("	".join("8"*100))
# druga wersja
for i in range(1,101):
    if i <= 99:
        print("8\t", end='')
    else:
        print("8")


# zadanie 6:
print("\nzadanie 6")
# Proszę naprawić:
i = 0

# pętla wydrukuje 0 i utknie na 1
while i < 10:
    if i % 2:
        i += 1
        continue
    print(i, end=' ')
    i += 1
print()

# zadanie 9:
print("\nzadanie 9")
x = 20
y = "dwadzieścia"
x, y = y, x
print(x, y)
