import pyodbc
from config.db_config import CONN_STR

try:
    conn = pyodbc.connect(CONN_STR)
    print("Kết nối SQL Server OK")
    conn.close()
except Exception as e:
    print("Lỗi kết nối:")
    print(e)