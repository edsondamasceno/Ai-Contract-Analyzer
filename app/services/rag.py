from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

vectorstore = None

def index_documents(texts):
    global vectorstore
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts, embeddings)


def retrieve(query):
    return vectorstore.similarity_search(query)