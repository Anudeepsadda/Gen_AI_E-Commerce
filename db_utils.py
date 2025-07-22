import sqlite3
import pandas as pd

def query_db(sql_query: str) -> pd.DataFrame:
    try:
        conn = sqlite3.connect("ecommerce_data.db")
        df = pd.read_sql(sql_query, conn)
        conn.close()
        return df
    except Exception as e:
        return pd.DataFrame([{"error": str(e)}])
