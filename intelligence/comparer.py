from config import LLM_MODEL
from intelligence.llm_router import run_llm

def compare(text_a, text_b, provider):
    prompt = open("prompts/compare.txt").read().format(a=text_a[:6000], b=text_b[:6000])
    return run_llm(prompt, provider, LLM_MODEL)
