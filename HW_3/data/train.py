from ultralytics import YOLO
import os

# Указываем путь к файлу конфигурации
DATA_CONFIG = os.path.abspath('data.yaml')

# Логика выбора модели (новая или продолжение обучения)
checkpoint_path = 'runs/detect/train/weights/last.pt'

if os.path.exists(checkpoint_path):
    print(f'--- Найдена точка сохранения: {checkpoint_path}. Продолжаем... ---')
    model = YOLO(checkpoint_path)
else:
    print('--- Начинаем новое обучение (базовая модель YOLOv8n) ---')
    model = YOLO('yolov8n.pt')

# Запуск обучения с параметрами
if os.path.exists(DATA_CONFIG):
    print(f'--- Используем файл конфигурации: {DATA_CONFIG} ---')
    results = model.train(
        data=DATA_CONFIG, # Путь к данным
        epochs=30, # Сколько раз прогнать датасет
        imgsz=640, # Размер картинки
        patience=10, # Early Stopping: если 10 эпох ошибка не падает, обучение остановится
        save=True, # Сохранять промежуточные результаты
        device='cpu', # Если есть видеокарта NVIDIA, поменять на 0
        project='runs/detect', # Папка для логов
        name='train', # Имя сессии
        exist_ok=True, # Не создавать новую папку при каждом запуске
        plots=True, # Рисовать графики точности (mAP) и ошибки (Loss)
        verbose=True # Показывать детальный прогресс каждой эпохи
    )
    print('--- Обучение завершено! ---')
else:
    print(f'Ошибка: Файл {DATA_CONFIG} не найден.')
