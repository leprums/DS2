import cv2
import numpy as np
from ultralytics import YOLO
import pygame
from collections import deque
import math

WIDTH, HEIGHT = 640, 480
TRAIL_LENGTH = 20
RIGHT_HAND_ID = 9
LEFT_HAND_ID = 10
CLAP_THRESHOLD = 100
FLASH_DURATION = 10

# Путь к дообученной модели
GESTURE_MODEL_PATH = r'runs/detect/runs/detect/train/weights/best.pt'

# Инициализация
pygame.mixer.init()
try:
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
except:
    print('Файл music.mp3 не найден')

# Загружаем обе модели
pose_model = YOLO('yolov8n-pose.pt') 
gesture_model = YOLO(GESTURE_MODEL_PATH) 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

right_trail = deque(maxlen=TRAIL_LENGTH)
left_trail = deque(maxlen=TRAIL_LENGTH)
flash_counter = 0
special_visual = False # Для эффекта "козы"

print('''Запуск! 
        Подними любую руку для увеличения громкости и опусти для уменьшения.
        Сожми любую руку в кулак ✊ для остановки звука.
        Разведи пальцы на руке широко 🖐️  для воспроизведения звука.        
        Покажи "козу" 🤘 для изменения настроения.        
        Хлопни в ладоши для вспышки.
        Нажми клавушу "Q" для выхода.''')

while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    frame = cv2.flip(frame, 1)

    # Сначала ищем позы (yolo)
    pose_results = pose_model(frame, verbose=False)
    
    # Затем ищем жесты (дообученная модель)
    gesture_results = gesture_model(frame, verbose=False, conf=0.6)
    
    current_gesture = None
    if len(gesture_results[0].boxes) > 0:
        class_id = int(gesture_results[0].boxes.cls[0])
        current_gesture = gesture_model.names[class_id]

    # --- ЛОГИКА ЖЕСТОВ ---
    if current_gesture == 'fist':
        # КУЛАК: пауза и чистим шлейфы
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        right_trail.clear()
        left_trail.clear()
        special_visual = False

    elif current_gesture == 'five':
        # ЛАДОНЬ: плэй
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        special_visual = False

    elif current_gesture == 'horns':
        # КОЗА: чистим шлейфы и включаем спецэффект
        right_trail.clear()
        left_trail.clear()
        special_visual = True

    # --- РАБОТА С ПОЗАМИ  ---
    rh_pos, lh_pos = None, None
    vol_right, vol_left = 0.0, 0.0

    if pose_results[0].keypoints is not None and len(pose_results[0].keypoints.xy) > 0:
        points = pose_results[0].keypoints.xy[0] 
        
        if len(points) > RIGHT_HAND_ID and points[RIGHT_HAND_ID][0] > 0:
            rh_pos = (int(points[RIGHT_HAND_ID][0]), int(points[RIGHT_HAND_ID][1]))
            # Рисуем шлейф только если нет "кулака" или "козы"
            if current_gesture not in ['fist', 'horns']:
                right_trail.append(rh_pos)
            vol_right = max(0.0, min(1.0, 1.0 - (rh_pos[1] / HEIGHT)))
        
        if len(points) > LEFT_HAND_ID and points[LEFT_HAND_ID][0] > 0:
            lh_pos = (int(points[LEFT_HAND_ID][0]), int(points[LEFT_HAND_ID][1]))
            if current_gesture not in ['fist', 'horns']:
                left_trail.append(lh_pos)
            vol_left = max(0.0, min(1.0, 1.0 - (lh_pos[1] / HEIGHT)))

    # Управление звуком
    pygame.mixer.music.set_volume(max(vol_right, vol_left))
    
    # Логика хлопка
    if rh_pos and lh_pos:
        dist = math.sqrt((rh_pos[0]-lh_pos[0])**2 + (rh_pos[1]-lh_pos[1])**2)
        if dist < CLAP_THRESHOLD and flash_counter == 0:
            flash_counter = FLASH_DURATION

    # --- ВИЗУАЛИЗАЦИЯ ---
    overlay = frame.copy()
    for trail, color in zip([right_trail, left_trail], [(255, 0, 255), (255, 255, 0)]):
        for i in range(1, len(trail)):
            thickness = int(np.sqrt(TRAIL_LENGTH / (i + 1)) * 8)
            cv2.line(overlay, trail[i-1], trail[i], color, thickness, cv2.LINE_AA)

    frame = cv2.addWeighted(overlay, 0.7, frame, 0.3, 0)

    # Доп. эффект для "козы" (красный фильтр)
    if special_visual:
        frame[:, :, 2] = cv2.add(frame[:, :, 2], 80)

    # Вспышка
    if flash_counter > 0:
        flash_layer = np.full((HEIGHT, WIDTH, 3), 255, dtype=np.uint8)
        alpha = flash_counter / FLASH_DURATION
        frame = cv2.addWeighted(flash_layer, alpha, frame, 1 - alpha, 0)
        flash_counter -= 1
    
    # Добавляем инфо на экран
    info_text = f'GESTURE: {current_gesture} | VOL: {int(pygame.mixer.music.get_volume()*100)}%'
    cv2.putText(frame, info_text, (20, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow('AI Generative Art v2.0', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()