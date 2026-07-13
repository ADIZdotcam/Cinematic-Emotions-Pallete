"""
preprocessing.py

Handles:
- Reading input files
- Dialogue extraction
- Text preprocessing
"""

import re
import spacy
import PyPDF2


# ==========================================================
# Load spaCy Model
# ==========================================================

nlp = spacy.load("en_core_web_sm")


# ==========================================================
# Unicode Cleaning
# ==========================================================

def clean_unicode(text: str) -> str:
    """
    Replace problematic unicode characters with standard ones.
    """

    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')

    return text


# ==========================================================
# Dialogue Extraction
# ==========================================================

def extract_dialogues(script_text: str) -> list:
    """
    Extract movie dialogues from screenplay text.
    """

    scene_pattern = r"^(INT\.|EXT\.).*"
    character_pattern = r"^[A-Z][A-Z\s]*\b$"
    action_pattern = r"^\(.*\)$"

    lines = script_text.split("\n")

    dialogues = []
    current_character = None
    current_dialogue = []

    for line in lines:

        line = clean_unicode(line.strip())

        if re.match(scene_pattern, line):

            current_character = None

            if current_dialogue:

                dialogues.append(" ".join(current_dialogue))
                current_dialogue = []

        elif re.match(character_pattern, line):

            if current_dialogue:

                dialogues.append(" ".join(current_dialogue))
                current_dialogue = []

            current_character = line

        elif re.match(action_pattern, line):

            continue

        elif current_character and line:

            current_dialogue.append(line)

    if current_dialogue:

        dialogues.append(" ".join(current_dialogue))

    return dialogues


# ==========================================================
# Text Preprocessing
# ==========================================================

def preprocess_text(dialogues: list) -> list:
    """
    Lemmatize dialogues and remove stop words.
    """

    cleaned_dialogues = []

    for dialogue in dialogues:

        doc = nlp(dialogue)

        tokens = [

            token.lemma_

            for token in doc

            if not token.is_stop and not token.is_punct

        ]

        cleaned_dialogues.append(" ".join(tokens))

    return cleaned_dialogues


# ==========================================================
# Read TXT File
# ==========================================================

def read_text_file(file_path: str) -> str:
    """
    Read plain text file.
    """

    with open(file_path, "r", encoding="utf-8") as file:

        return file.read()


# ==========================================================
# Read PDF File
# ==========================================================

def read_pdf_file(file_path: str) -> str:
    """
    Extract text from PDF.
    """

    text = ""

    with open(file_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted

    return text


# ==========================================================
# Generic File Reader
# ==========================================================

def read_script(file_path: str) -> str:
    """
    Read TXT or PDF screenplay.
    """

    if file_path.lower().endswith(".txt"):

        return read_text_file(file_path)

    elif file_path.lower().endswith(".pdf"):

        return read_pdf_file(file_path)

    raise ValueError(
        "Unsupported file format. Please use a TXT or PDF file."
    )