from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from transformers import pipeline

def build_rag():

    # Load policy text manually
    with open("app/data/policies.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Vector store
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Lightweight LLM (Laptop Friendly)
    generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=256
)

    llm = HuggingFacePipeline(pipeline=generator)

    # Retrieval QA
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa