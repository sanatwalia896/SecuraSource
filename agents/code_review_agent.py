from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import Config
from dotenv import load_dotenv
load_dotenv()

class CodeReviewAgent:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = ChatGroq(api_key=Config.GROQ_API_KEY,model=Config.MODEL)
        
    def review_code(self):
        docs = self.vector_store.similarity_search("*.py OR *.js OR *.java OR *.cpp OR *.c", k=10)
        prompt = ChatPromptTemplate.from_template(
            """Review this code for potential vulnerabilities, missing dependencies, and coding errors:
            {code}
            Check for:
            1. Security vulnerabilities
            2. Missing dependencies
            3. Code quality issues
            4. Best practices violations"""
        )
        response = self.llm.invoke(prompt.format(code=[doc.page_content for doc in docs]))
        return response.content