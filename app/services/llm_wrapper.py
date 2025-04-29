import os
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI

load_dotenv()

OPENAI_API_KEY     = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL       = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")  # ou "gpt-4"
LLM_TEMPERATURE    = float(os.getenv("LLM_TEMPERATURE", 0.1))
LLM_MAX_TOKENS     = int(os.getenv("LLM_MAX_TOKENS", 512))


llm = OpenAI(
    model=OPENAI_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=LLM_TEMPERATURE,
    max_tokens=LLM_MAX_TOKENS
)