import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

# Carrega variáveis de ambiente
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)


def test_vector_store():
    client = QdrantClient(host="localhost", port=6333)
    scroll_result = client.scroll(
        collection_name="guest_docs",
        limit=100
    )
    
    print(scroll_result)


if __name__ == "__main__":
    test_vector_store()
