# Берем официальный легкий образ Python
FROM python:3.11.8-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем список зависимостей
COPY requirements.txt .

# Устанавливаем библиотеки (без кэша)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект (папку src, данные, интенты)
COPY . .

# Команда для запуска бота
CMD sh -c "python -m src.data_processor && python -m src.bot"