import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    DATA_DIR = "./data/repos"
    MODEL=os.getenv("MODEL","gemma2-9b-it")