import torch
import torch.nn as nn
import json
from model import TinyNet, clean_text, bag_of_words

# Загружаем конфиг
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Готовим данные
all_words = []
tags = []
xy = []
hidden_size = 16

for intent in config['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = clean_text(pattern)
        all_words.extend(w)
        xy.append((w, tag))

all_words = sorted(list(set(all_words)))
tags = sorted(list(set(tags)))

# Параметры
X_train = torch.stack([bag_of_words(s, all_words) for (s, t) in xy])
y_train = torch.LongTensor([tags.index(t) for (s, t) in xy])

# Модель
model = TinyNet(len(all_words), hidden_size, len(tags))
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Учим 200 эпох
for epoch in range(200):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

# Сохраняем всё в один файл
torch.save({
    'model_state': model.state_dict(),
    'all_words': all_words,
    'tags': tags,
    'hidden_size': hidden_size,
    'in_size': len(all_words),
    'out_size': len(tags)
}, 'model.pth')

print('Модель готова!')
