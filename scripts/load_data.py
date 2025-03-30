import psycopg2
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.postgres_config import POSTGRES_CONFIG

tables = ['users']
conn = psycopg2.connect(**POSTGRES_CONFIG)
cur = conn.cursor()

for table in tables:

    file_path = f'./data/{table}.csv'
    df = pd.read_csv(file_path)

    cols = ','.join(df.columns)
    placeholders = ','.join(["%s"]*len(df.columns))
    query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"

    for _, row in df.iterrows():
        cur.execute(query, tuple(row))
    
    print(f'Data loaded  into {table}')

conn.commit()
cur.close()
conn.close()
print("🎉 All data loaded successfully!")
