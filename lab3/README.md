# Практика по MLops команда №14 lab№3

## Iris Prediction API

Веб-сервис на FastAPI для предсказания класса цветка Iris с использованием модели машинного обучения (RandomForestClassifier из scikit-learn).

## Структура проекта
```
lab3/
│── app/
│   │── model.py         # Код модели машинного обучения
│   │── main.py          # API на FastAPI
│   │── requirements.txt # Зависимости проекта
│── Dockerfile           # Инструкция для сборки Docker-образа
│── docker-compose.yml   # Конфигурация docker-compose
│── .dockerignore        # Исключения для Docker-контейнера
```
## Запуск через Docker
Соберать образ:
```bash
docker build -t iris-api:latest .
```
Запустить контейнер:
```bash
docker run -d -p 8000:8000 iris-api
```
API доступно по адресу: `http://localhost:8000/docs`


## Использование docker-compose
Запустить сервис:
```bash
docker-compose up -d
```
API доступно по адресу: `http://localhost:8000/docs`



