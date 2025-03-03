import pandas as pd
from sklearn.preprocessing import StandardScaler

train_df = pd.read_csv('train/train_data.csv')
test_df = pd.read_csv('test/test_data.csv')

scaler = StandardScaler()

for column in train_df.drop('target', axis=1).columns:
    train_df[column] = scaler.fit_transform(train_df[column].to_frame())
    test_df[column] = scaler.fit_transform(test_df[column].to_frame())

train_df.to_csv('train/train_data.csv', index=False)
test_df.to_csv('test/test_data.csv', index=False)