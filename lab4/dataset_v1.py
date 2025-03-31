from catboost.datasets import titanic

train, _ = titanic()
df = train[['Pclass', 'Sex', 'Age']].copy()
df.to_csv('titanic.csv', index=False)