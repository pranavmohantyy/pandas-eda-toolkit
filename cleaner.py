import pandas as pd

def fill_nulls(df, strategy):
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'forward-fill':
        return df.fillna(method='ffill')
    elif strategy == 'zero':
        return df.fillna(0)
    else:
        raise ValueError("Invalid strategy")
