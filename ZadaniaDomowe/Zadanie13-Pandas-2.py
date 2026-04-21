# Zadanie 10 – Custom Funkcja Agregująca
# from sklearn.datasets import fetch_california_housing
# Napisz własną funkcję, która oblicza zakres międzykwartylowy (IQR = Q3 - Q1) 
# i zastosuj ją do grupy.
# Dataset: California Housing

# Wymagania:
# 	Napisz funkcję iqr_func(x) obliczającą IQR
# 	Zastosuj ją do MedHouseVal według regionów
# 	Porównaj IQR między regionami

# Oczekiwany rezultat:
# 	Tabela z IQR dla każdego regionu

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
df = data.frame

def iqr_func(x):
    x = x.dropna()                  # usuń NaN
    q1 = np.percentile(x, 25)
    q3 = np.percentile(x, 75)
    return q3 - q1

n_regions = 6
df['Region'] = pd.cut(df['Latitude'], bins=n_regions, labels=[f"Region_{i+1}" for i in range(n_regions)])

# jawnie ustaw observed, i sortuj po kolumnie 'IQR'
iqr_by_region = df.groupby('Region', observed=False)['MedHouseVal'].agg(IQR=iqr_func)
print(iqr_by_region.sort_values(by='IQR', ascending=False))
