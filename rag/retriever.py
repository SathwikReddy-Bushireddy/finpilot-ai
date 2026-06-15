import os
from rag.vector_store import load_vector_store

def get_relevant_chunks(query):
    # Check if faiss_index exists
    index_path = "faiss_index"
    if not os.path.exists(index_path):
        return []
    
    db = load_vector_store()
    docs = db.similarity_search(
        query,
        k=4
    )

    return docs
