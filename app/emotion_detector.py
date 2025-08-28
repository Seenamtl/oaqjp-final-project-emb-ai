import requests
import json

def emotion_detector(text_to_analyse):
    """Return emotions dict with dominant_emotion; all None on invalid input/error."""

    # 1) Handle blank / missing input
    if text_to_analyse is None or not str(text_to_analyse).strip():
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
    except requests.RequestException:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    if resp.status_code != 200:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    data = resp.json()
    emotions = data['emotionPredictions'][0]['emotion']
    dominant = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant
    return emotions
