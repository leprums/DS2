from dotenv import load_dotenv
import os
import asyncio
import logging
import time
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.model_utils import ReagentSearcher
from src.intent_manager import IntentManager

# Загружаем токены
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)

# Инициализация
try:
    searcher = ReagentSearcher()
    intent_manager = IntentManager('intentions.json')
    print('✅ Бот готов к работе!')
except Exception as e:
    print(f'❌ Ошибка загрузки: {e}')
    exit()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('👋 Привет, коллега! Я помогу найти реактив. Просто напиши название или формулу.')

@dp.message(F.text)
async def handle_query(message: types.Message):
    query = message.text.strip()

    # 1. Проверка интентов
    intent_response = intent_manager.get_intent_response(query)
    if intent_response:
        await message.reply(f'🤖 {intent_response}')
        return 
    
    # 2. Поиск
    start_time = time.time()
    results = searcher.search(query, threshold=0.83)
    elapsed = (time.time() - start_time) * 1000
    
    if results:
        response_parts = [f'✅ *Найдено вариантов: {len(results)}* (за {elapsed:.1f} мс)\n' + '='*20]
        
        for i, res in enumerate(results, 1):
            confidence = res['score'] * 100
            item_info = [f"*{i}. [{confidence:.1f}%] {res['name']}*"]
            
            loc = res['location'].replace(' ,', '').replace(', ,', ',').strip(', ')
            item_info.append(f'📍 Место: {loc}')
            
            if res.get('formula'):
                item_info.append(f"🧪 Формула: `{res['formula']}`")
            if res.get('purity'):
                item_info.append(f"✨ Чистота: {res['purity']}")
            if res.get('note'):
                item_info.append(f"📝 Примечание: _{res['note']}_")
            
            response_parts.append('\n'.join(item_info))
            response_parts.append('-' * 20)
            
        await message.answer('\n'.join(response_parts))
    else:
        await message.reply(f'🤖 {intent_manager.get_fallback()}')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')
        