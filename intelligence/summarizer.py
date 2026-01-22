from config import LLM_MODEL
from intelligence.llm_router import run_llm

def summarize(text, provider):
    prompt = open("prompts/summary.txt").read().format(context=text[:8000])
    return run_llm(prompt, provider, LLM_MODEL)
