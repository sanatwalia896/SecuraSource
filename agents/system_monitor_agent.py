from utils.system_monitor import SystemMonitor
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import Config

from dotenv import load_dotenv
load_dotenv()

class SystemMonitorAgent:
    def __init__(self):
        self.monitor = SystemMonitor()
        self.llm = ChatGroq(api_key=Config.GROQ_API_KEY,model=Config.MODEL)
        
    def monitor_execution(self):
        self.monitor.capture_initial_state()
        # Execution happens in ExecutionAgent
        changes = self.monitor.get_changes()
        prompt = ChatPromptTemplate.from_template(
            "Analyze these system changes after software execution:\n{changes}"
        )
        response = self.llm.invoke(prompt.format(changes=str(changes)))
        return {"system_changes": response.content}