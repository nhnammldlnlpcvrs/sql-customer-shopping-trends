# config/db_config.py

SERVER = "localhost"
DATABASE = "CustomerShopping"
DRIVER = "ODBC Driver 17 for SQL Server"

CONN_STR = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=CustomerShopping;"
    "Trusted_Connection=yes;"
)