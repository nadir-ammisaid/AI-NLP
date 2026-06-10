# ALICE'S ADVENTURES IN WONDERLAND

> Nested Literary Puzzles - Lightweight NLP Engine for Project Gutenberg Books

This project was developed as part of the Artificial Intelligence module at Epitech.

The objective is to build a lightweight Natural Language Processing (NLP) engine capable of analyzing books from Project Gutenberg through dedicated CLI commands and generating structured book cards.

The application extracts lexical, thematic and semantic information from literary works without relying on large language models or external APIs.

---

# Features

The project implements all mandatory tasks from the subject:

* Lexical Diversity Analysis
* Topic Modeling
* Named Entity Recognition
* Book Summarization
* Book Similarity
* Book Card Generation

---

# Prerequisites

* Python 3.12+
* pip (installed with Python)
* Internet connection (required during first installation and first model download)

---

# Installation

Clone the repository:

```bash
git clone git@github.com:nadir-ammisaid/AI-NLP.git
cd AI-NLP
```

Create a virtual environment:

```bash
python3 -m venv .venv   # or: python -m venv .venv
```

Activate it:

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Upgrade pip inside the virtual environment:

```bash
python3 -m pip install --upgrade pip   # or: python -m pip install --upgrade pip
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt   # or: python -m pip install -r requirements.txt
```

Install the spaCy English model:

```bash
python3 -m spacy download en_core_web_sm   # or: python -m spacy download en_core_web_sm
```

---

# Code Formatting and Tests

Before running the project, it is recommended to verify that the source code is correctly formatted and that all tests pass.

Format the source code:

```bash
python3 -m black src tests   # or: python -m black src tests
```

Run the test suite:

```bash
python3 -m pytest   # or: python -m pytest
```

Expected result:

```text
7 passed
```

This step helps ensure that the project is correctly installed and behaves as expected before downloading books and running NLP analyses.

---

# Download Books

Books can be downloaded directly from Project Gutenberg.

Example:

```bash
python3 src/download_books.py \
11 12 16 55 113 120 236 \
108 834 863 1661 61262 69087 70114 \
35 36 84 159 164 345 68283
```

Downloaded files are stored in:

```text
data/downloads/
```

---

# Dataset

The similarity engine operates on the official collection provided in the subject.

## Children / Young Adult

* Alice's Adventures in Wonderland
* Through the Looking-Glass
* Peter Pan
* The Wonderful Wizard of Oz
* The Secret Garden
* Treasure Island
* The Jungle Book

## Crime, Mystery & Thriller

* The Adventures of Sherlock Holmes
* The Memoirs of Sherlock Holmes
* The Return of Sherlock Holmes
* The Mysterious Affair at Styles
* Poirot Investigates
* The Murder of Roger Ackroyd
* The Big Four

## Science-Fiction & Fantasy

* The Time Machine
* The War of the Worlds
* Frankenstein
* The Island of Doctor Moreau
* Twenty Thousand Leagues Under the Sea
* Dracula
* The Call of Cthulhu

---

# Usage

Display help:

```bash
python3 src/bookworm.py --help
```

Display version:

```bash
python3 src/bookworm.py --version
```

---

## Lexical Diversity

```bash
python3 src/bookworm.py --lexdiv 11
```

Returns lexical richness metrics:

```json
{
    "tok": 11793,
    "typ": 2076,
    "hap": 932,
    "ttr": 0.176
}
```

---

## Topic Modeling

```bash
python3 src/bookworm.py --topics 11
```

Example:

```json
{
    "1": ["alice", "rabbit", "mouse"],
    "2": ["queen", "hatter", "hare"],
    "3": ["court", "king", "gryphon"]
}
```

---

## Named Entity Recognition

```bash
python3 src/bookworm.py --entities 11
```

Example:

```json
{
    "characters": ["Alice", "Rabbit"],
    "locations": ["Wonderland"]
}
```

---

## Book Summarization

```bash
python3 src/bookworm.py --summarize 11
```

Returns an extractive summary composed of the most representative paragraphs.

---

## Book Similarity

