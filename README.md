# Customer Shopping Trends  
**SQL Server – Python – ETL – Data Analysis & Visualization**

---

## Project Overview

This project implements a complete **data engineering and data analytics pipeline** using a real-world customer shopping dataset.

The workflow includes:
- Database schema design with SQL Server
- ETL pipeline using Python (Pandas + PyODBC)
- Loading cleaned data into SQL Server
- Exploratory Data Analysis (EDA) and data visualization
- SQL-based analytical queries

This project is suitable for:
- Database Management Systems (DBMS) coursework
- Data Analytics / Data Engineering portfolio
- Practicing SQL–Python integration in real scenarios

---

## Dataset

- Source: Kaggle – Customer Shopping Trends  
- File: `shopping_trends_clean.csv`

The dataset contains customer demographic information and shopping behavior such as purchase amount, category, payment method, and subscription status.

---

## Technologies Used

- Microsoft SQL Server
- Python 3
- pandas
- pyodbc
- matplotlib
- seaborn
- Jupyter Notebook

---

## Database Setup

Run the SQL script in SSMS:

```sql
CREATE DATABASE CustomerShopping;
GO

USE CustomerShopping;
GO

CREATE TABLE customer_shopping_trends (
    customer_id INT PRIMARY KEY,
    age INT,
    gender NVARCHAR(10),
    item_purchased NVARCHAR(50),
    category NVARCHAR(50),
    purchase_amount_usd INT,
    location NVARCHAR(50),
    size NVARCHAR(10),
    color NVARCHAR(30),
    season NVARCHAR(20),
    review_rating FLOAT,
    subscription_status NVARCHAR(10),
    payment_method NVARCHAR(50),
    shipping_type NVARCHAR(50),
    discount_applied NVARCHAR(10),
    promo_code_used NVARCHAR(10),
    previous_purchases INT,
    preferred_payment_method NVARCHAR(50),
    frequency_of_purchases NVARCHAR(30)
);
```

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Test database connection:

```bash
python test_db.py
```

Run ETL pipeline:

```bash
python main.py
```

---

## EDA & Visualization

Open Jupyter Notebook:

```bash
jupyter notebook notebooks/eda_customer_shopping.ipynb
```

The notebook includes:
- Data overview
- Distribution analysis
- Spending behavior visualization
- Subscription impact analysis

---

## Sample SQL Queries

```sql
SELECT category, AVG(purchase_amount_usd) AS avg_spending
FROM customer_shopping_trends
GROUP BY category;
```

---

## Outcome

This project demonstrates a complete workflow from raw data to database storage and analytical insights using SQL and Python.

---

## Author

Nam Nguyen  
SQL • Python • Data Analytics Project