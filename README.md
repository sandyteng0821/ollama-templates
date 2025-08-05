# ollama-templates

This repository provides example scripts and workflows to explore [Ollama](https://ollama.com/) with local LLMs for chat, RAG (retrieval-augmented generation), and function calling.

---

## 📁 Repository Structure

```
./
├── data/                         # Input files for demo (PDFs, text)
│   ├── BOI.pdf
│   └── grocery_list.txt
├── function-calling.py          # Function calling example using Ollama
├── pdf-rag.py                   # Basic PDF RAG script
├── pdf-rag-streamlit.py         # Streamlit UI for PDF RAG chatbot
├── requirements.txt             # Python dependencies
├── start-1.py                   # Simple Ollama chat example
├── start-2.py                   # Chat / generate / delete models
```

---

## 🧠 Ollama Models

Before running the scripts, pull the necessary models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

Check your installed models with:

```bash
ollama list
```

---

## ⚙️ Environment Setup

### Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### System Dependencies

For PDF processing:

```bash
sudo apt-get install poppler-utils
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
sudo apt-get install tesseract-ocr-eng  # English OCR support
```

---

## 🧾 Python Requirements

The following libraries are included in `requirements.txt`:

- `ollama`
- `chromadb`
- `pdfplumber`
- `langchain`
- `langchain-core`
- `langchain-ollama`
- `langchain-community`
- `langchain_text_splitters`
- `unstructured` + `unstructured[all-docs]`
- `fastembed`
- `pikepdf`
- `sentence-transformers`
- `elevenlabs`

---

## 🚀 Usage

### 🔹 Starter Scripts

| Script         | Description                        |
|----------------|------------------------------------|
| `start-1.py`   | Chat with Ollama                   |
| `start-2.py`   | Chat + generate/delete model files |

```bash
python3 start-1.py
python3 start-2.py
```

---

### 🔸 Advanced Use Cases

| Script                        | Description                                |
|------------------------------|--------------------------------------------|
| `pdf-rag.py`                 | RAG using `data/BOI.pdf`                   |
| `pdf-rag-streamlit.py`       | Streamlit UI for PDF RAG chatbot          |
| `function-calling.py`        | Function calling with `grocery_list.txt`  |

```bash
# Basic PDF RAG
python3 pdf-rag.py

# Streamlit UI for RAG chatbot
streamlit run pdf-rag-streamlit.py

# Ollama function calling
python3 function-calling.py
```

Press `Ctrl+C` to stop Streamlit.

---

## 📌 Notes

- Make sure Ollama is running locally.
- Tested with Python 3.10+ and Ubuntu (for apt-based dependencies).
- `data/` folder contains example input files. You can replace them with your own.

---

## 🧪 License

MIT License – Use freely for learning and experimentation.