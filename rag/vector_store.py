from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

def create_vector_store(chunks):
    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )
    return vector_db

def save_vector_store(vector_db):
    vector_db.save_local(
        "faiss_index"
    )

def load_vector_store():
    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )