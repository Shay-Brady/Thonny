import pandas as pd

df = pd.read_csv('summer.csv')

df[df["Country"] == 'USA']

print(df["Country"])