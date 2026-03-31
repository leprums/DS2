import torch
import torch.nn as nn
import re
from nltk.stem.snowball import SnowballStemmer

# Инициализируем стеммер
stemmer = SnowballStemmer("russian")

def clean_text(text):
    # Очистка и приведение к нижнему регистру
    text = re.sub(r'[^\w\s]', ' ', text.lower())
    words = text.split()
    # Стемминг: обрезаем слова до корней
    return [stemmer.stem(w) for w in words]

# Функция для вектора
def bag_of_words(tokenized_sentence, words):
    return torch.FloatTensor([1.0 if w in tokenized_sentence else 0.0 for w in words])

# Сама нейросеть
class TinyNet(nn.Module):
    def __init__(self, in_size, hidden, out_size):
        super().__init__()
        self.l1 = nn.Linear(in_size, hidden)
        self.l2 = nn.Linear(hidden, out_size)
        self.relu = nn.ReLU()
        
    def forward(self, x): 
        return self.l2(self.relu(self.l1(x)))
    