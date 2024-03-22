from typing import List, Tuple
from collections import Counter
import emoji
from gcp import read_json_from_gcp

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Lista para almacenar los emojis y sus conteos
    emoji_counts = Counter()    
        
    for tweet in file_path:
        # Obtener el contenido del tweet
        content = tweet.get('content', '')
        # Convertir emojis Unicode en texto plano y contarlos
        emojis_text = emoji.emojize(content)
        emojis_list = [c for c in emojis_text if c in emoji.EMOJI_DATA]
        emoji_counts.update(emojis_list)
    
    # Obtener los top 10 emojis más usados
    top_emojis = emoji_counts.most_common(10)
    
    return top_emojis

# Ejemplo de uso
file_path = read_json_from_gcp("latam-1", "farmers-protest-tweets-2021-2-4.json", "latam-challenge-417813")
result = q2_time(file_path)
print(result)