# Book Summarization

## Objective

The goal of summarization is to provide a concise overview of a book without requiring users to read the full text.

The implementation uses an extractive summarization approach based on semantic embeddings.

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
 Paragraph Extraction
          │
          ▼
 Sentence Embeddings
(all-MiniLM-L6-v2)
          │
          ▼
 Document Centroid
(mean embedding)
          │
          ▼
 Cosine Similarity
(score paragraphs)
          │
          ▼
 Ranking
(most representative paragraphs)
          │
          ▼
 Top-K Selection
          │
          ▼
 Extractive Summary
```

---

## Technical Choices

### Why extractive summarization?

Extractive methods select important passages directly from the original text.

Advantages:

* Fast execution
* Deterministic output
* No hallucinations
* Lightweight computation
* Preserves the author's original wording

This approach fully complies with the project constraints prohibiting large generative models.

---

### Why sentence embeddings?

Traditional keyword-based methods often struggle to capture semantic meaning.

Embeddings represent paragraphs as dense vectors encoding semantic information.

This allows the algorithm to identify passages that best represent the overall content of the book rather than simply selecting the most frequent words.

---

### Why MiniLM?

The project uses:

```text
all-MiniLM-L6-v2
```

Advantages:

* Lightweight model
* Fast inference
* Small memory footprint
* Good semantic representation quality
* Suitable for local execution

This model is significantly lighter than large transformer architectures while maintaining strong semantic performance.

---

### Why centroid-based ranking?

Each paragraph embedding is compared to the average embedding of the entire book.

The centroid acts as a semantic representation of the global content.

Paragraphs with the highest cosine similarity to the centroid are considered the most representative and are selected for the summary.

Advantages:

* Simple implementation
* Fast computation
* Deterministic results
* Good global coverage of the book

---

## Limitations

Extractive summaries reuse original paragraphs.

Consequently:

* Summaries may be long.
* Redundant information may appear.
* Narrative flow is not always preserved.
* Selected paragraphs may contain dialogue without surrounding context.
* The algorithm does not rewrite or simplify text.

The system identifies representative content but does not generate new sentences.

---

## Alternatives Considered

### TextRank

Pros:

* Popular summarization algorithm
* Graph-based approach
* No embedding model required

Cons:

* More sensitive to local sentence structure
* Can miss globally important passages

---

### LexRank

Pros:

* Robust graph-based ranking
* Well-established approach

Cons:

* More computationally expensive
* Similar limitations to TextRank

---

### Clustering-Based Summarization

Pros:

* Good thematic coverage
* Can reduce redundancy

Cons:

* More complex implementation
* Requires additional parameter tuning

---

### Abstractive Summarization

Pros:

* More natural summaries
* Better readability

Cons:

* Requires large transformer models
* Higher resource consumption
* Risk of hallucinations
* Not compliant with project constraints

---

The embedding-based extractive approach was selected because it provides the best balance between quality, speed, simplicity and resource consumption while remaining fully compliant with the project's lightweight NLP requirements.
