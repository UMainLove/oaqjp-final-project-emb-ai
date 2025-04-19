import pytest
from EmotionDetection import emotion_detector

@pytest.mark.parametrize("text, expected", [
    ("I am glad this happened",            "joy"),
    ("I am really mad about this",         "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this",             "sadness"),
    ("I am really afraid that this will happen", "fear"),
])
def test_dominant_emotion(text, expected):
    result = emotion_detector(text)
    assert result["dominant_emotion"] == expected
