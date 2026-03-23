# Tworzenie słownika z danymi
student = {
'imie': 'Anna',
'wiek': 25,
'oceny': [4.5, 5.0, 4.0],
'aktywny': True
}

# Dostęp do wartości przez klucz
print(student['imie']) # Anna
print(student['wiek']) # 25
print("="*30)

# Dostęp z użyciem metody get() - bezpieczniejsze (zwraca None jeśli klucz nie istnieje)
print(student.get('imie')) # Anna
print(student.get('miasto')) # None (zamiast KeyError)
print(student.get('miasto', 'Warszawa')) # Warszawa (wartość domyślna)
print("="*30)

# Dodawanie nowych par klucz-wartość
student['miasto'] = 'Kraków'
student['email'] = 'anna@example.com'
# Modyfikacja wartości
student['wiek'] = 26

print(student)

# # Usuwanie elementów
# del student['aktywny'] # Usuwa parę klucz-wartość

wiek_studenta = student.pop('wiek') # Usuwa i zwraca wartość (26)
print(student)
# {'imie': 'Anna', 'oceny': [4.5, 5.0, 4.0], 'miasto': 'Kraków', 'email':'anna@example.com'}