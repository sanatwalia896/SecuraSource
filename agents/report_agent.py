from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import Config
from dotenv import load_dotenv
load_dotenv()

class ReportAgent:
    def __init__(self):
        self.llm = ChatGroq(api_key=Config.GROQ_API_KEY,model=Config.MODEL)
        
    def generate_report(self, doc_analysis, command_flow, system_changes, code_review, execution_results):
        prompt = ChatPromptTemplate.from_template(
            """Generate a detailed vulnerability report based on:
            Documentation: {doc_analysis}
            Command Flow: {command_flow}
            System Changes: {system_changes}
            Code Review: {code_review}
            Execution Results: {execution_results}
            
            Include:
            1. Project Overview
            2. Security Findings
            3. Recommendations
            4. System Impact Analysis
            5. Execution Issues"""
        )
        response = self.llm.invoke(prompt.format(
            doc_analysis=doc_analysis,
            command_flow=command_flow,
            system_changes=system_changes,
            code_review=code_review,
            execution_results=execution_results
        ))
        return response.content