"""
visualization.py

Visualization utilities for Emotion Palette.
"""

from pathlib import Path

import matplotlib.pyplot as plt

from config import EMOTION_COLORS


# ==========================================================
# Emotion Palette Visualization
# ==========================================================

def visualize_emotions(
    df,
    movie_name="Movie",
    save=True,
    show=True,
    output_dir="outputs"
):
    """
    Visualize the emotional journey as a color palette.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing Dialogue, Emotion and Confidence.

    movie_name : str
        Name of the movie.

    save : bool
        Save figure to outputs folder.

    show : bool
        Display figure.

    output_dir : str
        Output directory.
    """

    data = df.copy()

    data["Emotion"] = data["Emotion"].str.lower()

    data["Color"] = data["Emotion"].map(EMOTION_COLORS)

    # Remove neutral dialogues (optional)
    data = data[data["Emotion"] != "neutral"]

    plt.figure(figsize=(18, 2.8))

    for i, color in enumerate(data["Color"]):

        plt.bar(
            i,
            1,
            color=color,
            edgecolor=color,
            width=1.0
        )

    plt.xticks([])
    plt.yticks([])

    plt.xlim(-0.5, len(data) - 0.5)

    plt.title(
        f"Emotional Color Spectrum of {movie_name}",
        fontsize=16,
        weight="bold",
        pad=18
    )

    plt.box(False)

    plt.tight_layout()

    if save:

        Path(output_dir).mkdir(
            parents=True,
            exist_ok=True
        )

        filename = (
            movie_name.lower()
            .replace(" ", "_")
            + "_palette.png"
        )

        plt.savefig(
            Path(output_dir) / filename,
            dpi=300,
            bbox_inches="tight"
        )

    if show:

        plt.show()

    else:

        plt.close()


# ==========================================================
# Emotion Distribution
# ==========================================================

def plot_emotion_distribution(
    df,
    movie_name="Movie",
    save=True,
    show=True,
    output_dir="outputs"
):
    """
    Plot frequency of detected emotions.
    """

    counts = (
        df["Emotion"]
        .str.lower()
        .value_counts()
        .sort_values(ascending=False)
    )

    colors = [
        EMOTION_COLORS.get(e, "#808080")
        for e in counts.index
    ]

    plt.figure(figsize=(10, 5))

    plt.bar(
        counts.index,
        counts.values,
        color=colors
    )

    plt.xticks(rotation=45)

    plt.ylabel("Count")

    plt.title(
        f"Emotion Distribution - {movie_name}",
        fontsize=15,
        weight="bold"
    )

    plt.tight_layout()

    if save:

        filename = (
            movie_name.lower()
            .replace(" ", "_")
            + "_distribution.png"
        )

        plt.savefig(
            Path(output_dir) / filename,
            dpi=300,
            bbox_inches="tight"
        )

    if show:

        plt.show()

    else:

        plt.close()