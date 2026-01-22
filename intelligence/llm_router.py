import requests
from openai import OpenAI
from config import OPENAI_API_KEY, GEMINI_API_KEY, LLAMA_ENDPOINT

def call_openai(prompt, model):
    client = OpenAI(api_key=OPENAI_API_KEY)
    res = client.chat.completions.create(
        model=model,
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
    )
    return res.choices[0].message.content

def call_gemini(prompt):
    try:
        import google.generativeai as genai  
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        res = model.generate_content(prompt)
        return res.text
    except Exception as e:
        return f"Gemini not available. Error: {e}"


def call_llama(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    res = requests.post(LLAMA_ENDPOINT, json=payload).json()
    return res["response"]

def run_llm(prompt, provider, model):
    if provider == "openai":
        return call_openai(prompt, model)
    elif provider == "gemini":
        return call_gemini(prompt)
    elif provider == "llama":
        return call_llama(prompt)
    else:
        raise ValueError("Unknown LLM provider")
