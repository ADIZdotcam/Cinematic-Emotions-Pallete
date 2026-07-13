"""
main.py

Emotion Palette

Run the complete pipeline:
1. Read screenplay
2. Extract dialogues
3. Predict emotions
4. Generate visualizations
"""

from pathlib import Path

from src.emotion_classifier import process_file
from src.visualization import (
    visualize_emotions,
    plot_emotion_distribution
)


# ==========================================================
# Configuration
# ==========================================================

# Change this to your script
FILE_PATH = "sample_data/500DaysOfSummer.txt"

# Used only for titles and output filenames
MOVIE_NAME = "500 Days of Summer"


# ==========================================================
# Main Pipeline
# ==========================================================

def main():

    print("=" * 60)
    print(" Emotion Palette ")
    print("=" * 60)

    if not Path(FILE_PATH).exists():

        raise FileNotFoundError(
            f"\nFile not found:\n{FILE_PATH}"
        )

    print("\nReading screenplay...")

    df = process_file(FILE_PATH)

    print(f"Detected {len(df)} dialogues.")

    print("\nGenerating Emotion Palette...")

    visualize_emotions(
        df,
        movie_name=MOVIE_NAME
    )

    print("Generating Emotion Distribution...")

    plot_emotion_distribution(
        df,
        movie_name=MOVIE_NAME
    )

    print("\nFirst Five Predictions\n")

    print(df.head())

    print("\nDone!")
    print("Images saved in outputs/")


if __name__ == "__main__":
    main()