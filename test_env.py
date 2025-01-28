import dash
import pandas as pd
import os

# Load data
files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']

dfs = [pd.read_csv(file) for file in files]

after_operated_df = []

for df in dfs:
    df = df.copy()

    df = df[df['product'] == 'pink morsel']

    df['price'] = df['price'].str.replace('$', '').astype(float)

    df['sales'] = df['price'] * df['quantity']

    df = df[['sales','date', 'region']]

    after_operated_df.append(df)

final_df = pd.concat(after_operated_df)

final_df.to_csv('data/final_df.csv', index=False)