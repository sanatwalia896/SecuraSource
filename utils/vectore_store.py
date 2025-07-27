from langchain_community.document_loaders import GitLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import Config

def create_vector_store(repo_path):
    loader = GitLoader(
        repo_path=repo_path,
        branch="main",
        file_filter=lambda x: x.endswith(('.py', '.js', '.java', '.cpp', '.c', '.md', 'LICENSE'))
    )
    documents = loader.load()
    
    embeddings = HuggingFaceEmbeddings(
        model_name=Config.EMBEDDING_MODEL,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True},
        huggingfacehub_api_token=Config.HUGGINGFACE_TOKEN
    )
    
    vector_store = Chroma.from_documents(documents, embeddings)
    return vector_store, documents