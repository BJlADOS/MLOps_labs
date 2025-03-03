import pandas as pd
import os

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

X, y = make_regression(n_samples=15000, n_features=10, n_informative=3, n_targets=1)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

train_df = pd.DataFrame(X_train)
train_df['target'] = y_train

test_df = pd.DataFrame(X_test)
test_df['target'] = y_test

train_df.to_csv('train/train_data.csv', index=False)
test_df.to_csv('test/test_data.csv', index=False)