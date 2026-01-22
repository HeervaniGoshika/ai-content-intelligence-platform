
# 🧠 AI Content Intelligence Platform

An end-to-end **GenAI-powered system** that understands YouTube videos, PDFs, audio, and text, and provides intelligent outputs like summaries, notes, flashcards, semantic search, RAG-based Q&A, content comparison, and multi-LLM support.

---

## Key Features ✨

- 🎥 YouTube → Audio → Whisper transcription  
- 📄 PDF, audio, URL, and text ingestion  
- 🧩 Intelligent text chunking  
- 🔎 Semantic search using embeddings + FAISS  
- 🧠 RAG-based Question Answering  
- 📝 Notes & flashcards generation  
- 🔁 Comparison mode (two contents)  
- 🤖 Multi-LLM support (OpenAI, Gemini, LLaMA)  

---

## Technology Stack 🛠️

- **Language**: Python  
- **UI**: Streamlit  
- **LLMs**: OpenAI, Gemini, LLaMA (Ollama)  
- **Speech-to-Text**: Whisper / Faster-Whisper  
- **Embeddings**: SentenceTransformers  
- **Vector DB**: FAISS  
- **GenAI Patterns**: RAG, Prompt Engineering  
- **Deployment**: Docker, Streamlit Cloud  

---

## 🚀 Setup and Installation

### Prerequisites

Make sure you have the following installed:

- **Python 3.11+**
- **FFmpeg** (installed and added to your system PATH)

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Content-Intelligence-Platform.git
cd AI-Content-Intelligence-Platform
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

This project supports multiple LLM providers.

Create a file named .env in the root directory of the project.

Add your API keys as shown below:

    ```env
    OPENAI_API_KEY="your-openai-api-key"
    GEMINI_API_KEY="your-gemini-api-key"
    GROQ_API_KEY="your-groq-api-key"

    # Optional (for local LLaMA via Ollama)
    LLAMA_ENDPOINT=http://localhost:11434/api/generate

    ```

## ▶️ How to Run the Application

Once the setup is complete, start the Streamlit app using:

```bash
streamlit run app.py
```

A new tab should open in your web browser at `http://localhost:8501`.

## How to Use the App

1. **Select Content Source**: In the sidebar, choose the content type such as **YouTube URL**, **PDF**, **Audio**, or **Text**.

2. **Provide the Content**:
   * For YouTube, paste the video URL.
   * For PDFs or audio, upload the file from your system.
   * For text, paste the content directly.

3. **Process the Content**:  
   The application will extract text (transcription if needed), clean and chunk the content, generate embeddings, and build a FAISS vector store. Progress will be shown in the interface.

4. **Choose an Action**:
   * Generate a **Summary**
   * Create **Notes**
   * Generate **Flashcards**
   * **Index for Intelligence** to enable question answering

5. **Ask a Question**:  
   Once indexing is complete, use the input box to ask questions about the content using RAG-based retrieval.

6. **View Intelligent Answers**:  
   The AI will return context-aware answers grounded in the original content.

7. **Compare Contents (Optional)**:  
   Switch to **Comparison Mode** to analyze similarities, differences, and gaps between two pieces of content.

8. **Switch LLM Providers (Optional)**:  
   Use the sidebar to switch between **OpenAI**, **Gemini**, or **LLaMA** and compare responses.
