from typing import List, Tuple
from datetime import datetime
import gcp


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Lista para almacenar tuplas de fecha y usuario más activo
    date_top_user = []
    
    # Diccionario para contar tweets por fecha
    date_tweets = {}
    
      
    for tweet in file_path:
        if 'date' in tweet:
            tweet_date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet['user']['username']
            
            # Actualizar el conteo de tweets por fecha
            date_tweets[tweet_date] = date_tweets.get(tweet_date, 0) + 1
            
            # Actualizar el usuario más activo para esta fecha
            if not date_top_user or date_tweets[tweet_date] > date_tweets[date_top_user[-1][0]]:
                date_top_user.append((tweet_date, user))
                date_top_user.sort(key=lambda x: x[0], reverse=True)
                date_top_user = date_top_user[:10]
                    
    return date_top_user

# Ejemplo de uso
result = q1_memory(gcp.read_json_from_gcp("latam-1", "farmers-protest-tweets-2021-2-4.json", "latam-challenge-417813"))
print(result)