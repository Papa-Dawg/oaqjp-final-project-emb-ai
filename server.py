'''Module for Python server bringing Emotion Detector functionality to client '''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    '''Returns output of Emotion Detector to client'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    emotion_scores = {key: value for key, value in response.items() if key != 'dominant_emotion'}
    emotion_data = ', '.join(
        f"'{key}': {value if value is not None else 'None'}" 
        for key, value in emotion_scores.items()
        )
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return_text = (
        f"For the given statement, the system response is {emotion_data}."
        f"The dominant emotion is {dominant_emotion}."
    )
    return return_text

@app.route("/")
def render_index_page():
    '''returns HTML to client'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0", port=5000)