```bash
python3 src/bookworm.py --similar 11
```

Returns the five most similar books from the official collection.

Example:

```json
[
    "Through the Looking-Glass",
    "Peter Pan",
    "The Wonderful Wizard of Oz",
    "The Secret Garden",
    "The Jungle Book"
]
```

---

## Book Card

```bash
python3 src/bookworm.py --card 11
```

Returns a complete structured book card gathering every extracted feature.

---

# Project Architecture

```text
src/
├── bookcard/
├── gutenberg/
├── lexdiv/
├── nlp/
├── pipeline/
├── preprocessing/
├── semantic/
├── topics/
└── utils/
```

---

# Technical Choices

## Topic Modeling

Chosen method:

* LDA (Latent Dirichlet Allocation)

Alternatives considered:

* LSA
* BERTopic

Reasons:

* Lightweight
* Fast execution
* No training required
* Easy to explain
* Compatible with chapter-based analysis

Implementation details:

* Topics are extracted independently for each detected chapter or section.
* Multiple chapter formats are automatically detected (Roman numerals, numbered chapters, Gutenberg chapter structures).
* If no chapter structure is detected, the book is automatically split into 3 equal sections.

Limitations:

* Topic quality depends on chapter structure quality.
* LDA remains a statistical approach and does not understand semantic context.

---

## Summarization

Chosen method:

* Extractive summarization using sentence embeddings and cosine similarity

Alternatives considered:

* TextRank
* Abstractive transformer models

Reasons:

* Deterministic
* Lightweight
* Fast
* Compatible with project constraints

Limitations:

* Cannot generate new sentences
* May include redundant passages

---

## Named Entity Recognition

Chosen method:

* spaCy NER

Reasons:

* Production-ready
* Lightweight
* Reliable English language support

Limitations:

* May miss uncommon entities
* Dependent on source text quality

---

## Similarity

Chosen method:

* SentenceTransformer embeddings
* Cosine similarity

Reasons:

* Strong semantic representation
* Good performance on small collections
* Easy to interpret

---

# Additional Features

Beyond the mandatory requirements, the project includes several extra features and improvements:

* Additional lexical diversity metrics:

  * Root TTR
  * Corrected TTR
  * Herdan's C
  * Maas's a²

* Extended lexical statistics:

  * Mean Word Length (MWL)
  * Mean Word Frequency (MWF)

* Structured export of generated book cards:

  * Automatic JSON export
  * Reusable cached results

* Automatic caching of expensive computations:

  * Generated book cards are saved and can be reused later

* Chapter-aware topic extraction:

  * Automatic chapter detection for multiple Gutenberg formats
  * Topic extraction performed independently for each chapter
  * Automatic fallback to section-based splitting when no chapters are detected

* Project-wide automated test suite:

  * Metadata extraction
  * Lexical metrics
  * Topic modeling
  * Named entity recognition
  * Keyword extraction
  * Text cleaning
  * Summarization

* Cross-platform compatibility:

  * Linux
  * macOS
  * Windows

* Production-oriented repository organization:

  * Modular architecture
  * Dedicated NLP pipelines
  * Automated formatting with Black
  * Automated testing with Pytest

* Lightweight NLP design:

  * No LLMs
  * No external APIs
  * No heavy generative models
  * Fast local execution

* Methodology study and comparison:

  * Comparison of multiple summarization approaches
  * Comparison of multiple topic-modeling approaches
  * Justification of final technical choices
  * Documentation of alternatives, advantages and limitations

---

# Documentation

Additional technical documentation is available in:

```text
docs/
├── entities.md
├── lexdiv.md
├── summary.md
└── topics.md
```

These documents describe:

* Processing pipelines
* Technical choices
* Alternatives considered
* Advantages and limitations

---

# Limitations

* Topic modeling remains statistical and does not fully understand context.
* Summaries are extractive rather than generative.
* Entity recognition quality depends on the source text.
* Similarity results depend on the selected book collection.

---

# Authors

* Nadir AMMI SAID
* Michaël GIRARDET
* Younes HADDAD

Epitech Lyon - Artificial Intelligence Module
