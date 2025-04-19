"""
Server module for the Emotion Detection web application.
"""

import requests
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Handle the /emotionDetector POST endpoint.

    Reads the 'text' form field, calls emotion_detector(),
    and returns a formatted response or an error message.
    """
    text = request.form.get('text', '').strip()
    if not text:
        return "Invalid text! Please try again!", 400

    try:
        result = emotion_detector(text)
        if result.get('dominant_emotion') is None:
            return "Invalid text! Please try again!", 400

        response_str = (
            "For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_str

    except requests.exceptions.RequestException as error:
        # Only catching HTTP/network errors from requests
        return f"Error: {error}", 500


def main():
    """Run the Flask development server on 0.0.0.0:5000."""
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
