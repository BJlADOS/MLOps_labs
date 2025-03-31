import pandas as pd

df = pd.read_csv('titanic.csv')
sex_encoded = pd.get_dummies(df['Sex'], prefix='Sex')
df = pd.concat([df, sex_encoded], axis=1)
df.to_csv('titanic.csv', index=False)