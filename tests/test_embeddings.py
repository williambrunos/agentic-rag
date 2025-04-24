import os
from dotenv import load_dotenv

from data_pipeline.ingestion.extractor import load_guest_documents, build_embeddings_index
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from llama_index.core import Settings, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "guest_docs")


def test_vector_store_contains_docs():
    documents = load_guest_documents()
    build_embeddings_index(documents)

    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION_NAME)
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    retriever = index.as_retriever(similarity_top_k=3)
    results = retriever.retrieve("Who are the historical guests?")
    assert results, "Nenhum documento retornado!"
    for node in results:
        print(f"\n\Result: \n{node}\n\n")


    client = QdrantClient(host="localhost", port=6333)
    scroll_result = client.scroll(
        collection_name="guest_docs",
        limit=100
    )
    
    print(scroll_result)


if __name__ == "__main__":
    test_vector_store_contains_docs()
