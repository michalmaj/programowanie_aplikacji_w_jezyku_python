'''
Formatowanie tekstu:
'''
print(help(print))

a, b, c = 1, 2, 3
print(a, b, c) # domyślnym separatorem jest spacja

print(a, b, c, sep='_') # ale można go zmiennić

print(a, b, c, sep="...", end=" koniec")

x = 2
"x jest równe " + str(x) # skuteczne, ale mało wygodne

x = 2
# klasa string ma metodę format
"x jest równe {}".format(x)

# która w miejsce {} wstawia kolejne argumenty
"x jest równe {}, a x**2 = {}".format(x, x**2)

x = 2
y = 2.5
z = "trzy"
# domślnie pod {} wstawiane są kolejne argument format
"x, y, z = {}, {}, {}".format(x, y, z)

# ale kolejność można zmienić
"x, y, z = {2}, {0}, {1}".format(x, y, z)

a = 5
print(f"Moja zmienna {a}")

x = 1234567890
y = 1234567890.1234567890
z = "Python"
# z reguły nie ma potrzeby jawnej deklaracji typu
print("x, y, z = {}, {}, {}".format(x, y, z))

# ale można to zrobić
# d - int; f - float; s - str
print("x, y, z = {:d}, {:f}, {:s}".format(x, y, z))

# e - wygodny format dla dużych liczb - notacja matematyczna
# XeY = X * 10^Y
print("x, y, z = {:f}, {:e}, {}".format(x, y, z))

