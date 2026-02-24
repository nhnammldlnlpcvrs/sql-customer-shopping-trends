# main.py
from etl.transform import transform
from etl.load_to_sqlserver import load_to_sqlserver


def main():
    print("Bắt đầu ETL pipeline...")

    print("tep 1: Transform data")
    transform()

    print("Step 2: Load data vào SQL Server")
    load_to_sqlserver()

    print("ETL pipeline hoàn tất!")


if __name__ == "__main__":
    main()