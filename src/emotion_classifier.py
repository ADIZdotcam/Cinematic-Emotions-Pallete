"""
emotion_classifier.py

Loads the Hugging Face emotion model and performs
emotion classification on extracted dialogues.
"""

import pandas as pd

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    pipeline
)

from config import MODEL_NAME
from src.preprocessing import (
    extract_dialogues,
    preprocess_text,
    read_script
)


# ==========================================================
# Load Model (Only Once)
# ==========================================================

print("Loading emotion classification model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME
)

emotion_classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    return_all_scores=True
)

print("Model loaded successfully.")


# ==========================================================
# Emotion Classification
# ==========================================================

def classify_emotion(dialogue: str):
    """
    Predict the dominant emotion for a dialogue.

    Returns
    -------
    emotion : str
    confidence : float
    """

    predictions = emotion_classifier(dialogue)

    emotion_scores = {

        pred["label"]: pred["score"]

        for pred in predictions[0]

    }

    predicted_emotion = max(
        emotion_scores,
        key=emotion_scores.get
    )

    confidence = emotion_scores[predicted_emotion]

    return predicted_emotion, confidence


# ==========================================================
# Process Script Text
# ==========================================================

def process_script(script_text: str):
    """
    Extract dialogues, preprocess them,
    classify emotions and return a DataFrame.
    """

    dialogues = extract_dialogues(script_text)

    processed_dialogues = preprocess_text(dialogues)

    predictions = [

        classify_emotion(dialogue)

        for dialogue in processed_dialogues

    ]

    df = pd.DataFrame({

        "Dialogue": dialogues,

        "Emotion": [
            emotion
            for emotion, _ in predictions
        ],

        "Confidence": [
            confidence
            for _, confidence in predictions
        ]

    })

    return df


# ==========================================================
# Process File
# ==========================================================

def process_file(file_path: str):
    """
    Read a screenplay file and classify emotions.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    pandas.DataFrame
    """

    script = read_script(file_path)

    return process_script(script)