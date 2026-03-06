from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
with open("documents.txt", "r") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

# Encode documents
doc_embeddings = model.encode(documents)

# Load queries
with open("queries.txt", "r") as f:
    queries = [line.strip() for line in f.readlines() if line.strip()]

results = []

for query in queries:

    # Encode query
    query_embedding = model.encode([query])

    # Compute similarity
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    # Get most relevant document
    best_index = np.argmax(similarities)
    best_doc = documents[best_index]

    output = f"Query: {query}\nRetrieved Document:\n{best_doc}\n---\n"
    print(output)
    results.append(output)

# Save results
with open("results.txt", "w") as f:
    f.writelines(results)