# Topic Modeling Pipeline

## Objective

The goal of topic modeling is to automatically discover the main themes discussed throughout a book.

The implementation is based on the LDA (Latent Dirichlet Allocation) algorithm.

Topics are extracted independently for each chapter or section in order to capture how themes evolve throughout the book.

---

## Pipeline

```text
Project Gutenberg Book
          │
          ▼
      Cleaning
(remove headers, footers,
special characters)
          │
          ▼
 Chapter Detection
(or fallback section split)
          │
          ▼
    Tokenization
(split text into words)
          │
          ▼
 Stopwords Removal
(remove common words)
          │
          ▼
     POS Tagging
(assign grammatical tags)
          │
          ▼
   Noun Extraction
(keep meaningful nouns)
          │
          ▼
 Chapter Documents
(build chapter corpora)
          │
          ▼
      LDA Model
(topic extraction)
          │
          ▼
 Top 10 Words
 per Chapter
```

---

## Technical Choices

### Why LDA?

LDA is a lightweight and well-established topic modeling algorithm.

Advantages:

* Fast execution
* No training dataset required
* Easy to interpret
* Suitable for medium-sized books
* Fully compliant with project constraints

LDA identifies groups of words that frequently appear together and treats them as latent topics.

---

### Why chapter-based extraction?

The project subject requires extracting topics from each section of a book.

Instead of arbitrarily splitting books into equal parts, the implementation first attempts to detect actual chapter boundaries.

Advantages:

* Better thematic coherence
* More meaningful topics
* Closer to the real structure of the book
* Easier interpretation during presentation

If no valid chapter structure is detected, the system automatically falls back to a simple section-based split.

---

### Why keep nouns only?

Nouns generally carry most of the semantic meaning of a text.

Examples:

* Alice
* Rabbit
* Queen
* Holmes
* Mystery

Keeping nouns reduces grammatical noise and improves topic quality.

Benefits:

* Fewer irrelevant words
* More interpretable topics
* Better thematic representation

---

### Why automatic chapter detection?

Project Gutenberg books use different chapter formats.

Examples encountered in the dataset:

```text
CHAPTER I.
CHAPTER II.

I. A SCANDAL IN BOHEMIA
II. THE RED-HEADED LEAGUE

Chapter 1
Chapter 2

I Introduction
II The Machine
```

The project automatically detects multiple chapter structures before applying topic extraction.

This improves robustness across different books and authors.

---

## Limitations

LDA does not understand semantic context.

For example:

* "Queen" may refer to different concepts.
* Similar words may appear in separate topics.
* Synonyms are not automatically grouped together.

Results are therefore thematic rather than semantic.

Additional limitations:

* Topic quality depends on chapter quality.
* Very short chapters may produce weaker topics.
* Some topics may contain generic vocabulary.

---

## Alternatives Considered

### LSA (Latent Semantic Analysis)

Pros:

* Simple implementation
* Fast execution
* Low resource consumption

Cons:

* Less interpretable topics
* Lower topic quality on literary texts

---

### BERTopic

Pros:

* Better topic quality
* Strong semantic clustering

Cons:

* Requires transformer models
* Higher memory consumption
* Slower execution
* More complex pipeline

---

### Equal Section Splitting

Pros:

* Very easy implementation
* Works on every book

Cons:

* Ignores the actual structure of the book
* Topics may mix unrelated chapters

This approach is still used as a fallback when no chapter structure can be reliably detected.

---

LDA combined with automatic chapter detection was selected because it offers the best balance between quality, interpretability, speed, robustness and computational cost for this project.
