from sklearn import datasets
import pandas as pd
df = pd.DataFrame(datasets.fetch_california_housing())
print(df.head())