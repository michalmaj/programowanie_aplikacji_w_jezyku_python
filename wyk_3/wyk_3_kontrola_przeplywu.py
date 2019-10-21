'''
Paradygmaty programowania w Pythonie:
    programowanie strukturalne (np. Fortran, C)
    programowanie obiektowe (np. C++, Java)
    programowanie funkcyjne (np. Lisp, Haskell)
'''

'''
Programowanie strukturalne:
trzy struktury sterujące:
    sekwencja - wykonanie instrukcji w zadanej kolejności
    wybór - wykonanie instrukcji w zależności od stanu
    iteracja - wykonywanie instrukcji dopóki (nie)spełniony jest warunek
'''

# przykład funkcji w Pythonie
# przykład Python
# słowo kluczowe def, nazwa funkcji, parametry
def bezpieczne_dzielenie (a, b):
    if b != 0:
        return a / b
    else:
        return "Nie dziel przez zero!"

print(bezpieczne_dzielenie(2,3))
print(bezpieczne_dzielenie(11,0))

'''
Wcięcia:
    spacje (zalecane) lub tabulacje
    w Pythonie 3 nie wolno mieszać (w Pythonie 2 się nie zaleca)
    najczęściej wcięce = 4 spacje (czytelność)
    wiele edytorów umożliwia zamianę tab na spacje
'''

'''
Instrukcja warunkowa if:
    wykonaj instrukcje, jeśli spełniony jest warunek
'''
'''
if warunek: # zwróć uwagę na :
    instrukcja1
    instrukcja2
    ...
'''
if 2 > 1:
    print("2 jest większe od 1")

'''
Instrukcja warunkowa if else:
    wykonaj instrukcje, jeśli spełniony jest warunek, lub wykonaj inne instrukcje
'''
'''
if warunek:
    instrukcja1
    instrukcja2
    ...
else:
    instrukcja3
    instrukcja4
    ...
'''
if 2 > 3:
    print("2 jest większe od 3")
else:
    print("2 nie jest większe od 3")

'''
Instrukcja warunkowa if elif else:
    wykonaj jeśli, lub wykonaj jeśli, ..., lub wykonaj
'''
'''
if warunek1:
    instrukcja1
    instrukcja2
    ...
elif warunek2:
    instrukcja3
    instrukcja4
    ...
.
.
.
else:
    instrukcja5
    instrukcja6
'''
if 2 > 3:
    print("2 jest większe od 3")
elif 2 == 3:
    print("2 jest równe 3")
else:
    print("2 jest mniejsze od 3")


# przykład:
print("Podaj liczbę:", end=' ')

raw_x = input() # pobierz stringa z wejścia standardowego
x = eval(raw_x) # zinterpretuj jako wyrażenie Pythona

# x % 2 zwraca resztę z dzielenia
# każda wartość != 0 jest traktowana jako prawda
if x % 2:
    print("Podana liczba jest nieparzysta.")
else:
    print("Podana liczba jest parzysta.")

print(help(eval))

type(eval(input())) # parsuje wejście jako komendę