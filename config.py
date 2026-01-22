from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LLAMA_ENDPOINT = os.getenv("LLAMA_ENDPOINT")

LLM_MODEL = "gpt-4.1-mini"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
FAISS_PATH = "vector_db/index"
