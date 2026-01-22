import faiss, os, pickle
from config import FAISS_PATH
import numpy as np


index = None
stored_docs = []

def build(vectors, docs):
    global index, stored_docs
    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    stored_docs = docs
    os.makedirs(os.path.dirname(FAISS_PATH), exist_ok=True)
    faiss.write_index(index, FAISS_PATH)
    with open(FAISS_PATH + ".pkl", "wb") as f:
        pickle.dump(stored_docs, f)

def load():
    if not os.path.exists(FAISS_PATH):
        return None, None
    idx = faiss.read_index(FAISS_PATH)
    with open(FAISS_PATH + ".pkl", "rb") as f:
        docs = pickle.load(f)
    return idx, docs

def search(query_vector, index, docs, k=3):
    q = np.array(query_vector).reshape(1, -1).astype("float32")
    D, I = index.search(q, k)
    return [docs[i] for i in I[0]]
