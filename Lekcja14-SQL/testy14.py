import sqlite3
import pandas as pd
conn = sqlite3.connect(':memory:')

# Tabela klientów
customers = pd.DataFrame({
'customer_id': [1, 2, 3, 4],
'name': ['Jan Kowalski', 'Anna Nowak', 'Piotr Wiśniewski', 'Maria Zając'],
'city': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław']
})

# Tabela zamówień
orders = pd.DataFrame({
'order_id': [101, 102, 103, 104, 105],
'customer_id': [1, 2, 1, 3, 1],
'order_date': ['2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14'],
'total_amount': [250.0, 120.5, 340.0, 80.0, 190.0]
})
customers.to_sql('customers', conn, index=False)
orders.to_sql('orders', conn, index=False)

# INNER JOIN – tylko klienci którzy złożyli zamówienie
query = """
SELECT c.customer_id, c.name, c.city, o.order_id, o.order_date, o.total_amount 
FROM customers c 
INNER JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_id, o.order_date
"""
result = pd.read_sql_query(query, conn)
print("INNER JOIN - klienci z zamówieniami:")
print(result)

# Podsumowanie zamówień na klienta
query2 = """
SELECT c.name, COUNT(o.order_id) AS number_of_orders, SUM(o.total_amount) AS total_spent 
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
"""
print("\nPodsumowanie zamówień:")
print(pd.read_sql_query(query2, conn))
conn.close()
