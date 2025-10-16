import pandas as pd

ruta = 'https://raw.githubusercontent.com/Mriano29/CEIABD-class-codes/refs/heads/main/california_housing_train.csv'
df = pd.read_csv(ruta)

print(df.head())