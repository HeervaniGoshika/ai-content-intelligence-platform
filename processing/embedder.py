from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL
import numpy as np

model = SentenceTransformer(EMBED_MODEL)

def embed(texts):
    return np.array(model.encode(texts)).astype("float32")
