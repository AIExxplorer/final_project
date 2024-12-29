import requests


# Função para detecção de emoções
def emotion_detector(text_to_analyze):
    """
    Função que utiliza a Watson NLP Library para analisar emoções em um texto.

    :param text_to_analyze: Texto a ser analisado.
    :return: Resposta com as emoções detectadas.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    input_json = {
        'raw_document': {
            'text': text_to_analyze
        }
    }

    try:
        # Fazendo a requisição POST
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()  # Garante que erros HTTP sejam tratados
        return response.json()  # Retorna a resposta em JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ao Watson NLP API: {e}")
        return None
