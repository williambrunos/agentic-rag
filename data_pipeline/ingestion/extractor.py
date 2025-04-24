import os
import datasets
from dotenv import load_dotenv

from llama_index.core import Settings
from llama_index.core.schema import Document
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from llama_index.core.storage.storage_context import StorageContext

# Carrega .env
load_dotenv()

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def load_guest_documents() -> list[Document]:
    guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")
    docs = []
    for i in range(len(guest_dataset)):
        text = "\n".join([
            f"Name: {guest_dataset['name'][i]}",
            f"Relation: {guest_dataset['relation'][i]}",
            f"Description: {guest_dataset['description'][i]}",
            f"Email: {guest_dataset['email'][i]}"
        ])
        docs.append(Document(text=text, metadata={"name": guest_dataset['name'][i]}))
    return docs

def build_embeddings_index(
    documents: list[Document],
    qdrant_host: str = os.getenv("QDRANT_HOST", "localhost"),
    qdrant_port: int = int(os.getenv("QDRANT_PORT", 6333)),
    collection_name: str = os.getenv("QDRANT_COLLECTION", "guest_docs")
) -> None:
    client = QdrantClient(host=qdrant_host, port=qdrant_port)

    sample = Settings.embed_model.get_text_embedding(documents[0].text)
    vector_size = len(sample)

    existing = client.get_collections().collections
    if collection_name not in [c.name for c in existing]:
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config={"size": vector_size, "distance": "Cosine"}
        )

    vector_store = QdrantVectorStore(client=client, collection_name=collection_name)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_documents(
        documents, 
        storage_context=storage_context,
        show_progress=True,
    )
    print(f"Index criado na coleção '{collection_name}' do Qdrant.")

if __name__ == "__main__":
    documents = load_guest_documents()
    build_embeddings_index(documents)
