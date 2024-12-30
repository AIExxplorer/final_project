"""
This module contains a Flask application for emotion detection using Watson NLP API.
It provides a web interface and an API endpoint for analyzing emotions in text.
"""

import requests
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page with the interface for emotion detection.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detect emotions in a given text using the emotion_detector function.

    Returns:
        JSON: Contains the detected emotions and their scores. Returns an error
        message if the input is invalid or an exception occurs.
    """
    try:
        data = request.json
        text_to_analyze = data.get('text', '')

        emotion_response = emotion_detector(text_to_analyze)

        if emotion_response['dominant_emotion'] is None:
            return jsonify({'error': 'Invalid text! Please try again!'}), 400

        response_message = (
            f"For the given statement, the system response is 'anger': "
            f"{emotion_response['anger']}, 'disgust': {emotion_response['disgust']}, "
            f"'fear': {emotion_response['fear']}, 'joy': {emotion_response['joy']} "
            f"and 'sadness': {emotion_response['sadness']}. The dominant emotion is "
            f"{emotion_response['dominant_emotion']}."
        )
        return jsonify({'message': response_message, 'details': emotion_response})

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
