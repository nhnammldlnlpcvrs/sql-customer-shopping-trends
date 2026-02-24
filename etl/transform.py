# etl/transform.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd

RAW_PATH = "data/raw/shopping_trends.csv"
PROCESSED_PATH = "data/processed/shopping_trends_clean.csv"

def transform():
    df = pd.read_csv(RAW_PATH)

    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(usd)", "usd", regex=False)
        .str.replace("[()]", "", regex=True)
    )

    df["customer_id"] = df["customer_id"].astype(int)
    df["age"] = df["age"].astype(int)
    df["purchase_amount_usd"] = df["purchase_amount_usd"].astype(float)
    df["review_rating"] = df["review_rating"].astype(float)
    df["previous_purchases"] = df["previous_purchases"].astype(int)

    df = df.drop_duplicates().dropna()

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(PROCESSED_PATH, index=False)
    print("Transform xong dữ liệu")

if __name__ == "__main__":
    transform()