'''
Typ logiczny (boolowski, boolean):
    przyjmuje wartości: prawda lub fałsz
    w Pythonie następujące wartości są utożsamiane z fałszem:
        False
        None
        zero dowolnego typu (0, 0.0, 0j)
        pusta sekwencja '', (), [] lub mapowanie {}
    pozostałe wartości uznawane są za prawdę
'''

'''
Operacje logiczne:
'''

# Operacje logiczne - or:
print("0 or 0 -> " + str(0 or 0))
print("1 or 0 -> " + str(1 or 0))
print("0 or 1 -> " + str(0 or 1))
print("1 or 1 -> " + str(1 or 1))

# Operacje logiczne - and:
print("0 and 0 -> " + str(0 and 0))
print("1 and 0 -> " + str(1 and 0))
print("0 and 1 -> " + str(0 and 1))
print("1 and 1 -> " + str(1 and 1))

'''
Porównania:
==      	   równe
!=      	   różne
<       	   mniejsze
>       	   większe
<=      	   mniejsze lub równe
>=      	   większe lub równe
is      	   ten sam identyfikator
is not  	   inny identyfikator
'''