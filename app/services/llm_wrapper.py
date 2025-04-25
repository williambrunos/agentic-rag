from llama_index.llms.ollama import Ollama
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

MODEL_NAME = os.getenv("LLAMA_MODEL", "llama3.2")
LLM_TEMPERATURE = float(os.getenv("LLAMA_TEMPERATURE", 0.1))
REQUEST_LLM_TIMEOUT = float(os.getenv("LLAMA_REQUEST_TIMEOUT", 120.0))


llm = Ollama(
        model=MODEL_NAME,
        temperature=LLM_TEMPERATURE,
        request_timeout=REQUEST_LLM_TIMEOUT
)