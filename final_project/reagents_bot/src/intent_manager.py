import json
import random
import os

class IntentManager:
    def __init__(self, file_path):
        # Загружаем JSON с интентами
        with open(file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.intents = self.data['intents']
        self.fallbacks = self.data['fallback_responses']

    def get_intent_response(self, text):
        # Очистка от знаков препинания и разбивка на слова
        clean_query = text.lower().strip().replace('?', '').replace('!', '').replace(',', '').replace('.', '')
        words = clean_query.split()
        
        for intent in self.intents:
            for pattern in intent['patterns']:
                pattern_low = pattern.lower().strip()
                
                # Ищем либо полное совпадение фразы, либо отдельное слово
                if pattern_low == clean_query or pattern_low in words:
                    return random.choice(intent['responses'])
        
        return None

    def get_fallback(self):
        return random.choice(self.fallbacks)
    