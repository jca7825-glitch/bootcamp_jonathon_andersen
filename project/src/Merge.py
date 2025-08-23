
import os, json, time, datetime as dt, csv, pathlib
import pandas as pd
import os,sys
from pathlib import Path
sys.path.append(os.path.abspath(".."))


def CSV_Merger(lst):
    merged_df = None
    dfs=[]
    for i in lst:
        path = Path('../data/raw') / f'{i}.csv'
        df = pd.read_csv(path)

        if merged_df is None:
            merged_df = df

        else:
            merged_df = pd.merge(merged_df, df, on="date", how="outer")

    return merged_df
        
    
    