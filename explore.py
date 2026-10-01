import pandas as pd

df = pd.read_csv("raw_orders.csv")
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())