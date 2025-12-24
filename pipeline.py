import sqlite3
import pandas as pd

def extract():
    source_conn = sqlite3.connect("source.db")
    query = "SELECT * FROM users"
    df = pd.read_sql_query(query, source_conn)
    source_conn.close()
    return df

def transform(df):
    df = df.drop_duplicates()
    df["age"] = df["age"].fillna(df["age"].mean())
    df["age_group"] = df["age"].apply(lambda x: "young" if x < 25 else "adult")
    return df

def load(df):
    target_conn = sqlite3.connect("target.db")
    df.to_sql("users cleaned", target_conn, if_exists= "replace", index= False)
    target_conn.close()

def run_etl():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL pipeline completed successfully")

if __name__ == "__main__" :
    run_etl()

    