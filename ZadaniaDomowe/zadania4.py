# zad 1
# Pobranie danych od użytkownika
# waga = float(input("Podaj wagę w kg: "))
# wzrost = float(input("Podaj wzrost w metrach (np. 1.75): "))

# bmi = waga/ (wzrost ** 2)   

# # Interpretacja BMI
# if bmi < 18.5:
#     interpretacja = "Niedowaga"
# elif bmi < 25:
#     interpretacja = "Norma"
# else:
#     interpretacja = "Nadwaga"

# # Wyświetlenie wyniku
# print(f"BMI: {bmi:.2f}")
# print(f"Interpretacja: {interpretacja}")

##########
#Zad 2
# celsius = 23.5

# # Konwersje
# fahrenheit = celsius * 9/5 + 32
# kelvin = celsius + 273.15

# # Wyświetlenie wyniku
# print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F = {kelvin:.1f} K")
#########################
#Zad 3
# Dane
# total_samples = 1000

# # Proporcje
# train_ratio = 70
# val_ratio = 15
# test_ratio = 15

# # Obliczenia z użyciem dzielenia całkowitego
# train_size = total_samples * train_ratio // 100
# val_size = total_samples * val_ratio // 100

# # Reszta trafia do zbioru testowego
# test_size = total_samples - train_size - val_size

# Wynik
# print("Zbiór treningowy:", train_size)
# print("Zbiór walidacyjny:", val_size)
# print("Zbiór testowy:", test_size)
# print("Suma:", train_size + val_size + test_size)

###############################
# Zad 4
print(" ---------- Zadanie 4 -----------------------")
# Ustandaryzuj nazwę kolumny z datasetu.
# Dane:
# Nazwa raw: " PATIENT_age_YEARS "

# Wymagania:
# Usuń białe znaki
# Zamień na małe litery
# Zastąp _ przez " "
# Użyj title case

# Oczekiwany rezultat:
# Patient Age Years

# Dane wejściowe
raw_name = " PATIENT_age_YEARS "

# Standaryzacja nazwy
clean_name1 = raw_name.strip()      # usuń białe znaki z początku i końca
clean_name2 = clean_name1.lower()    # zamień na małe litery
clean_name3 = clean_name2.replace("_", " ")  # zamień _ na spację
clean_name4 = clean_name3.title()    # title case

#Wynik
print("clean_name1 -> " + clean_name1)
print("clean_name2 -> " + clean_name2)
print("clean_name3 -> " + clean_name3)
print("clean_name4 -> " + clean_name4)

print(" ")
print(" ---------- Zadanie 6 -----------------------")
#Zadanie 6 – Dokładność w procentach
#Sformatuj metryki modelu.
#Dane:
accuracy    =   0.9234
precision   =   0.8891
recall      =   0.9456

raport_fstring = f"Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall:{recall:.2f}"
print(raport_fstring)

print(f"""
{'='*30}
RAPORT - Zad. 6
{'='*30}
Accuracy: {accuracy:.2%}
Precision: {precision:.4f}
Recall: {recall:.4f}
{'='*30}
""")
#-------------------------------------
print(" ---------- Zadanie 9 – Normalizacja Min-Max ----------------")

value = 75
mix_in_column = 50
max_in_column = 100
pipe = "|"

#pattern
normalized = (value - mix_in_column) / (max_in_column - mix_in_column)
headers = ['value', '|' , 'normalized' ]
print(f"{headers[0]:<5} {headers[1]:^5} {headers[2]:>5}")
print(f"{value:<5} {pipe:^5} {normalized:>5}")

#git remote show -n origin