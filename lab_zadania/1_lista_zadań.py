# zadanie 1:
print("zadanie 1.")
from math import cos, pi
A = [11, 3.7, 57, -81]
print(f"Suma liczb to: {sum(A)}")
B = [53, 67, 8, 69, 44, 63, 2, 67, 60, 1, 60]
print(f"Średnia to: {sum(B)/len(B)}")
print(f"cos(pi) = {cos(pi)}")

# zadanie 2:
# w trybie interaktywnym

# zadanie 3:
print("\nZadanie 3")
print(round(7.5))
print(round(2.5))
print("funkcja round() w przypadku N.5 zawsze zaokrągla do najbliższej liczby parzystej, gdzie N oznacza liczby naturalne")

# zadanie 4:
print("\nZadanie 4")
import sys
print(f"funkcja maxsize() pokazuje rozmiar wskaźnika, można więc poznać ograniczenia rozmiaru struktur danych Pythona (np. łańcuchy, listy etc) {sys.maxsize}")

# zadanie 5:
print("\nZadanie 5")
pierwsza_zmienna = "Pierwsza"
druga_zmienna = "Druga"
trzecia_zmienna = 5
# print(pierwsza_zmienna * druga_zmienna) - nie wykona się, można na przykład wykonać iloczyn długości zadanych str.
print(pierwsza_zmienna + druga_zmienna)
print(pierwsza_zmienna * trzecia_zmienna)
print(pierwsza_zmienna + str(trzecia_zmienna))

# zadanie 6:
print("\nZadanie 6")
a = "      banan         "
b = "banan"
c = "4321890"
print(f"Moje słowo to {a.strip()} i nie ma spacji na początku i końcu")
print(f"{b.rjust(50)}")
print(c.isnumeric())

# zadanie 7:
print("\nZadanie 7")
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
print(a*b)
print(2*a+2*b)