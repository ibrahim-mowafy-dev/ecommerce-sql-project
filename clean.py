import pandas as pd

df = pd.read_csv("raw_orders.csv")
print("Before:", len(df))

df = df.drop_duplicates()

print("Cities before:", df["city"].nunique())

df["city"] = df["city"].str.strip().str.title()
df["customer_name"] = df["customer_name"].str.strip().str.title()

print("Cities after:", df["city"].nunique())
df["price"] = df["price"].astype(str).str.replace("EGP", "").str.strip()
df["price"] = pd.to_numeric(df["price"])

print(df["price"].dtype)

print("Rows before quantity fix:", len(df))

df = df[df["quantity"] > 0]
df["quantity"] = df["quantity"].astype(int)

print("Rows after quantity fix:", len(df))
print("Missing payment before:", df["payment_method"].isnull().sum())

df["payment_method"] = df["payment_method"].fillna("Unknown")

print("Missing payment after:", df["payment_method"].isnull().sum())
d1 = pd.to_datetime(df["order_date"], format="%Y-%m-%d", errors="coerce")
d2 = pd.to_datetime(df["order_date"], format="%d/%m/%Y", errors="coerce")
df["order_date"] = d1.fillna(d2)

print("Bad dates:", df["order_date"].isnull().sum())
print(df["order_date"].dtype)
customers = (
    df.groupby("customer_name")
    .agg(customer_email=("customer_email", "first"), city=("city", "first"))
    .reset_index()
)
customers["customer_id"] = customers.index + 1

print(len(customers))
print(customers.head())
products = (
    df.groupby("product_name")
    .agg(category=("category", "first"), price=("price", "first"))
    .reset_index()
)
products["product_id"] = products.index + 1

print(len(products))
print(products.head())
orders = df.merge(customers[["customer_name", "customer_id"]], on="customer_name")
orders = orders.merge(products[["product_name", "product_id"]], on="product_name")

orders = orders[["order_id", "order_date", "customer_id", "product_id", "quantity", "payment_method"]]

print(len(orders))
print(orders.head())
import sqlite3

conn = sqlite3.connect("shop.db")

customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)

conn.close()
print("Saved 3 tables to shop.db")