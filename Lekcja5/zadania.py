#print("test")


# data = [5,7,8,9,5,88,99,77]
# train = data[:5]

# data.reverse()
# #data.sort(reverse=True)
# #print(data)


# predictions = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat', 'dog', 'cat','bird']
# # Operator 'in' - sprawdzenie czy element istnieje
# if 'cat' in predictions:
#  print("Model przewidział przynajmniej jednego kota")

# accuracy_scores = [0.72, 0.68, 0.75, 0.81, 0.79]

# # Zmiana fragmentu listy
# accuracy_scores[2:4] = [0.76, 0.82] # Aktualizacja wyników 3 i 4
# print(f"Po aktualizacji: {accuracy_scores}")
# Usunięcie elementu przez del
# del accuracy_scores[0] # Usunięcie pierwszego (najgorszego) wyniku
# print(f"Po usunięciu pierwszego: {accuracy_scores}")

# insert() - wstawia element na konkretnej pozycji
features = ['wiek', 'dochod', 'wyksztalcenie']
features.insert(1, 'plec') # Wstawienie 'plec' na pozycję 1
print(f"Po insert: {features}")

# Operator + do konkatenacji (tworzy NOWĄ listę)
all_features = features + ['miasto', 'zawod']
print(f"Wszystkie cechy: {all_features}")
print(f"Oryginalna lista features: {features}") # Niezmieniona!


