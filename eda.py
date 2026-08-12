import pandas as pd
import matplotlib.pyplot as plt

def quick_summary(df):
    print(f"Shape: {df.shape}")
    print(f"Data types:\n{df.dtypes}")
    print(f"Null counts:\n{df.isnull().sum()}")
    print(f"Basic stats:\n{df.describe()}")

def missing_report(df):
    null_counts = df.isnull().sum()
    total = df.shape[0]
    null_percentage = (null_counts / total) * 100
    report = pd.DataFrame({
        'Null Count': null_counts,
        'Null Percentage': null_percentage
    })
    print(report)
    report['Null Percentage'].plot(kind='bar')
    plt.title('Null Value Analysis')
    plt.show()
