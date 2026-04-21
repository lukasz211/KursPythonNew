# Znajdź pasażerów 1 klasy, kobiety, które przeżyły
# Oblicz średni wiek i średnią cenę biletu dla tej grupy
# Porównaj z mężczyznami z 3 klasy którzy nie przeżyli
# Stwórz wykres porównawczy (barplot)

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect(':memory:')
titanic = pd.DataFrame({
  'passenger_id': [1, 2, 3, 4, 5, 6, 7, 8],
  'name': ['Braund', 'Cumings', 'Heikkinen', 'Futrelle', 'Allen', 'Moran', 'McCarthy', 'Palsson'],
  'age': [22, 38, 26, 35, 35, None, 54, 2],
  'sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'male'],
  'survived': [0, 1, 1, 1, 0, 0, 0, 0],
  'pclass': [3, 1, 3, 1, 3, 3, 1, 3],
  'fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 21.08]
})

titanic.to_sql('titanic', conn, index=False)

# 1) Pasażerki 1 klasa - Survived
query_female = """
SELECT passenger_id, name, age, sex, survived, pclass, fare
FROM titanic
WHERE pclass = 1 AND sex = 'female' AND survived = 1;
"""
df_female = pd.read_sql_query(query_female, conn)
print("Kobiety które ocalały z 1 Klasy:\n", df_female, "\n")

# 2) Oblicz średni wiek i średnią cenę biletu dla tej grupy
mean_age_f = df_female['age'].mean()
mean_fare_f = df_female['fare'].mean()
print(f"Kobiety (1 klasa, ocalone) - Średnia wieku: {mean_age_f:.2f}, Średnia cena biletu: {mean_fare_f:.2f}\n")

# 3) Mężczyźni 3 klasa - Not Survived
query_male = """
SELECT passenger_id, name, age, sex, survived, pclass, fare
FROM titanic
WHERE pclass = 3 AND sex = 'male' AND survived = 0;
"""
df_male = pd.read_sql_query(query_male, conn)
print("3 Klasa Mężczyźni którzy nie przeżyli :\n", df_male, "\n")

mean_age_male = df_male['age'].mean()
mean_fare_male = df_male['fare'].mean()
print(f"Mężczyźni (3 Klasa, NOT survived) - mean age: {mean_age_male:.2f}, mean fare: {mean_fare_male:.2f}\n")

# 4) Wykres porównawczy (barplot) - porównanie mean age i mean fare
metrics = ['Średnia wieku', 'Średnia cena biletu']
group1 = [mean_age_f if not np.isnan(mean_age_f) else 0, mean_fare_f]
group2 = [mean_age_male if not np.isnan(mean_age_male) else 0, mean_fare_male]

x = np.arange(len(metrics))
width = 0.25

fig, ax1 = plt.subplots(figsize=(6,4))
ax1.bar(x - width/2, group1, width, label='Kobiety Klasa1 - Survived', color='C0')
ax1.bar(x + width/2, group2, width, label='Mężczyźni Klasa3 - Not Survived', color='C1')

ax1.set_xticks(x)
ax1.set_xticklabels(metrics)
ax1.set_ylabel('Wartość')
ax1.set_title('Porównanie: średni wiek i średnia cena biletu')
ax1.legend()
plt.tight_layout()
plt.show()
