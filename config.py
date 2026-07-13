"""
config.py

Project configuration for Emotion Palette.
Contains model configuration and emotion color mapping.
"""

# ==========================================================
# Hugging Face Model
# ==========================================================

MODEL_NAME = "j-hartmann/emotion-english-roberta-large"


# ==========================================================
# Emotion Color Mapping
# ==========================================================

EMOTION_COLORS = {
    "joy": "#FFD700",             # Gold
    "sadness": "#1E90FF",         # Dodger Blue
    "fear": "#800080",            # Purple
    "anger": "#FF4500",           # Orange Red
    "surprise": "#FFA500",        # Orange
    "disgust": "#556B2F",         # Dark Olive Green
    "amusement": "#FF6347",       # Tomato
    "anxiety": "#8B0000",         # Dark Red
    "awe": "#00CED1",             # Dark Turquoise
    "boredom": "#A9A9A9",         # Dark Gray
    "calmness": "#87CEFA",        # Light Sky Blue
    "compassion": "#FFB6C1",      # Light Pink
    "contempt": "#8B4513",        # Saddle Brown
    "contentment": "#98FB98",     # Pale Green
    "despair": "#2F4F4F",         # Dark Slate Gray
    "disappointment": "#808080",  # Gray
    "empathy": "#F4A460",         # Sandy Brown
    "envy": "#228B22",            # Forest Green
    "excitement": "#FF69B4",      # Hot Pink
    "frustration": "#DC143C",     # Crimson
    "gratitude": "#FFDAB9",       # Peach Puff
    "guilt": "#8B008B",           # Dark Magenta
    "hope": "#00FA9A",            # Medium Spring Green
    "horror": "#4B0082",          # Indigo
    "interest": "#00BFFF",        # Deep Sky Blue
    "jealousy": "#32CD32",        # Lime Green
    "loneliness": "#2E8B57",      # Sea Green
    "love": "#FF1493",            # Deep Pink
    "nostalgia": "#D2B48C",       # Tan
    "pride": "#FFD700",           # Gold
    "relief": "#ADFF2F",          # Green Yellow
    "remorse": "#8A2BE2",         # Blue Violet
    "shame": "#FF00FF",           # Magenta
    "sympathy": "#FF69B4",        # Hot Pink
    "trust": "#4169E1",           # Royal Blue
    "wonder": "#DA70D6",          # Orchid
    "yearning": "#9932CC"         # Dark Orchid
}