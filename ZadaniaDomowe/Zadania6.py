#Praca domowa lekcja 6. zadanie 9, 11, 12

# Zadanie 9 – Inwersja słownika
# Masz słownik mapujący nazwy produktów na kategorie: {'laptop': 'elektronika', 'klawiatura': 'elektronika', 'krzesło': 'meble', 'biurko': 'meble'} . 
# Stwórz odwrotny słownik gdzie klucze to kategorie, a wartości to listy produktów.

# Wymagania:
#         Iteruj po oryginalnym słowniku
#         Zgrupuj produkty według kategorii
#         Wynik: {'elektronika': ['laptop', 'klawiatura'], 'meble': [...]}
        

# Oczekiwany wynik:
#     Słownik kategoria: lista_produktów

products = {
    'laptop': 'elektronika',
    'klawiatura': 'elektronika', 
    'krzesło': 'meble', 
    'biurko': 'meble'
    }

inverted = {}

for produkt, kategoria in products.items():
    if kategoria in inverted:
        inverted[kategoria].append(produkt)
    else:
        inverted[kategoria] = [produkt]
        print(inverted)
        
print(inverted)

#=================================
# Zadanie 11 – Dictionary comprehension - kwadraty liczb
# Stwórz słownik używając dictionary comprehension, gdzie klucze to liczby od 1 do 20, a
# wartości to ich kwadraty. Następnie przefiltruj ten słownik (też comprehension!) by zawierał
# tylko liczby parzyste.

# Wymagania:
#     Użyj dictionary comprehension 2 razy
#     Pierwszy słownik: wszystkie liczby 1-20
#     Drugi słownik: tylko parzyste klucze

# Oczekiwany wynik:
#     Dwa słowniki wypisane

# 1️⃣ Słownik: liczby 1–20 i ich kwadraty
squares = {x: x**2 for x in range(1, 21)}

# 2️⃣ Filtrowanie: tylko liczby parzyste
even_squares = {k: v for k, v in squares.items() if k % 2 == 0}

# Wynik
print("Wszystkie liczby:")
print(squares)

print("\nTylko liczby parzyste:")
print(even_squares)

# Zadanie 12 – Analiza transakcji - słowniki zagnieżdżone
# Masz listę transakcji (krotek): [('2024-01-15', 'Elektronika', 1200), ('2024-01-
# 16', 'Meble', 800), ('2024-01-15', 'Elektronika', 350), ...] . 

# Stwórz słownik gdzie kluczem jest data, a wartością słownik z sumą sprzedaży dla każdej kategorii tego dnia.
# Wymagania:
#     Zagnieżdżone słowniki: {data: {kategoria: suma}}
#     Iteruj po transakcjach i akumuluj sumy

# Oczekiwany wynik:
#     Słownik typu: {'2024-01-15': {'Elektronika': 1200, 'Meble': 450, ...}, ...}
    
transactions = [
    ('2024-01-15', 'Elektronika', 1200),
    ('2024-01-15', 'Meble', 450),
    ('2024-01-16', 'Elektronika', 800),
    ('2024-01-16', 'Elektronika', 350),
    ('2024-01-15', 'Odzież', 200),
    ('2024-01-16', 'Meble', 600)
]

summary = {}

# Agregacja
for date, category, amount in transactions:
    
    # Jeśli data nie istnieje → dodaj
    if date not in summary:
        summary[date] = {}
    
    # Jeśli kategoria nie istnieje dla tej daty → dodaj
    if category not in summary[date]:
        summary[date][category] = amount
    else:
        summary[date][category] += amount

# Wynik
print(summary)