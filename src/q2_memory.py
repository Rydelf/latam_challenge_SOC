from typing import List, Tuple
from collections import Counter
import emoji
from gcp import read_json_from_gcp


def q2_memory(bucket_name: str, file_name: str, project_id: str) -> List[Tuple[str, int]]:
    emoji_counts = Counter()

    # Obtener los datos JSON del archivo en GCP
    json_data = read_json_from_gcp(bucket_name, file_name, project_id)

    # Procesar los tweets para contar emojis
    for tweet_data in json_data:
        # Obtener el contenido del tweet
        content = tweet_data.get('content', '')
        # Convertir emojis Unicode en texto plano y contarlos
        emojis_text = emoji.emojize(content)
        emojis_list = [c for c in emojis_text if c in emoji.EMOJI_DATA]
        emoji_counts.update(emojis_list)

    # Obtener los top 10 emojis más usados
    top_emojis = emoji_counts.most_common(10)

    return top_emojis


# Ejemplo de uso
result_memory = q2_memory("latam-1", "farmers-protest-tweets-2021-2-4.json", "latam-challenge-417813")
print(result_memory)