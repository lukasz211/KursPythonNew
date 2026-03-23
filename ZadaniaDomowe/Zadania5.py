#Praca domowa (lekcja 5) - zadanie 5, 8, 9, 10

# Zadanie 5 – Parsowanie CSV
# Masz string CSV: "Alice,28,Data Scientist,75000" . Użyj split(',') aby wyciągnąć:
#     Imię
#     Wiek (jako int)
#     Zawód
#     Pensję (jako int)
# Wyświetl te informacje w formacie: "Alice ma 28 lat, pracuje jako Data Scientist i# zarabia $75000"

csv = "Alice,28,Data Scientist,75000"

# Parsowanie CSV
parts = csv.split(",")
#------------------------
name = parts[0]
age = int(parts[1])
job = parts[2]
salary = int(parts[3])
#------------------------
print('='*62)
print(f"{name} ma {age} lat, pracuje jako {job} i zarabia ${salary}")
print('='*62)

#================================================
# Zadanie 8 – Ekstakcja informacji ze stringa
# Masz nazwę pliku: "model_results_2024_Q3.csv" . Wyciągnij rok i kwartał używając slicing lub split.

plik = "model_results_2024_Q3.csv"
parts = plik.split("_")
print(parts)
rok = parts[2]

kwartal = parts[3]
print(kwartal)
kwartal = parts[3].split(".")[0]  # usuwamy .csv

print('='*30)
print(f"Rok: {rok}")
print(f"Kwartał: {kwartal}")
print('='*30)

#===========================================
# Zadanie 9 – Filtrowanie outlierów
# Masz listę pomiarów: [23, 24, 22, 150, 23, 25, -10, 24, 23]. 
# Outlierem jest wartość poza zakresem [20, 30].
# Stwórz nową listę bez outlierów używając list comprehension

#List Comprehension

pomiary = [23, 24, 22, 150, 23, 25, -10, 24, 23]

# usuwanie outlierów (zakres 20–30)
nowy_pomiar = [x for x in pomiary if 20 <= x <= 30]

print(nowy_pomiar)

# nowy_pomiar2 = [x/3 for x in pomiary if 20 <= x <= 30]  #wynikowe 'x' podzielone przez 3
# print(nowy_pomiar2)

print('='*30)
# [x        for x in pomiary        if 20 <= x <= 30]
#  ↑                    ↑                    ↑
# co zrobić     skąd brać dane          warunek 

# nowy_pomiar2 = [x/3 for x in pomiary if 20 <= x <= 30]  # x podzielone przez 3
# print(nowy_pomiar2)

#===============================
#inaczej
# filtered = []
# for x in pomiary:
#     if 20 <= x <= 30:
#         filtered.append(x)
# print(f"Filtered=  {filtered}")


#===========================================================
# Zadanie 10 – Agregacja danych po kategoriach
# Masz listę transakcji (kategoria, kwota):
    
transactions = [
    ('food', 50),
    ('transport', 20),
    ('food', 30),
    ('entertainment', 40),
    ('transport', 15),
    ('food', 25)
] 
# Oblicz łączną kwotę dla każdej kategorii. Wynik zapisz w słowniku (użyj pętli i warunków).

# Słownik wynikowy
summary = {}
# count = 0

# Agregacja
for category, amount in transactions:
    if category in summary:
        summary[category] += amount
    else:
        summary[category] = amount
        #count += 1
    # print(summary)
    # print(count)

# Wynik
print(summary)
print('='*60)


"""
Kluczowe zasady Green IT dla kolekcji:
1. Używaj list comprehensions zamiast pętli for z append (szybsze i bardziej czytelne)

numbers = [1, 2, 3, 4, 5, 6]
even = [x for x in numbers if x % 2 == 0]
print(even)
[2, 4, 6]

2. Preferuj extend() i append() zamiast operatora + dla list
3. Używaj join() zamiast += przy budowaniu długich stringów
4. Unikaj niepotrzebnego kopiowania - modyfikuj in-place gdy to możliwe
5. Czyść duże struktury ( del , clear() ) gdy nie są już potrzebne
6. Używaj slicingu zamiast pętli do filtrowania danych

Success
Efektywny kod = mniej czasu obliczeń = mniej zużytej energii = mniejszy ślad węglowy. W
Data Science, gdzie przetwarzamy miliony rekordów, różnica między += a join() może
oszczędzić godziny czasu procesora!
"""