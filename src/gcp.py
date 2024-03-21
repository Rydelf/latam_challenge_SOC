import json
from google.cloud import storage

def read_json_from_gcp(bucket_name, file_name, project_id):
    # Inicializa el cliente de almacenamiento con el ID del proyecto
    storage_client = storage.Client(project=project_id)
    
    # Obtiene el bucket
    bucket = storage_client.bucket(bucket_name)
    
    # Obtiene el blob (archivo) del bucket
    blob = bucket.blob(file_name)
    
    # Descarga el contenido del archivo JSON como bytes
    json_content_bytes = blob.download_as_string()
    
    # Decodifica cada línea del archivo JSON
    json_data = [json.loads(line) for line in json_content_bytes.decode('utf-8').splitlines() if line.strip()]
    
    return json_data