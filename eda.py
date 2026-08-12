import pandas as pd

def quick_summary(df):
    print(f"Shape: {df.shape}")
    print(f"Data types:\n{df.dtypes}")
    print(f"Null counts:\n{df.isnull().sum()}")
    print(f"Basic stats:\n{df.describe()}")