import streamlit as st
from ingestion.youtube_loader import load_youtube
from ingestion.pdf_loader import load_pdf
from intelligence.summarizer import summarize

from processing.cleaner import clean
from processing.chunker import chunk_text
from processing.embedder import embed
from processing.vector_store import build, load, search
from intelligence.qa_rag import answer

from intelligence.comparer import compare

from intelligence.notes_generator import generate_notes, generate_flashcards

st.set_page_config(layout="wide")
st.title("AI Content Intelligence Platform")

mode = st.sidebar.selectbox("Mode", ["Single Content", "Compare Two Contents"])

provider = st.sidebar.selectbox(
    "LLM Provider",
    ["openai", "gemini", "llama"]
)


if mode == "Single Content":

    option = st.selectbox("Choose input", ["YouTube", "PDF"])
    text = None

    if "text" not in st.session_state:
        st.session_state.text = None

    if option == "YouTube":
        url = st.text_input("YouTube URL")
        if st.button("Process"):
            st.session_state.text = load_youtube(url)


    if option == "PDF":
        file = st.file_uploader("Upload PDF", type=["pdf"])
        if st.button("Process") and file:
            st.session_state.text = load_pdf(file)

    text = st.session_state.text

    if text:
        st.text_area("Extracted Text", text, height=250)

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Summarize"):
                st.markdown(summarize(text, provider))

        with col2:
            if st.button("Generate Notes"):
                st.markdown(generate_notes(text, provider))

        with col3:
            if st.button("Generate Flashcards"):
                st.markdown(generate_flashcards(text, provider))


        if st.button("Index for Intelligence"):
            if text:
                cleaned = clean(text)
                chunks = chunk_text(cleaned)
                vectors = embed(chunks)
                build(vectors, chunks)
                st.success("Content indexed into vector database!")
            else:
                st.error("Please process content first.")

    st.divider()
    st.subheader("Ask Questions About Your Content")
    question = st.text_input("Ask something about the content")
    if st.button("Ask") and question:
        idx, docs = load()
        result = answer(question, idx, docs, provider)
        st.markdown(result)


if mode == "Compare Two Contents":

    st.subheader("Compare Two Contents")
    col1, col2 = st.columns(2)

    with col1:
        url1 = st.text_input("YouTube URL A")
    with col2:
        url2 = st.text_input("YouTube URL B")

    if st.button("Process Both") and url1 and url2:
        st.session_state.text_a = load_youtube(url1)
        st.session_state.text_b = load_youtube(url2)
        st.success("Both contents processed")

    if "text_a" in st.session_state and "text_b" in st.session_state:
        st.text_area("Content A", st.session_state.text_a[:2000], height=200)
        st.text_area("Content B", st.session_state.text_b[:2000], height=200)

        if st.button("Compare"):
            result = compare(st.session_state.text_a, st.session_state.text_b, provider)
            st.subheader("Comparison Result")
            st.markdown(result)