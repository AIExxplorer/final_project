import requests


# Função para detecção de emoções
def emotion_detector(text_to_analyze):
    """
    Função que utiliza a Watson NLP Library para analisar emoções em um texto.

    :param text_to_analyze: Texto a ser analisado.
    :return: Dicionário com as emoções detectadas e a emoção dominante.
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

        # Converte a resposta em JSON para um dicionário
        response_data = response.json()

        # Extrai as emoções relevantes e seus scores
        emotions = response_data.get('emotion_predictions', {})

        # Obtém as emoções desejadas
        emotion_scores = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0)
        }

        # Determina a emoção dominante
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Adiciona a emoção dominante ao dicionário
        emotion_scores['dominant_emotion'] = dominant_emotion

        return emotion_scores

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ao Watson NLP API: {e}")
        return None
