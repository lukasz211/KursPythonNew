import os

# # Tworzenie słownika z danymi
# student = {
# 'imie': 'Anna',
# 'wiek': 25,
# 'oceny': [4.5, 5.0, 4.0],
# 'aktywny': True
# }

# # Dostęp do wartości przez klucz
# print(student['imie']) # Anna
# print(student['wiek']) # 25
# print("="*30)

# # Dostęp z użyciem metody get() - bezpieczniejsze (zwraca None jeśli klucz nie istnieje)
# print(student.get('imie')) # Anna
# print(student.get('miasto')) # None (zamiast KeyError)
# print(student.get('miasto', 'Warszawa')) # Warszawa (wartość domyślna)
# print("="*30)


# # Dodawanie nowych par klucz-wartość
# student['miasto'] = 'Kraków'
# student['email'] = 'anna@example.com'
# # Modyfikacja wartości
# student['wiek'] = 26

# print(student)
# print(type(student))

pusty_slownik = {}
inny_pusty = dict()

print(type(pusty_slownik))
print(type(inny_pusty))

print('='*30)

pusty_zbior = set()
print(type(pusty_zbior))

liczby = {1, 2, 3, 4, 5}
owoce = {'jabłko', 'banan', 'pomarańcza'}
print(type(liczby))
print(type(owoce))
print('='*30)
print("Pusty set")
pusty_set = {}   # Dictionary
print(type(pusty_set))


liczby2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
pierwszy, drugi, *reszta, _, ostatni = liczby2
print(pierwszy)
print(drugi)
print(reszta)
print(_)
print(ostatni)



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


#---------------------------------------------