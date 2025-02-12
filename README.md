# 🤖 Chatbot Application Using LangChain

![LangChain](https://img.shields.io/badge/LangChain-Chatbot-blue.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg) ![MLOps](https://img.shields.io/badge/MLOps-Deployment-red.svg)

A comprehensive project demonstrating the power of LangChain for building advanced chatbot applications, leveraging RAG (Retrieval-Augmented Generation) pipelines, multiple data sources, and deployment using Chain as an API. The project also integrates the **Groq Inference Engine** and **Hugging Face models**.

## 📖 Overview
This project aims to explore the capabilities of **LangChain** for chatbot development. It covers the full spectrum from basic chatbot implementation to advanced retrieval-augmented generation (RAG) pipelines. The project is designed for developers and researchers looking to enhance chatbot intelligence with multiple data sources and cutting-edge inference technologies.

## 🚀 Features

- **Basic Chatbot**: Implement a simple chatbot using LangChain.
- **Chain as API**: Deploy LangChain chains as APIs for seamless integration.
- **Basic RAG Pipeline**: Build a fundamental retrieval-augmented generation (RAG) pipeline.
- **Advanced RAG Pipeline**: Enhance the RAG pipeline for improved responses.
- **Multi-Source RAG**: Implement RAG with multiple data sources.
- **End-to-End LangChain Project**: Utilize **Groq Inference Engine** for optimized processing.
- **Hugging Face Integration**: Leverage pre-trained models from **Hugging Face** with LangChain.

## 📌 Tech Stack

- **LangChain**
- **Python (3.8+)**
- **FastAPI**  (for API deployment)
- **DVC** (for data versioning)
- **Groq Inference Engine**
- **Hugging Face Transformers**

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/langchain-chatbot.git
   cd langchain-chatbot
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. Start the API server:
   ```bash
   python app.py  # or `uvicorn app:app --reload` for FastAPI
   ```
2. Access the chatbot API at `http://127.0.0.1:8000`.

## 📂 Project Structure
```
langchain-chatbot/
│── agents/
│   ├── agents.ipynb           # Notebook for LangChain agents
│── api/
│   ├── api.py                 # API implementation
│   ├── client.py              # API client
│── chatbot/
│   ├── app.py                 # Chatbot application
│── groq/
│   ├── appp.py                # Groq inference engine integration
│── HuggingFace/
│   ├── huggingface.ipynb      # Hugging Face model integration
│   ├── us_cen/                # Data sources for Hugging Face
│       ├── acsbr-015.pdf
│       ├── acsbr-016.pdf
│       ├── acsbr-017.pdf
│       ├── p70-178.pdf
│── rag/
│   ├── attention.pdf
│   ├── Multi-Algorithm.pdf
│   ├── retriever.ipynb        # RAG retriever implementation
│   ├── simplerag.ipynb        # Simple RAG implementation
│   ├── speech.txt             # Speech dataset for RAG
│── venv/                      # Virtual environment
│── .env                       # Environment variables
│── requirements.txt           # Dependencies
│── README.md                  # Project documentation
```

## 📌 To-Do
- [ ] Add more evaluation metrics for RAG pipeline.
- [ ] Optimize API latency.
- [ ] Expand multi-source document retrieval.

## 🤝 Contributing

Feel free to fork the repo, create a new branch, and submit a pull request. Contributions are welcome!

## 📜 License
This project is licensed under the MIT License.

---

⭐ **If you find this project useful, don't forget to star the repository!**
