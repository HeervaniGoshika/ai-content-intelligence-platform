from intelligence.llm_router import run_llm
from processing.embedder import embed
from processing.vector_store import search

def answer(question, index, docs, provider):
    q_vec = embed([question])[0]
    top_chunks = search(q_vec, index, docs)
    context = "\n".join(top_chunks)
    prompt = open("prompts/qa.txt").read().format(context=context, question=question)
    return run_llm(prompt, provider, LLM_MODEL)
