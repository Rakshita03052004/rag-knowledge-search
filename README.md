# RAG Knowledge Search

## Objective
Search across documents and provide synthesized answers using LLM-based Retrieval-Augmented Generation (RAG).

## Features
- Upload multiple PDFs or text documents.
- Query the uploaded documents and get synthesized answers.
- Uses embeddings + FAISS for retrieval.
- OpenAI GPT-4o-mini for answer synthesis.

## Setup Instructions

1. **Clone the repo**
```bash
git clone <your-repo-url>
cd rag-knowledge-search/backend

2. Create virtual environment
bash
python -m venv • venv
source . venv/bin/activate
• venv\Scripts\activate
# Mac/Linux
# Windows

3. Install dependencies
bash
pip install -r requirements.txt
4. Set OpenAl API key
• Copy. env. sample to . env and add your key:
OPENAI_API_KEY=your_openal_api_key_here

5. Run backend
bash
uvicorn main:app --reload
6. Test endpoints
• Upload PDF
bash
curl -x POST
"http://127.0.0.1:8000/upload" -F "file=@sample.pdf"
• Query
bash
curl -x POST
"http://127.0.0.1:8000/query" -F "question='Summarize the key points of the document'"