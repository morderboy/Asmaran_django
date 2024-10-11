# Используем официальный образ Python 3.12
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY req.txt /app/

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r req.txt

# Копируем все файлы вашего проекта в контейнер
COPY . /app/

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Применяем миграции базы данных
RUN python manage.py migrate

# Запуск сервера Django
CMD ["gunicorn", "--workers", "6", "--bind", "0.0.0.0:8000", "Asmaran_django.wsgi:application"]

# Открываем порт 8000
EXPOSE 8000
