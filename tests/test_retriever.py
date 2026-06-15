from rag.retriever import get_relevant_chunks

docs = get_relevant_chunks(
    "What is Tesla revenue?"
)
for doc in docs:
    print(doc.page_content)