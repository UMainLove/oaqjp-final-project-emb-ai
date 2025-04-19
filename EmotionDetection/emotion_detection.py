import requests
import json

def emotion_detector(text_to_analyse):
    """
    Call Watson’s EmotionPredict endpoint, extract the five
    emotion scores plus the dominant emotion, and return
    a flat dict.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=payload, headers=headers)

    # === NEW: handle blank‑input API error ===
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response.raise_for_status()
    data = response.json()
    scores = data['emotionPredictions'][0]['emotion']

    emotions = {
        'anger':    scores['anger'],
        'disgust':  scores['disgust'],
        'fear':     scores['fear'],
        'joy':      scores['joy'],
        'sadness':  scores['sadness'],
    }
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions
