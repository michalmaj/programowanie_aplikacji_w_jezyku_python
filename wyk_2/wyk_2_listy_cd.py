# slowa kluczowe/zastrzeżone:
import keyword
print(keyword.kwlist) # lista słów kluczowych w Pythonie


print(len(keyword.kwlist))


'''
Lista:
    sekwencja zmiennych dowolnego typu
    dynamiczny rozmiar
    inicjowana jest:
        nawiasy kwadratowe
        konstruktor klasy list
        list comprehension
'''

wyrazenie = "Python to najlepszy język programowania, służy do machine learning, data science"
print(wyrazenie.split())
print(wyrazenie.split(','))

# tworzenie listy z fragmentu innej listy
temp = wyrazenie.split()
# budowanie nowej listy z rozpakowanego stringa z innej listy
znaki = [*temp[0]]
print(znaki)