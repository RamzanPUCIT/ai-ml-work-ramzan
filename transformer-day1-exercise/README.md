# Day 1 — Transformer & Attention Exercise

This repository contains:
- A conceptual write-up on Generative AI, self-attention, encoder vs decoder, and Vision Transformers (ViT).
- A clean NumPy implementation of scaled dot-product attention.

---

## 1️⃣ What is Generative AI?

Generative AI refers to models that create new content, such as text, images, audio, or code, by learning patterns from data. Unlike traditional machine learning models that mainly perform classification or regression (predicting labels or numeric values), generative models learn the underlying distribution of data and can generate new samples similar to what they were trained on.

Traditional ML models are usually discriminative — they learn decision boundaries between classes. Generative AI models, however, try to model how the data is formed so they can produce new, realistic outputs.

Modern Generative AI systems are powered by Transformer architectures, especially in language tasks. These models generate outputs step-by-step by predicting the next token based on previous context.

### Real-world Applications:
1. Conversational assistants (Chatbots, AI copilots)
2. Content generation (summarization, translation, report writing)
3. Image and media generation tools

---

## 2️⃣ Self-Attention Explained

Sentence: **"The cat sat on the mat"**

Self-attention allows each word in a sentence to look at every other word to decide which ones are important.

### Query (Q), Key (K), Value (V)

- Query (Q): What the word is looking for.
- Key (K): What the word contains.
- Value (V): The actual information passed forward.

Each word creates Q, K, and V vectors. We compute the similarity between a word's Query and all Keys to determine attention weights.

### Why scale by √dₖ?

As vector dimensions increase, dot product values become large, pushing softmax into extreme regions. Dividing by √dₖ keeps values stable and improves gradient behavior.

### Why apply Softmax?

Softmax converts similarity scores into probabilities that sum to 1. This ensures we compute a weighted average of Value vectors.

### What problem does Attention solve vs RNNs?

RNNs process words sequentially, making long-range dependencies difficult to learn and limiting parallel computation. Self-attention connects all words directly and allows full parallelization.

---

## 3️⃣ Encoder vs Decoder Comparison

| Component | Encoder | Decoder |
|------------|----------|----------|
| Purpose | Builds contextual representation | Generates sequence |
| Self-Attention | Full attention | Masked attention |
| Masked Attention | Not required | Prevents looking at future tokens |
| Cross-Attention | Not used in encoder-only models | Used to attend encoder outputs |
| Use Case | Understanding tasks | Text generation |

Masked attention ensures a token cannot see future tokens during training.

Cross-attention allows the decoder to attend to the encoder outputs in sequence-to-sequence tasks like translation.

---

## 4️⃣ Vision Transformers (ViT)

Vision Transformers apply the Transformer architecture to images. Instead of words, images are split into fixed-size patches (e.g., 16×16 pixels). Each patch is flattened into a vector and projected into an embedding space. These embeddings act as tokens.

Since Transformers do not inherently understand position, positional embeddings are added to retain spatial information. Without positional embeddings, the model would treat patches as unordered.

Unlike CNNs, which use convolution filters and local receptive fields, ViTs allow every patch to attend to every other patch using self-attention. This enables global context modeling from early layers. CNNs have built-in inductive biases (like locality and translation invariance), while ViTs rely more on data and attention mechanisms.

---

## How to Run

```bash
pip install -r requirements.txt
python attention_demo.py
