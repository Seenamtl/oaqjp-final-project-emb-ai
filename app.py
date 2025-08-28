from flask import Flask, render_template, request
from app.emotion_detector import emotion_detector   # import from your package

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    # Get text from query parameter (like ?textToAnalyze=...)
    text_to_analyze = request.args.get('textToAnalyze')

    # Call your emotion_detector function
    response = emotion_detector(text_to_analyze)

    # If invalid input → return error message
    if response.dominant == "":
        response_text = "Invalid Input! Please try again."
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': {response.emotions.get('anger',0)}, "
            f"'disgust': {response.emotions.get('disgust',0)}, "
            f"'fear': {response.emotions.get('fear',0)}, "
            f"'joy': {response.emotions.get('joy',0)}, "
            f"'sadness': {response.emotions.get('sadness',0)}. "
            f"The dominant emotion is {response.dominant}."
        )

    return response_text

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





'''
import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)
    status_code = response.status_code
    
    if status_code == 400:
        formatted_response = { 'anger': None,
                             'disgust': None,
                             'fear': None,
                             'joy': None,
                             'sadness': None,
                             'dominant_emotion': None }
    else:
        res = json.loads(response.text)
        formatted_response = res['emotionPredictions'][0]['emotion']
        dominant_emotion = max(formatted_response, key = lambda x: formatted_response[x])
        formatted_response['dominant_emotion'] = dominant_emotion

    return formatted_response 
    '''
    
    
    
    
"""
    SERVER.PY

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    ''' This function calls the application
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant_emotion']}."

    return response_text

@app.route("/")
def render_index_page():
    ''' This is the function to render the html interface
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
"""