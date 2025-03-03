import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

train_df = pd.read_csv('train/train_data.csv')
X_train = train_df.drop('target', axis=1)
y_train = train_df['target']

model = LinearRegression()
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)