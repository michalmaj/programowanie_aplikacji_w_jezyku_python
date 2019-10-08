# tak pisząc jest probem, bo każdorazowa zmiana imienia i wieku musi nastąpić w każdym prinie
print("był sobie mężczyzna i nazywał się Kłentin")
print("miał 55 lat")
print("bardzo lubił imie Kłentin")
print("ale nie lubił, że ma 55 lat")

# pierwsza wersja: utworzenie zmiennych i ich modyfikacja
imie = "Kłentin"
wiek = 55
print("był sobie mężczyzna i nazywał się " + imie)
print("miał" + str(wiek) + " lat")# rzutownie int na str
print("bardzo lubił imie " + imie)
print("ale nie lubił, że ma " + str(wiek) + " lat")# rzutownie int na str



# Więcej wyświetlania ze zmianą wielkości czcionki
wyrazenie = "Wykład Python"
print(wyrazenie.lower())
print(wyrazenie[0]) # indesk zaczyna się od 0
print(wyrazenie.index("n"))# poda na którym ideksie znajduje się litera
print(wyrazenie.replace("Wykład", "Moduł"))
