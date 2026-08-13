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


def normalize(df, columns, method):
    if method == 'min-max':
        return (df[columns] - df[columns].min()) / (df[columns].max() - df[columns].min())
    elif method == 'z-score':
        return (df[columns] - df[columns].mean()) / df[columns].std()
    else:
        raise ValueError("Invalid method")


def encode_categoricals(df, columns, method):
    if method == 'label':
        for col in columns:
            df[col] = df[col].astype('category').cat.codes
    elif method == 'one-hot':
        df = pd.get_dummies(df, columns=columns, drop_first=True)
    else:
        raise ValueError("Invalid encoding method")
    return df