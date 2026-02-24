import pandas as pd
import pyodbc
from config.db_config import CONN_STR


CSV_PATH = "data/processed/shopping_trends_clean.csv"
TABLE_NAME = "customer_shopping_trends"


def load_to_sqlserver():
    df = pd.read_csv(CSV_PATH)

    conn = pyodbc.connect(CONN_STR)
    cursor = conn.cursor()

    insert_sql = f"""
    INSERT INTO {TABLE_NAME} (
        customer_id,
        age,
        gender,
        item_purchased,
        category,
        purchase_amount_usd,
        location,
        size,
        color,
        season,
        review_rating,
        subscription_status,
        payment_method,
        shipping_type,
        discount_applied,
        promo_code_used,
        previous_purchases,
        preferred_payment_method,
        frequency_of_purchases
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    rows = df.itertuples(index=False, name=None)

    for row in rows:
        cursor.execute(insert_sql, row)

    conn.commit()
    conn.close()

    print("Insert dữ liệu từ shopping_trends_clean.csv thành công")