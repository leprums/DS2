from dotenv import load_dotenv
import os
import torch
import random
import json
from aiogram import Bot, Dispatcher, types, executor
from model import TinyNet, clean_text, bag_of_words

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

ckpt = torch.load('model.pth')

# Модель
model = TinyNet(ckpt['in_size'], ckpt['hidden_size'], ckpt['out_size'])
model.load_state_dict(ckpt['model_state'])
model.eval()

# Загружаем переменные из файла .env
load_dotenv()
# Достаем токен по имени ключа
API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я DS-помощник. Вот что я умею: \n- Подскажу команды Git\n- Разберусь с venv\n- Дам шорткаты VS Code\nПросто напиши свой вопрос!")

@dp.message_handler()
async def handle_message(msg: types.Message):
    # Кодируем входной текст
    sentence = clean_text(msg.text)
    X = bag_of_words(sentence, ckpt['all_words'])
    
    with torch.no_grad():
        output = model(X)
        probs = torch.softmax(output, dim=0) # Получаем вероятности
        prob, idx = torch.max(probs, dim=0)
        tag = ckpt['tags'][idx]

    # Если нейронка уверена больше чем на 60%
    if prob.item() > 0.6:
        for intent in config['intents']:
            if tag == intent['tag']:
                await msg.answer(random.choice(intent['responses']))
                return
    
    # Если не уверена
    await msg.answer(random.choice(config['fallback_responses']))

if __name__ == '__main__':
    executor.start_polling(dp)
    