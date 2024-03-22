from typing import List, Tuple
from gcp import read_json_from_gcp

def q3_time(file_path) -> List[Tuple[str, int]]:
    # Diccionario para contar menciones por usuario
    mentions_count = {}
    
    # Iterar sobre cada tweet en los datos JSON
    for tweet in file_path:
        # Verificar si la clave 'mentionedUsers' está presente en el tweet
        if 'mentionedUsers' in tweet:
            mentioned_users = tweet['mentionedUsers']
            # Verificar si mentioned_users no es None
            if mentioned_users is not None:
                for user in mentioned_users:
                    username = user.get('username')
                    if username:
                        mentions_count[username] = mentions_count.get(username, 0) + 1
    
    # Ordenar los usuarios por número de menciones de forma descendente
    top_users = sorted(mentions_count.items(), key=lambda x: x[1], reverse=True)
    
    return top_users[:10]  # Devuelve los 10 usuarios más mencionados

# Calcular el top 10 de usuarios más mencionados
file_path = read_json_from_gcp("latam-1", "farmers-protest-tweets-2021-2-4.json", "latam-challenge-417813")
result = q3_time(file_path)
print(result)