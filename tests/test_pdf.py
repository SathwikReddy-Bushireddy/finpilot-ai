from rag.pdf_loader import load_pdf
from rag.text_splitter import split_documents

docs=load_pdf("uploads/sample.pdf")
print("Pages:",len(docs))
chunks=split_documents(docs)
print("Chunks:", len(chunks))
print(chunks[0].page_content[:500])