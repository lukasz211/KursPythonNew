#Zadanie 2
temp = [-5, 3, -2, 8, 12, -1, 6, 0, 15, -3]
suma = 0
licza_pomiarow = 0

for t in temp:
    if t > 0 :
        suma += t
        licza_pomiarow += 1

print(f"Suma dodatnich temperatur: {suma}")
print(f"Liczba dodatnich pomiarów: {licza_pomiarow}")

#-----------------
#Zadanie 3
# Napisz program, który wyświetli odliczanie od 20 do 0 z krokiem -2 (20, 18, 16, ..., 2, 0).
# Użyj pętli for i funkcji range() .

# Wymagania:
#     for i in range(20, -1, -2):
#     Wyświetl każdą liczbę

# Oczekiwany rezultat:
#     Lista liczb: 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0

#range(start, stop, step)
for i in range(20, -1, -2):
    print(i, end=' ')
    
#---------------------
Zad 4
