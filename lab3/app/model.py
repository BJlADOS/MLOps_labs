import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Загружаем данные
iris = load_iris()
X, y = iris.data, iris.target

# Обучаем модель
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Сохраняем модель
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

def predict(features):
    """Загружает модель и делает предсказание."""
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model.predict([features]).tolist()
