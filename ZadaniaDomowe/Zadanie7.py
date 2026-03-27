# Zadanie 9 – Kategorie BMI dla listy pacjentów.oct
# Masz dane pacjentów: wagi = [70, 85, 62, 95, 78] (kg) i wzrosty = [1.75, 1.80,# 1.65, 1.78, 1.72] (m). 
# Oblicz BMI dla każdego i sklasyfikuj (niedowaga < 18.5, norma 18.5-24.9, nadwaga >= 25).


# Dataset:
#     Listy równoległe: wagi i wzrosty

# Wymagania:
#     Użyj pętli for i in range(len(wagi)):
#     Oblicz bmi = wagi[i] / (wzrosty[i] ** 2)
#     Sklasyfikuj używając if/elif/else
#     Wyświetl wyniki dla każdego pacjenta
    
# Oczekiwany rezultat:
#     5 linii z BMI i kategorią dla każdego pacjenta
    
wagi = [70, 85, 62, 95, 78]
wzrosty = [1.75, 1.80, 1.65, 1.78, 1.72]
print(range(len(wagi))) #range(0, 5)

for i in range(len(wagi)):
    bmi = wagi[i] / (wzrosty[i] ** 2)

    # Klasyfikacja
    if bmi < 18.5:
        kategoria = "Niedowaga"
    elif bmi < 25:
        kategoria = "Norma"
    else:
        kategoria = "Nadwaga"

    # Wynik dla pacjenta
    print(f"Pacjent {i+1}: BMI = {bmi:.2f}, {kategoria}")

#======================================================    
# Zad 10 - Znajdź wszystkie liczby pierwsze do 100
# Napisz program, który znajdzie wszystkie liczby pierwsze od 2 do 100 używając zagnieżdżonych pętli.

# Wymagania:
# Pętla zewnętrzna: for n in range(2, 101):
# Pętla wewnętrzna: sprawdź dzielniki od 2 do √n
# Zmienna czy_pierwsza = True
# Jeśli znajdziesz dzielnik, ustaw czy_pierwsza = False i użyj break
# Jeśli czy_pierwsza == True , dodaj do listy

# Oczekiwany rezultat:
# Lista liczb pierwszych: [2, 3, 5, 7, 11, 13, ..., 97]
# Liczba znalezionych: 25

import math
primes = []

for n in range(2, 101):
    czy_pierwsza = True

    # sprawdzamy dzielniki od 2 do sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            czy_pierwsza = False
            break

    if czy_pierwsza:
        primes.append(n)

# Wynik
print("Lista liczb pierwszych:", primes)
print("Liczba znalezionych:", len(primes))
    
print(range(2, int(math.sqrt(3)) + 1))
print(math.sqrt(3))


#------------------------------------------
#Zad 11
# Masz dane sprzedaży miesięcznej: [1200, 1350, 1290, 1480, 1520, 1510, 1680,1720, 1700, 1890, 1950, 2100] . 
# Zidentyfikuj miesiące, w których sprzedaż wzrosła w porównaniu do poprzedniego miesiąca.

# Dataset:
# Lista 12 wartości (sprzedaż miesięczna w PLN)

# Wymagania:
# Pętla for i in range(1, len(sprzedaz)):
# Porównaj sprzedaz[i] z sprzedaz[i-1]
# Oblicz zmianę procentową
# Wyświetl miesiące ze wzrostem

# Ocekiwany rezultat:
# Lista miesięcy ze wzrostem i procentowy przyrost

sprzedaz = [1200, 1350, 1290, 1480, 1520, 1510, 1680, 1720, 1700, 1890, 1950, 2100]
miesiace_wzrost = []

for i in range(1, len(sprzedaz)):
    poprzedni = sprzedaz[i - 1]
    obecny = sprzedaz[i]

    if obecny > poprzedni:
        zmiana_procent = ((obecny - poprzedni) / poprzedni) * 100
        miesiace_wzrost.append((i + 1, zmiana_procent))  # i+1 = numer miesiąca

print("Miesiące ze wzrostem:")
for miesiac, procent in miesiace_wzrost:
    print(f"Miesiąc {miesiac}: +{procent:.2f}%")