import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.core.tools import FunctionTool
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "guest_docs")
TOP_K = int(os.getenv("TOP_K", 3))

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def retrieve_docs(query: str) -> str:
    """
    This function retrieves documents from a Qdrant vector store based on a query.
    Args:
        query (str): The query string to search for.
    Returns:
        str: A formatted string containing the retrieved documents.
    """
    # Conecta ao Qdrant
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME
    )
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    retriever = index.as_retriever(similarity_top_k=TOP_K)
    results = retriever.retrieve(query)

    if results:
        return "\n\n".join([doc.text for doc in results])
    else:
        return "No matching guest information found."
    

# Define a tool for the agent
perform_retrieval_tool = FunctionTool.from_defaults(
    retrieve_docs,
    name="retrieve_docs",
    description="Retrieve documents from the Qdrant vector store based on a query."
)