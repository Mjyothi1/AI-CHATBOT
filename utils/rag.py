import faiss
import numpy as np
from models.embeddings import get_embedding_model

docs = [
    "AI is transforming healthcare",
    "Machine learning helps predict diseases",
    "Chatbots improve customer support"
]

model = get_embedding_model()
embeddings = model.encode(docs)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

def retrieve(query):
    q = model.encode([query])
    D, I = index.search(np.array(q), k=1)
    return docs[I[0][0]]
