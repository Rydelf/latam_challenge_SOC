from typing import List, Tuple
from gcp import read_json_from_gcp

def q3_memory(bucket_name: str, file_name: str, project_id: str) -> List[Tuple[str, int]]:
    # Diccionario para contar menciones por usuario
    mentions_count = {}

    # Obtener los datos JSON del archivo en GCP
    json_data = read_json_from_gcp(bucket_name, file_name, project_id)
    
    # Iterar sobre cada tweet en los datos JSON generados
    for tweet in json_data:
        # Verificar si la clave 'mentionedUsers' está presente en el tweet
        if 'mentionedUsers' in tweet:
            mentioned_users = tweet['mentionedUsers']
            # Verificar si mentioned_users no es None
            if mentioned_users is not None:
                for user in mentioned_users:
                    username = user.get('username')
                    if username:
                        # Utilizar un generador de expresión para obtener el username
                        mentions_count[username] = mentions_count.get(username, 0) + 1
    
    # Utilizar un generador para ordenar y obtener los 10 usuarios más mencionados
    top_users_generator = (item for item in sorted(mentions_count.items(), key=lambda x: x[1], reverse=True)[:10])
    
    return list(top_users_generator)  # Devuelve los 10 usuarios más mencionados como lista


# Calcular el top 10 de usuarios más mencionados
result = q3_memory("latam-1", "farmers-protest-tweets-2021-2-4.json", "latam-challenge-417813")
print(result)