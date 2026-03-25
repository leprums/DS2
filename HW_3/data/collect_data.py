import cv2
import os
import time

# --- НАСТРОЙКИ ---
# Имя жеста, который снимаю
GESTURE_NAME = 'five' 
SAVE_PATH = f'images/{GESTURE_NAME}'
COUNT_TO_COLLECT = 10 # Сколько фото сделать за один раз
WIDTH, HEIGHT = 640, 480

# Создаем папку, если её нет
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

cap = cv2.VideoCapture(0) # 1 для внешней камеры 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)


print(f'Готовимся собирать жесты для: {GESTURE_NAME}')
print('У тебя есть 5 секунд, чтобы подготовиться...')
time.sleep(5)

count = 0
while count < COUNT_TO_COLLECT:
    ret, frame = cap.read()
    time.sleep(3)
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    
    # Генерируем уникальное имя файла
    img_name = os.path.join(SAVE_PATH, f'{GESTURE_NAME}_{int(time.time()*100)}.jpg')
    
    # Сохраняем фото
    cv2.imwrite(img_name, frame)
    count += 1
    
    # Выводим инфо на экран
    display_frame = frame.copy()
    cv2.putText(display_frame, f'Collected: {count}/{COUNT_TO_COLLECT}', (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Data Collection', display_frame)

    # Небольшая пауза, чтобы ты успевала менять положение руки
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

print(f'Готово! Фото сохранены в {SAVE_PATH}')
cap.release()
cv2.destroyAllWindows()