
from sklearn.datasets import load_iris
# Wczytanie Iris dataset
iris = load_iris()
X = iris.data # Macierz cech (150, 4)
y = iris.target # Wektor etykiet (150,)
print("Kształt macierzy cech:", X.shape) # 150 obserwacji,

