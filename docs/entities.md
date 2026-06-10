# Named Entity Recognition

## Objective

The goal of Named Entity Recognition (NER) is to identify important characters and locations mentioned throughout a book.

This information can be used to build character maps, timelines and cross-book references.

---

## Pipeline

```text
Project Gutenberg Book
          │
          ▼
      Cleaning
(remove headers, footers)
          │
          ▼
      spaCy NER
(entity detection)
          │
          ▼
 Entity Validation
(length, casing,
format checks)
          │
          ▼
 Entity Filtering
(remove common words,
invalid entities)
          │
          ▼
 Character Extraction
(PERSON)
          │
          ▼
 Location Extraction
(GPE / LOC)
          │
          ▼
 Frequency Filtering
(keep recurring entities)
          │
          ▼
 Deduplication
(remove overlaps)
          │
          ▼
     JSON Output
```

---

## Technical Choices

### Why spaCy?

spaCy provides a lightweight and efficient pre-trained NER model.

Advantages:

* Fast execution
* Good accuracy
* Easy integration
* No additional training required
* Lightweight enough for local execution

---

### Why entity validation?

Raw NER output often contains noisy entities.

Validation rules remove:

* Very short entities
* Uppercase-only entities
* Lowercase-only entities
* Chapter titles
* Possessive forms
* Non-alphabetic entities

This improves precision before applying additional filters.

---

### Why frequency filtering?

Books often contain many entities that appear only once.

Examples:

* Typographical errors
* Secondary characters
* Misclassified entities

Keeping only recurring entities improves output quality.

Current thresholds:

* Characters: minimum 3 occurrences
* Locations: minimum 3 occurrences

---

### Why custom filtering?

Some literary books contain words frequently mistaken for entities.

Examples observed during testing:

* Common nouns
* Dialogue artifacts
* Animal names
* Narrative vocabulary

A dedicated filtering layer removes these false positives before generating the final output.

---

## Limitations

NER models occasionally misclassify entities.

Examples observed during testing:

* Dinah detected as a location
* Akela detected as a location
* Tabaqui detected as a location

Entity recognition is probabilistic and therefore imperfect.

Other limitations:

* Some fictional characters may not be recognized.
* Rare entities may be filtered out by frequency thresholds.
* Different names for the same character are not merged automatically.
* Results depend on the quality of the source text.

---

## Alternatives Considered

### Rule-Based Extraction

Pros:

* Fully explainable
* No external model required

Cons:

* Difficult to generalize
* High maintenance cost
* Poor robustness on different books

---

### Transformer-based NER

Pros:

* Higher accuracy
* Better contextual understanding

Cons:

* Heavier models
* Higher memory consumption
* Slower execution

---

### Dictionary-Based Extraction

Pros:

* Very fast
* Easy to implement

Cons:

* Requires predefined character lists
* Poor adaptability to unknown books

---

spaCy was selected because it provides the best balance between speed, accuracy, simplicity and resource consumption for this project.
