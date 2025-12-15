# Ollama LLM Chatbot with Streamlit

A simple yet powerful chatbot application powered by Ollama's Llama3 model, built with Streamlit and LangChain for local LLM inference.

## 🚀 Features

- **Local LLM Inference**: Run Llama3 locally via Ollama (no API costs!)
- **Interactive UI**: Clean Streamlit interface for chat interactions
- **LangChain Integration**: Modular prompt templates and output parsing
- **LangSmith Tracing**: Optional monitoring and debugging (requires LangChain API key)
- **Privacy-Focused**: All processing happens locally on your machine

## 📋 Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai/) installed on your system
- 8GB+ RAM recommended for Llama3 model
- Virtual environment (recommended)

## 🔧 Installation

### 1. Install Ollama

**Windows/Mac/Linux:**
```bash
# Visit https://ollama.ai/download and install for your OS
# Or use the command line:
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. Pull the Llama3 model

```bash
ollama pull llama3
```

### 3. Clone and Setup Project

```bash
git clone <your-repo-url>
cd "Gen ai"
```

### 4. Create and activate virtual environment

```bash
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root:

```env
# Optional: For LangSmith tracing/monitoring
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=ollama-chatbot

# Optional: Hugging Face API key (if needed for other features)
HF_API_KEY=your_huggingface_key_here
```

**Note:** The app will work without these keys, but LangSmith tracing will be disabled.

## ▶️ Usage

### Start the chatbot:

```bash
streamlit run ollama_app.py
```

The app will open in your browser at `http://localhost:8501`

### Using the chatbot:

1. Enter your question in the text input field
2. Press Enter or click outside the input box
3. The chatbot will process your query using the local Llama3 model
4. Response appears below the input field

### Example Queries:

- "Explain quantum computing in simple terms"
- "Write a Python function to sort a list"
- "What are the benefits of renewable energy?"
- "Summarize the history of artificial intelligence"

## 📁 Project Structure

```
Gen ai/
├── ollama_app.py          # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── README.md             # This file
└── .venv/                # Virtual environment (excluded from Git)
```

## 🛠️ Tech Stack

- **Streamlit**: Interactive web UI framework
- **LangChain**: LLM orchestration and prompt management
- **Ollama**: Local LLM inference engine
- **Llama3**: Meta's open-source language model
- **Python-dotenv**: Environment variable management

## ⚙️ Configuration

### Change the Model

Edit line 25 in `ollama_app.py`:

```python
# Use different Ollama models
model = OllamaLLM(model="llama3")      # Default
model = OllamaLLM(model="llama2")      # Llama 2
model = OllamaLLM(model="mistral")     # Mistral
model = OllamaLLM(model="codellama")   # Code Llama
```

### Customize the System Prompt

Modify the prompt template in `ollama_app.py`:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Your custom system message here"),
    ("user", "Question:{input}"),
])
```

## 🐛 Troubleshooting

### Error: "Ollama connection failed"
- Ensure Ollama is running: `ollama serve`
- Verify model is installed: `ollama list`
- Check if port 11434 is available

### Error: "Model not found"
- Pull the model: `ollama pull llama3`
- List available models: `ollama list`

### Slow responses
- Llama3 requires significant RAM (8GB+)
- Try smaller models: `ollama pull llama2` or `mistral`
- Close other memory-intensive applications

### Import errors
- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

## 🎯 Key Dependencies

```
streamlit              # Web UI framework
langchain-ollama       # Ollama integration for LangChain
langchain-core         # Core LangChain components
python-dotenv          # Environment variable loading
```

## 🔒 Privacy & Security

- All LLM inference runs **locally** on your machine
- No data sent to external APIs (unless LangSmith tracing is enabled)
- `.env` file excluded from Git via `.gitignore`

## 📈 Performance Tips

1. **Use GPU acceleration** if available (Ollama supports CUDA)
2. **Adjust model size** based on your hardware
3. **Limit input length** for faster responses
4. **Keep Ollama updated** for performance improvements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) for local LLM inference
- [LangChain](https://langchain.com) for LLM orchestration
- [Streamlit](https://streamlit.io) for the UI framework
- [Meta AI](https://ai.meta.com) for Llama3

## 📧 Support

For issues or questions:
- Open an issue on GitHub
- Check [Ollama documentation](https://github.com/ollama/ollama)
- Visit [LangChain docs](https://python.langchain.com)

---

**Note**: This chatbot runs entirely on your local machine. No internet connection required after initial setup (except for optional LangSmith tracing).
