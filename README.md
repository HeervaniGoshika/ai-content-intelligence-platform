# AI Content Intelligence Platform

An end-to-end GenAI system that understands YouTube videos, PDFs, audio,
and text, and provides summarization, notes, flashcards, semantic
search, RAG Q&A, comparison, and multi-LLM support.

------------------------------------------------------------------------

## Features

-   YouTube → audio → Whisper transcription
-   PDF, audio, URL and text ingestion
-   Chunking + embeddings + FAISS vector store
-   RAG-based Q&A
-   Notes & flashcards generation
-   Comparison mode (two contents)
-   Multi-LLM: OpenAI, Gemini, LLaMA (Ollama)

------------------------------------------------------------------------

## Tech Stack

-   Python, Streamlit
-   Whisper / Faster-Whisper
-   SentenceTransformers
-   FAISS
-   OpenAI, Gemini, Ollama (LLaMA)
-   RAG, Vector Search
-   Docker

------------------------------------------------------------------------

## Folder Structure

    ai_content_platform/
    │
    ├── app.py
    ├── config.py
    ├── requirements.txt
    │
    ├── ingestion/
    ├── processing/
    ├── intelligence/
    ├── prompts/
    └── vector_db/

------------------------------------------------------------------------

## Setup (Local)

``` bash
git clone <your-repo-url>
cd ai-content-platform
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` file:

``` env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
LLAMA_ENDPOINT=http://localhost:11434/api/generate
```

Run:

``` bash
streamlit run app.py
```

Open:

    http://localhost:8501

------------------------------------------------------------------------

## Using LLaMA (Optional)

Install Ollama: https://ollama.com

``` bash
ollama run llama3
```

Keep it running while using provider = llama.

------------------------------------------------------------------------

## Docker

Build image:

``` bash
docker build -t ai-content-platform .
```

Run:

``` bash
docker run -p 8501:8501 --env-file .env ai-content-platform
```

------------------------------------------------------------------------

## Cloud Deployment

### Streamlit Cloud

1.  Push to GitHub\
2.  Go to https://share.streamlit.io\
3.  Connect repo\
4.  Add secrets (API keys)\
5.  Deploy

### Render / Railway / Fly.io

-   Use Dockerfile
-   Add env variables in dashboard
-   Deploy

------------------------------------------------------------------------

## Use Cases

-   Study assistant
-   Research assistant
-   Content analysis
-   Interview preparation
-   Knowledge management

------------------------------------------------------------------------

