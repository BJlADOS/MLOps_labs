# Базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY app/ app/
COPY app/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r app/requirements.txt

# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]