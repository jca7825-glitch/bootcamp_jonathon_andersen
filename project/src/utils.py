import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Summary_Data(df):
    numeric_cols = df.select_dtypes(include='number').columns

    mean = df.groupby('category')[numeric_cols].mean().reset_index()

    std = df.groupby('category')[numeric_cols].std().reset_index()

    mean = mean.rename(columns={col: f"{col}_mean" for col in numeric_cols})
    std = std.rename(columns={col: f"{col}_std" for col in numeric_cols})

    summary =pd.merge(mean,std, on='category')
    return summary
    

    