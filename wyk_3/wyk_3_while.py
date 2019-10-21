'''
Pętla while:
    wykonuj blok instrukcji dopóki warunek jest spełniony
'''

'''
while warunek:
    instrukcje
'''
i = 0
while i < 5: # wykonuj dopóki i < 5
    i += 1   # bez tego mamy nieskończoną pętlę
    print(i, sep = ',',end='')

# przykład z instrukcją warunkową if:
n = input("Podaj liczbę całkowitą: ")
if n.isdigit():
    print("Twoja liczba to:", n)
else:
    print(n, "nie jest liczbą całkowitą...")

# przykład z pętlą while:
n = input("Podaj liczbę całkowitą: ")
while not n.isdigit():
    n = input("Spróbuj jeszcze raz: ")
print("Twoja liczba to:", n)

''''
Przykład nieskończonej pętli while:
i = 1
while i != 10:
    i += 2
'''

'''
Dodatkowe instrukcje sterujące:
    break - przerwij pętlę
    continue - przerwij obecną iterację
    pass - nie rób nic
    else - wykonuj jeśli pętla zakończyła się inaczej niż break
'''

# break:
for i in range(10): # drukuj liczby z range(10)
    print(i, end=' ')
    if i > 5:       # przerwij pętlę jeśli i > 5
        break

i = 0
while True:   # wykonuj w niekończoność
    print(i, end=' ')
    if i > 5: # przerwij pętlę jeśli i > 5
        break
    i += 1    # bez tego byłaby nieskończona pętla zer

# continue:
for i in range(10):
    if i % 2:    # jeśli i jest nieparzyste
        continue # pomiń
    print(i, end=' ')

i = 0
# pętla wydrukuje 0 i utknie na 1
while i < 10:
    if i % 2:
        i += 1
        continue
    print(i, end=' ')
    i += 1

# pass:
for i in range(10):
    if i % 2:    # jeśli i jest nieparzyste
        pass     # nie rób nic
    else:        # w innej sytuacji drukuj
        print(i, end=' ')

i = 0
# w praktyce napisalibyśmy: if not i % 2: print...
while i < 10:
    if i % 2:
        pass
    else:
        print(i, end=' ')
    i += 1

# else:
for i in range(10):
    if i < 5: # drukuj mniejsze od 5
        print(i, end=' ')
    else:     # dla pozosyałych nie rób nic
        pass
else: # wykonaj po zakończeniu pętli
    print("Koniec pętli.")

for i in range(10):
    if i < 5: # drukuj mniejsze od 5
        print(i, end=' ')
    else:     # przerwij pętlę
        break
else: # pętla nie doszła do końca przez break
    print("Koniec pętli.")