from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import Config
from dotenv import load_dotenv
load_dotenv()

class DocumentationAgent:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = ChatGroq(api_key=Config.GROQ_API_KEY,model=Config.MODEL)
        
    def analyze_docs(self):
        docs = self.vector_store.similarity_search("README.md and LICENSE", k=5)
        prompt = ChatPromptTemplate.from_template(
            "Analyze these documents and summarize key information about the project and its license:\n{docs}"
        )
        response = self.llm.invoke(prompt.format(docs=[doc.page_content for doc in docs]))
        return response.content