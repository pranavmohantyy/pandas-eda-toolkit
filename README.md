# pandas-eda-toolkit

This toolkit provides reusable data exploration and cleaning helpers built on pandas.

## Usage Example

Here's how to use the toolkit with the Titanic dataset:

```python
import pandas as pd
from cleaner import fill_nulls
from eda import quick_summary
from pipeline import Pipeline

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Quick summary of the data
quick_summary(df)

# Fill nulls in the 'Age' column using mean
df['Age'] = fill_nulls(df['Age'], strategy='mean')

# Create a pipeline object
pipeline = Pipeline(df)

# Fill nulls with forward fill strategy
pipeline.fill_nulls('forward-fill')

# Print the updated summary
quick_summary(pipeline.df)
```
