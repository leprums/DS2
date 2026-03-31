import torch
import json
import random
from model import TinyNet, clean_text, bag_of_words

# Загружаем конфиг
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

ckpt = torch.load('model.pth', map_location='cpu')
words = ckpt['all_words']
tags = ckpt['tags']

# Модель
model = TinyNet(ckpt['in_size'], ckpt['hidden_size'], ckpt['out_size'])
model.load_state_dict(ckpt['model_state'])
model.eval()

print('🤖  Бот-тестер запущен! Пиши что-нибудь (для выхода нажми Ctrl+C):\n')

while True:
    sentence = input('Вы: ')
    tokens = clean_text(sentence)
    X = bag_of_words(tokens, words)
    
    with torch.no_grad():
        output = model(X)
        probs = torch.softmax(output, dim=0)
        prob, idx = torch.max(probs, dim=0)
        tag = tags[idx]

    if prob.item() > 0.6:
        for intent in config['intents']:
            if tag == intent['tag']:
                print(f'Бот: {random.choice(intent["responses"])} (Уверенность: {prob.item():.2f})\n')
    else:
        print(f'Бот: {random.choice(config["fallback_responses"])} (Уверенность низкая: {prob.item():.2f})\n')
        