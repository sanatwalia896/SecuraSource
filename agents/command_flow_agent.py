from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import Config
from dotenv import load_dotenv
load_dotenv()

class CommandFlowAgent:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = ChatGroq(api_key=Config.GROQ_API_KEY,model=Config.MODEL)
        
    def generate_commands(self):
        docs = self.vector_store.similarity_search("README.md OR setup.py OR package.json", k=3)
        prompt = ChatPromptTemplate.from_template(
            "Based on these project files, generate a sequence of commands to install and run the software:\n{docs}"
        )
        response = self.llm.invoke(prompt.format(docs=[doc.page_content for doc in docs]))
        return response.content