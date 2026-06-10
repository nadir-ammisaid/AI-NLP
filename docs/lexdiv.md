# Lexical Diversity

## Objective

The goal of lexical diversity analysis is to measure the richness and variety of vocabulary used in a book.

These metrics help characterize an author's writing style and compare books quantitatively.

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
    Tokenization
(split text into words)
          │
          ▼
 Stopwords Removal
(remove common words)
          │
          ▼
      POS Tagging
(assign grammatical roles)
          │
          ▼
    Lemmatization
(normalize words)
          │
          ▼
 Lexical Statistics
(tok, typ, hap,
ttr, mwl, mwf,
rttr, cttr,
herdan, maas)
          │
          ▼
     JSON Output
```

---

## Technical Choices

### Why lexical metrics?

Lexical metrics are simple, fast and interpretable indicators of vocabulary richness.

Examples:

* Total word count
* Unique vocabulary size
* Hapax count
* Type-Token Ratio (TTR)
* Mean word length
* Mean word frequency

These metrics are commonly used in stylometry and corpus linguistics.

---

### Why lemmatization?

Different forms of the same word can artificially inflate vocabulary size.

Examples:

* run
* runs
* running
* ran

Lemmatization groups these forms under a common base form, producing more meaningful lexical statistics.

---

### Why additional lexical metrics?

Traditional metrics such as TTR are useful but highly sensitive to text length.

Additional metrics provide complementary perspectives on lexical richness.

Implemented metrics:

* Root TTR (RTTR)
* Corrected TTR (CTTR)
* Herdan's C
* Maas's a²

These metrics are widely used in corpus linguistics to reduce the impact of text length.

---

## Metrics Returned

The project computes:

```text
tok     Total number of word tokens
typ     Number of unique word types
hap     Number of hapax legomena
ttr     Type-Token Ratio
mwl     Mean Word Length
mwf     Mean Word Frequency
rttr    Root Type-Token Ratio
cttr    Corrected Type-Token Ratio
herdan  Herdan's C
maas    Maas's a²
```

---

## Limitations

Lexical diversity metrics measure vocabulary richness rather than semantic meaning.

For example:

* Two books may have similar lexical diversity while discussing completely different topics.
* A book with simple vocabulary may still be highly engaging.
* Longer books naturally introduce more vocabulary variation.

Although RTTR, CTTR, Herdan's C and Maas's a² reduce text-length bias, no lexical metric is entirely independent from corpus size.

---

## Alternatives Considered

### MTLD

Pros:

* Highly robust to text length
* Widely used in linguistic research

Cons:

* More complex implementation
* Harder to explain during presentation

---

### MATTR

Pros:

* Stable across different book sizes
* Reduces corpus-size effects

Cons:

* Slightly slower computation
* Requires additional window-size tuning

---

### HD-D

Pros:

* Strong statistical robustness
* Popular in modern lexical diversity studies

Cons:

* More computationally expensive
* Less intuitive to explain

---

The selected metrics were chosen because they provide a good balance between simplicity, interpretability, computational efficiency and robustness while remaining easy to justify during the project presentation.
