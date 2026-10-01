# E-commerce Data Cleaning & SQL Project

A small data engineering project: take a messy raw CSV of online-shop orders, clean it with Python (Pandas), split it into related tables, store them in a SQLite database, and answer business questions with SQL.

> **Note:** `raw_orders.csv` is a **synthetic practice dataset** (512 rows) created for this project, with real-world problems added on purpose (duplicates, missing values, inconsistent text and dates).

## Tech Stack
- **Python**
- **Pandas** (cleaning & transformation)
- **SQLite3** (storage)
- **SQL** (analysis with GROUP BY and JOINs)

## Project Structure
| File | Purpose |
|---|---|
| `raw_orders.csv` | Raw, messy input data |
| `explore.py` | First look at the data (missing values, duplicates) |
| `clean.py` | Cleaning + splitting into tables + saving to `shop.db` |
| `queries.py` | SQL queries that answer business questions |

## What the Cleaning Step Does
- Removes 12 duplicate rows
- Standardizes city and customer names (21 spellings of city names became 8 real cities)
- Converts the price column from text (e.g. `95 EGP`) to numbers
- Removes orders with missing or negative quantities
- Fills missing payment methods with `Unknown`
- Unifies two different date formats into one

## Database Design
The flat file is split into 3 related tables so nothing is repeated:
- `customers` (customer_id, customer_name, customer_email, city)
- `products` (product_id, product_name, category, price)
- `orders` (order_id, order_date, customer_id, product_id, quantity, payment_method)

## How to Run
```bash
pip install -r requirements.txt
python clean.py
python queries.py
```

## Example Results
**Top products by revenue**
| product_name | revenue |
|---|---|
| Mechanical Keyboard | 162000 |
| Bluetooth Speaker | 70500 |
| Backpack | 66000 |
| Desk Lamp | 42560 |
| Laptop Stand | 42420 |

**Revenue by city**
| city | revenue |
|---|---|
| Cairo | 142435 |
| Alexandria | 97420 |
| Giza | 71640 |
| Mansoura | 68100 |
| Tanta | 46590 |
| Luxor | 27610 |
| Zagazig | 24010 |
| Aswan | 19235 |

## Possible Next Steps
- Add monthly revenue analysis
- Add data quality checks before saving
- Build a dashboard on top of the database
