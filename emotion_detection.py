import requests

def emotion_detector(text_to_analyze):
    try:
        url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        payload = {"raw_document": {"text": text_to_analyze}}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        print(data)  # Debugging
        if "text" in data:
            return data["text"]
        return "No 'text' attribute in response"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

