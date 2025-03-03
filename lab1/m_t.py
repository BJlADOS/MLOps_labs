import pandas as pd
import pickle
from sklearn.metrics import r2_score

test_df = pd.read_csv('test/test_data.csv')
X_test = test_df.drop('target', axis=1)
y_test = test_df['target']

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"Model test R² score is: {r2:.3f}")