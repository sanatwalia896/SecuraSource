import subprocess
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import Config
from dotenv import load_dotenv
load_dotenv()

class ExecutionAgent:
    def __init__(self, command_flow):
        self.command_flow = command_flow
        self.llm = ChatGroq(api_key=Config.GROQ_API_KEY,model=Config.MODEL)
        
    def execute(self):
        results = []
        for cmd in self.command_flow.split('\n'):
            if cmd.strip():
                try:
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    results.append(f"Command: {cmd}\nOutput: {result.stdout}\nError: {result.stderr}")
                except Exception as e:
                    results.append(f"Command: {cmd}\nError: {str(e)}")
        
        prompt = ChatPromptTemplate.from_template(
            "Analyze these execution results for potential issues:\n{results}"
        )
        response = self.llm.invoke(prompt.format(results='\n'.join(results)))
        return response.content