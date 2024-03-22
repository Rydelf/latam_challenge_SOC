from typing import List, Tuple
from datetime import datetime
from gcp import read_json_from_gcp

def q1_memory(tweets: List[dict]) -> List[Tuple[datetime.date, str]]:
    # Diccionario para almacenar la cantidad de tweets por fecha
    date_tweets = {}
    # Diccionario para almacenar el usuario más activo por fecha
    date_top_user = {}

    # Procesar cada tweet en la lista
    for tweet in tweets:
        # Obtener la fecha del tweet
        tweet_date = datetime.strptime(tweet['date'], "%Y-%m-%dT%H:%M:%S%z").date()
        user = tweet['user']['username']
        
        # Contar la cantidad de tweets por fecha
        date_tweets[tweet_date] = date_tweets.get(tweet_date, 0) + 1
        
        # Actualizar el usuario más activo para esta fecha
        if tweet_date not in date_top_user:
            date_top_user[tweet_date] = user
        else:
            current_tweets = date_tweets[tweet_date]
            max_tweets = date_tweets.get(date_top_user[tweet_date], 0)
            if current_tweets > max_tweets:
                date_top_user[tweet_date] = user
    
    # Obtener las top 10 fechas con más tweets
    top_dates = sorted(date_tweets.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Obtener el usuario más activo para cada fecha
    result = [(date, date_top_user[date]) for date, _ in top_dates]
    
    return result


# Ejemplo de uso
file_path = read_json_from_gcp("latam-1", "farmers-protest-tweets-2021-2-4.json", "latam-challenge-417813")
result = q1_memory(file_path)
print(result)