import pandas as pd

def split_vehicles(df):
    return [group[1] for group in df.groupby('vid')]
