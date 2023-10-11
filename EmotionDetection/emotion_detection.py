import json # importamos la libreria json
import requests # Librería Python que facilita el trabajo con peticiones HTTP
def emotion_detector(text_to_analyse): # función para procesar la detección de emociones
    # URL Para acceder a la función de predicción de emociones de la biblioteca Watson NLP.
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    # Encabezados y el formato json de entrada
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    InputObj = {"raw_document": {"text": text_to_analyse}}
    resp = requests.post(url, json=InputObj, headers=headers)  # Respuesta a la peticion se introducen la url,entrada en formato json y encabezados
    RespJson = json.loads(resp.text)  # Respuesta en formato json
    if resp.status_code == 200:
        EmotionPredictions = RespJson["emotionPredictions"][0]["emotion"] # Se devuelve el porcentaje de predicción de cada emoción en formato json
        DominantEmotion = max(EmotionPredictions.items(), key=lambda x: x[1])[0] # Se obtiene la emoción dominante
        return {
            'anger': EmotionPredictions['anger'],
            'disgust': EmotionPredictions['disgust'],
            'fear': EmotionPredictions['fear'],
            'joy': EmotionPredictions['joy'],
            'sadness': EmotionPredictions['sadness'],
            "dominant_emotion": DominantEmotion }
    else:
        return {'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            "dominant_emotion": None
        }

if __name__ == '__main__':
    print(emotion_detector("I am so happy I am doing this"))