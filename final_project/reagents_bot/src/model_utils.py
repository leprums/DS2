import torch
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util

class ReagentSearcher:
    def __init__(self, model_name='intfloat/multilingual-e5-small', csv_path='data/processed/clean_reagents.csv', npy_path='data/processed/reagents_embeddings.npy'):
        # Инициализация модели и данных
        self.model = SentenceTransformer(model_name, cache_folder='models')
        self.df = pd.read_csv(csv_path).fillna('')
        # Подгружаем эмбеддинги
        self.corpus_embeddings = torch.from_numpy(np.load(npy_path))

    def search(self, user_query, threshold=0.83, top_k=10):
        # Подготовка запроса
        query_text = f'query: {user_query}'
        query_embedding = self.model.encode(query_text, convert_to_tensor=True)
        
        # Поиск похожих
        hits = util.semantic_search(query_embedding, self.corpus_embeddings, top_k=top_k)[0]
        
        results = []
        for hit in hits:
            score = hit['score']
            if score < threshold:
                continue
                
            idx = hit['corpus_id']
            item = self.df.iloc[idx]
            
            # Логика бонусов за точное совпадение
            q = user_query.lower().strip()
            name = str(item['название']).lower().strip()
            form = str(item['формула']).lower().strip() if pd.notna(item['формула']) else ''
            
            if q == name or q == form:
                score += 0.1
                
            results.append({
                'name': item['название'],
                'location': f"Комн. {item['комната']}, {item['шкаф']}, {item['полка']}, {item.get('коробка', '')}",
                'formula': item['формула'] if pd.notna(item['формула']) else None,
                'purity': item['чистота'] if pd.notna(item['чистота']) else None,
                'note': item['примечание'] if pd.notna(item['примечание']) else None,
                'score': round(score, 3)
            })
            
        # Сортировка по обновленному score
        results = sorted(results, key=lambda x: x['score'], reverse=True)
        return results
    