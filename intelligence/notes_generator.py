from config import LLM_MODEL
from intelligence.llm_router import run_llm

def generate_notes(text, provider):
    prompt = open("prompts/notes.txt").read().format(context=text[:8000])
    return run_llm(prompt, provider, LLM_MODEL)

def generate_flashcards(text, provider):
    prompt = open("prompts/flashcards.txt").read().format(context=text[:8000])
    return run_llm(prompt, provider, LLM_MODEL)
