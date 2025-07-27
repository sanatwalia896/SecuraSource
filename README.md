
## 🛡️ SecuraSource

### 🔍 AI-Powered Open Source Vulnerability Detection Tool

SecuraSource is an intelligent, agent-based vulnerability scanning system designed to analyze open-source software repositories. It uses a combination of **LLM agents**, **system monitoring**, and **automated execution** to detect potentially dangerous code patterns, command flows, system-level changes, and more — producing a comprehensive security report.

---

### 🚀 Features

* ✅ **Agent-Based Architecture** using [LangGraph](https://github.com/langchain-ai/langgraph)
* 📄 **Documentation Understanding** via embeddings + LLMs
* 🧠 **Command Flow Reconstruction**
* 🧪 **Safe Execution Monitoring** (Pre/Post system state analysis)
* 🔍 **Code Review Agent** (LLM-assisted)
* 📝 **Automated Report Generation**
* 🌐 **Streamlit UI** for easy interaction
* 🔐 Built with **Groq LLMs** for ultra-fast and efficient reasoning

---

### 🧰 Tech Stack

| Component    | Technology                 |
| ------------ | -------------------------- |
| Language     | Python 3.11                |
| UI Framework | Streamlit                  |
| Agents       | LangGraph + LangChain      |
| LLM Provider | Groq (Mixtral / LLaMA3)    |
| Embeddings   | HuggingFace Transformers   |
| Vector Store | FAISS (in-memory)          |
| Repo Parsing | Git + Python FS Handling   |
| Monitoring   | Custom SystemMonitor class |

---

### 📦 Installation

```bash
git clone https://github.com/yourusername/SecuraSource.git
cd SecuraSource
pip install -r requirements.txt
```

Make sure you have Python 3.11+ installed.

---

### 🔐 Setup

Create a `.env` file at the root of your project:

```env
GROQ_API_KEY=your_groq_api_key
MODEL=llama3-8b-8192  # or mixtral-8x7b
```

---

### 🧑‍💻 How It Works

1. Clone and analyze a GitHub repository
2. Build vector index for the repo
3. Run documentation analysis
4. Generate likely command flows
5. Monitor pre/post system state
6. Execute code in isolated environment
7. Perform LLM-driven code review
8. Generate detailed report with vulnerabilities, suggestions, and findings

---

### 📸 UI Preview

![SecuraSource UI Preview](https://via.placeholder.com/900x400?text=Screenshot+coming+soon)

---

### 🧪 Sample Output

```
Repository: example-nodejs-app
Detected Risks:
- Uses outdated dependency (express 3.x)
- Writes to system logs without sanitization
- Uses hardcoded credentials in config.js

Suggestions:
- Upgrade express to 4.x or higher
- Sanitize inputs before logging
- Move secrets to environment variables
```

---

### 🛠️ Project Structure

```
SecuraSource/
│
├── app.py                     # Main Streamlit App
├── config.py                  # API keys & config
├── agents/                    # Modular agents
│   ├── documentation_agent.py
│   ├── command_flow_agent.py
│   ├── execution_agent.py
│   ├── code_review_agent.py
│   ├── report_agent.py
│   └── system_monitor_agent.py
│
├── utils/                     # Helpers
│   ├── system_monitor.py
│   └── vector_store.py
│
├── data/                      # Cloned repositories
├── requirements.txt
└── README.md
```

---

### 🙌 Acknowledgements

* [LangChain](https://www.langchain.com/)
* [LangGraph](https://github.com/langchain-ai/langgraph)
* [Streamlit](https://streamlit.io/)
* [Groq](https://groq.com/)
* [FAISS](https://github.com/facebookresearch/faiss)

---

### 📜 License

This project is under the MIT License — feel free to fork, enhance, and use in your own research!

---

### 🤝 Contribute

Found a bug? Have a feature idea? Pull requests and issues are welcome!




