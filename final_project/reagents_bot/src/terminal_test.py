import time
from src.model_utils import ReagentSearcher
from src.intent_manager import IntentManager

def main():
    # Инициализация
    print('📦 Загрузка поискового движка и базы знаний...')
    try:
        searcher = ReagentSearcher()
        intent_manager = IntentManager('intentions.json')
        print('✅ Система готова к работе!')
    except Exception as e:
        print(f'❌ Ошибка инициализации: {e}')
        return

    print('\n--- Поиск реактивов (Терминальная версия) ---')
    print('Введите название, формулу или просто скажите "Привет"')
    print('Для выхода нажмите Ctrl+C')

    try:
        while True:
            query = input('\n🔎 Запрос: ').strip()
            if not query:
                continue

            # Сначала проверяем интенты
            intent_response = intent_manager.get_intent_response(query)
            
            if intent_response:
                print(f'🤖 {intent_response}')
                continue

            # Если не интент — запускаем векторный поиск
            start_time = time.time()
            results = searcher.search(query, threshold=0.83)
            elapsed = (time.time() - start_time) * 1000

            # Обработка результатов
            if results:
                print(f'✅ Найдено вариантов: {len(results)} (за {elapsed:.1f} мс)')
                print('=' * 40)
                
                for i, res in enumerate(results, 1):
                    confidence = res['score'] * 100
                    print(f"{i}. [{confidence:.1f}%] {res['name']}")
                    
                    # Чистим строку локации от лишних запятых
                    loc = res['location'].replace(' ,', '').replace(', ,', ',').strip(', ')
                    print(f'   📍 Место: {loc}')
                    
                    if res.get('formula'):
                        print(f"   🧪 Формула: {res['formula']}")
                    if res.get('purity'):
                        print(f"   ✨ Чистота: {res['purity']}")
                    if res.get('note'):
                        print(f"   📝 Примечание: {res['note']}")
                    
                    print('-' * 40)
            else:
                # Если нейронка ничего не нашла — выдаем fallback
                print(f'🤖 {intent_manager.get_fallback()}')

    except KeyboardInterrupt:
        print('\n\n👋 Тестирование завершено!')

if __name__ == '__main__':
    main()
    