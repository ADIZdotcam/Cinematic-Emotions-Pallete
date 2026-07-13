# 🎨 Emotion Palette: Visualizing the Emotional Journey of Movie Scripts

Emotion Palette is a Natural Language Processing (NLP) project that transforms movie dialogues into a visual color palette representing the emotional progression of a story.

Instead of simply classifying emotions, this project provides an intuitive visual representation of how emotions evolve throughout a screenplay, allowing users to experience the emotional rhythm of a narrative.

---

## 📌 Features

- 🎬 Extracts dialogues from movie scripts
- 📝 Supports **TXT** and **PDF** screenplay files
- 🧹 Cleans and preprocesses text using spaCy
- 🤖 Emotion classification using **RoBERTa**
- 🎨 Maps emotions to unique colors
- 🌈 Generates an emotional color spectrum
- 📊 Creates emotion distribution charts

---

## 🧠 Model

This project uses the Hugging Face model:

> **j-hartmann/emotion-english-roberta-large**

The model predicts the dominant emotion for each dialogue along with a confidence score.

---

## 📂 Project Structure

```
emotion-palette/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── sample_data/
│   └── sample_script.txt
│
├── outputs/
│
└── src/
    ├── __init__.py
    ├── preprocessing.py
    ├── emotion_classifier.py
    └── visualization.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/emotion-palette.git

cd emotion-palette
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the spaCy model:

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ Usage

Place your screenplay inside the `sample_data` directory.

Update the following variables in `main.py`:

```python
FILE_PATH = "sample_data/sample_script.txt"

MOVIE_NAME = "Movie Name"
```

Run the project:

```bash
python main.py
```

---

## 📈 Output

The project generates:

- Emotion prediction for every dialogue
- Confidence score
- Emotional color spectrum
- Emotion distribution chart

All generated figures are saved inside the **outputs/** directory.

---

## 🎨 Emotion Color Mapping

Each detected emotion is represented by a unique color.

| Emotion | Color |
|---------|-------|
| Joy | 🟨 Gold |
| Sadness | 🟦 Dodger Blue |
| Fear | 🟪 Purple |
| Anger | 🟥 Orange Red |
| Surprise | 🟧 Orange |
| Disgust | 🟩 Dark Olive Green |
| ... | ... |

---

## 📚 Technologies Used

- Python
- Hugging Face Transformers
- spaCy
- PyTorch
- Pandas
- Matplotlib
- NumPy
- PyPDF2

---

## 📜 License

This project is released under the MIT License.

---

## 👤 Author

**Aditya Maurya** and **Mayank Kumar**
