# etl/extract.py
import pandas as pd

RAW_PATH = "data/raw/shopping_trends_kaggle.csv"

def extract():
    df = pd.read_csv(RAW_PATH)
    print("Extract Done!")
    return df

if __name__ == "__main__":
    df = extract()
    print(df.head())