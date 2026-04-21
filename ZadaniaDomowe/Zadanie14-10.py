import sqlite3
import pandas as pd
conn = sqlite3.connect(':memory:')
# Tabela sprzedaży
sales = pd.DataFrame({
'sale_id': range(1, 11),
'product': ['Laptop', 'Laptop', 'Mysz', 'Klawiatura', 'Monitor','Laptop', 'Mysz', 'Monitor', 'Słuchawki', 'Klawiatura'],
'category': ['Elektronika', 'Elektronika', 'Akcesoria', 'Akcesoria','Elektronika', 'Elektronika', 'Akcesoria', 'Elektronika', 'Akcesoria','Akcesoria'],
'quantity': [1, 2, 5, 3, 1, 1, 10, 2, 4, 2],
'revenue': [3500, 7000, 250, 600, 1200, 3500, 500, 2400, 600, 400]
})
sales.to_sql('sales', conn, index=False)
#Pogrupuj według kategorii | Użyj HAVING aby znaleźć tylko kategorie z przychodem > 1000 PLN | Oblicz liczbę transakcji, łączny przychód i średnią dla każdej kategorii
#Posortuj według łącznego przychodu
query = """
SELECT
  category,
  COUNT(*) AS num_sales,
  SUM(revenue) AS total_revenue,
  AVG(revenue) AS avg_revenue
FROM sales
GROUP BY category
HAVING SUM(revenue) > 1000
ORDER BY total_revenue DESC;
"""
#print("Produkty z przychodem > 1000:")
print(pd.read_sql_query(query, conn))


# # HAVING z wieloma warunkami
# query2 = """
# SELECT product, COUNT(*) AS sales_count,
# AVG(revenue) AS avg_revenue
# FROM sales
# GROUP BY product
# HAVING COUNT(*) >= 3 AND AVG(revenue) > 500
# ORDER BY avg_revenue DESC
# """
# print("\n>= 3 sprzedaży i średnia > 500:")
# print(pd.read_sql_query(query2, conn))
conn.close()