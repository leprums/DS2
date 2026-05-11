import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import sys

def prepare_data(input_path='data/raw/reagents_raw.xlsx', output_dir='data/processed'):
    
    output_csv = os.path.join(output_dir, 'clean_reagents.csv')
    output_npy = os.path.join(output_dir, 'reagents_embeddings.npy')

    print("--- Старт обработки данных ---")

    # Проверка существования входного файла
    if not os.path.exists(input_path):
        print(f"❌ КРИТИЧЕСКАЯ ОШИБКА: Файл не найден по пути {input_path}")
        print("Проверьте, лежит ли исходный Excel в папке data/raw/")
        return

    # Проверка и создание папки для результатов
    if not os.path.exists(output_dir):
        print(f"📂 Папка {output_dir} не найдена. Создаю...")
        os.makedirs(output_dir, exist_ok=True)
    else:
        print(f"✅ Папка {output_dir} обнаружена.")

    # Загрузка данных
    try:
        df = pd.read_excel(input_path)
        print(f"📊 Данные успешно загружены. Строк: {len(df)}")
    except Exception as e:
        print(f"❌ Ошибка при чтении Excel: {e}")
        return

    # Формирование пассажей
    df = df.fillna('')
    def create_passage(row):
        parts = [
            f"название: {row['название']}",
            f"формула: {row['формула']}",
            f"синонимы: {row.get('синонимы', '')}"
        ]
        return "passage: " + " | ".join([p for p in parts if p])

    df['passage'] = df.apply(create_passage, axis=1)

    # Путь к папке с моделью
    model_name = 'intfloat/multilingual-e5-small'
    base_model_path = 'models'

    # Проверяем, существует ли папка models, если нет — создаем
    if not os.path.exists(base_model_path):
        print(f"📂 Папка {base_model_path} не найдена. Создаю...")
        os.makedirs(base_model_path, exist_ok=True)

    print(f"🧠 Подключение модели {model_name}...")
    try:
        # cache_folder заставляет SentenceTransformer искать/скачивать модель
        model = SentenceTransformer(model_name, cache_folder=base_model_path)
        
        # Выводим путь, куда сохранена модель
        print(f"✅ Модель готова: {os.path.abspath(base_model_path)}")
        
    except Exception as e:
        print(f"❌ Не удалось инициализировать нейросеть: {e}")
        return

    # Генерация и сохранение
    print("🏗️ Генерация векторов (эмбеддингов)...")
    embeddings = model.encode(df['passage'].tolist(), show_progress_bar=True)

    # Сохраняем всё
    df.to_csv(output_csv, index=False, encoding='utf-8')
    np.save(output_npy, embeddings)

    print(f"\n Готово! Файлы созданы:")
    print(f"   - {output_csv}")
    print(f"   - {output_npy}")

if __name__ == "__main__":
    prepare_data()
    