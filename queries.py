import sqlite3
import pandas as pd

conn = sqlite3.connect("shop.db")

# Query 1: number of orders per payment method
q1 = """
SELECT payment_method, COUNT(*) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC
"""

# Query 2: top 5 products by revenue (joins 2 tables)
q2 = """
SELECT p.product_name,
       SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 5
"""

# Query 3: revenue per city (joins 3 tables)
q3 = """
SELECT c.city,
       SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.city
ORDER BY revenue DESC
"""

print("Orders per payment method:")
print(pd.read_sql(q1, conn))
print()
print("Top 5 products by revenue:")
print(pd.read_sql(q2, conn))
print()
print("Revenue per city:")
print(pd.read_sql(q3, conn))

conn.close()
