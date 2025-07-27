import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROK_API_KEY = os.getenv("GROK_API_KEY")
    HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    DATA_DIR = "./data/repos"