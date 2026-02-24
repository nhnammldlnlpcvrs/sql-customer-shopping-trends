# etl/load_to_sqlserver.py
import pandas as pd
import pyodbc
from config.db_config import CONN_STR


def load_to_sqlserver():
    df = pd.read_csv("data/processed/shopping_trends_clean.csv")

    conn = pyodbc.connect(CONN_STR)
    cursor = conn.cursor()

    insert_sql = """
    INSERT INTO customer_shopping_trends (
        customer_id, age, gender, item_purchased, category,
        purchase_amount_usd, location, size, color, season,
        review_rating, subscription_status, payment_method,
        shipping_type, discount_applied, promo_code_used,
        previous_purchases, preferred_payment_method, frequency_of_purchases
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_sql, tuple(row))

    conn.commit()
    conn.close()

    print("Load dữ liệu thành công")