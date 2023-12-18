import pandas as pd
import numpy as np
import sqlite3

def load_data():
    conn = sqlite3.connect("bus_aug23.db")
    query = "SELECT * FROM vehicles;"
    df = pd.read_sql_query(query, conn)

    df = df[df['vid'].notnull()]

    numeric_cols = ['vid', 'lat', 'lon', 'hdg', 'pid', 'pdist', 'spd', 'tatripid']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    df['tmstmp'] = pd.to_datetime(df['tmstmp'])
    df = df.set_index(pd.DatetimeIndex(df['tmstmp']))

    return df
