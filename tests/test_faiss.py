from rag.pdf_loader import load_pdf
from rag.text_splitter import split_documents
from rag.vector_store import create_vector_store

docs = load_pdf(
    "uploads/sample.pdf"
)
chunks = split_documents(docs)
db = create_vector_store(chunks)
print("Vector DB Created")