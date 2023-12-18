import pandas as pd

def get_speeds(df, time_start, time_end):
    selected_data = df.between_time(time_start, time_end).loc[df.index.dayofweek < 5]
    return selected_data.groupby('vid')['spd'].mean()
