# zadanie 1
print("zadanie 1")
parzyste = range(2,100,2)
a,b,c,*d = parzyste
print(a,b,c,d)
x,y,z,*_ = parzyste
print(_)
# wersja prosta
start, *temp, stop = parzyste
print(start,stop)
nowa_lista = temp
print(nowa_lista)
# wersja złożona
pierwsza, ostatnia = parzyste[0], parzyste[len(parzyste)-1]
print(pierwsza,ostatnia)
lista_srodek = [*parzyste]
print("Moja lista: ", lista_srodek)
print(lista_srodek[1:(len(lista_srodek)-1)])

# zadanie 2
print("\nzadanie 2")
lista_liczb = [*range(0,101)]
lista_kwadratow = [element**2 for element in lista_liczb]

for index, wartosc1 in enumerate(zip(lista_liczb,lista_kwadratow)):
    print(f" Liczba {wartosc1[0]} podniesiona do kwadratu daje wynik: {wartosc1[1]}")

# zadanie 3
print("\nzadanie 3")
a = 3
b = 4
c = 5

A = [a, b, c]
A.sort(reverse = True)

T = A[0]**2 - (A[1]**2 + A[2]**2)
C = (A[1] + A[2])

if A[0] < C:
    print("tak z odcinków o podanej długości można zbudować trójką")
    if T == 0:
        print("tak będzie to trójkąt prostokątny")
    else:
        print("nie będzie to trójkąt prostokątny")
else:
    print("z podanych odcinków nie można zbudować trójkąta")


# zadanie 4
print("\nzadanie 4")
import random
ukryta_liczba = random.randint(1,100)
print(ukryta_liczba)
while True:
    podana_liczba = int(input("Podaj liczbę: "))
    if podana_liczba == ukryta_liczba:
        print("Wygrana!")
        break
    else:
        if abs(podana_liczba-ukryta_liczba)<50 and abs(podana_liczba-ukryta_liczba)>=10:
            print("Różnica jest mniejsza niż 50")
        elif abs(podana_liczba-ukryta_liczba) < 10 and abs(podana_liczba-ukryta_liczba)>=5:
            print("Różnica jest mniejsza niż 10")
        elif abs(podana_liczba - ukryta_liczba) < 5 and abs(podana_liczba - ukryta_liczba) >= 3:
            print("Róznica jest mniejsza od 5")
        elif abs((podana_liczba - ukryta_liczba)) < 3:
            print("Już prawie, różnica jest mniejsza od 3")
        else:
            print("Różnica jest większa niż 50")





