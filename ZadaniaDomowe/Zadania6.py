#Praca domowa lekcja 6. zadanie 9, 11, 12

# Dictionary comprehension - tworzenie słowników w jednej linii
liczby = [1, 2, 3, 4, 5]
kwadraty = {x: x**2 for x in liczby}
print(kwadraty) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtrowanie podczas tworzenia
parzyste_kwadraty = {x: x**2 for x in liczby if x % 2 == 0}
print(parzyste_kwadraty) # {2: 4, 4: 16}

#Czyszczenie słownika
kwadraty.clear()
print(kwadraty) # {}