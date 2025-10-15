# rag-knowledge-search
Retrieval-Augmented Generation (RAG) system with document upload and semantic search


VIDEO LINK - https://drive.google.com/file/d/1JYO8i8eLZvPyD0VND2NETczEydt5bmfa/view?usp=sharing

GITHUB REPO -  https://github.com/Rakshita03052004/rag-knowledge-search

Project Overview
RAG Knowledge Search is a Retrieval-Augmented Generation (RAG) system that allows users to upload documents (PDFs or text) and query them using natural language, retrieving synthesized answers using large language models (LLMs). It combines semantic embeddings, vector search, and LLM-based answer generation for efficient knowledge retrieval.
Key Features:
Upload multiple documents (PDF or TXT).


Search documents using natural language queries.


Retrieve most relevant chunks using semantic similarity.


Generate concise, synthesized answers using OpenAI GPT models.


Optional frontend explorer for easy interaction.



Motivation
Traditional document search often relies on keyword matching and cannot generate summarized or context-aware answers.
RAG integrates vector embeddings for semantic search and LLMs for synthesis, making it ideal for:
Research summaries


Knowledge bases


Internal documentation search


Educational applications



Architecture
1. 
Backend
Tech Stack: Python, FastAPI, FAISS, Sentence Transformers, OpenAI GPT.
Modules:
main.py: FastAPI server to handle uploads and queries.


embeddings.py: Initializes embedding model (all-MiniLM-L6-v2) and creates vector representations of text.


ingestion.py: Processes uploaded documents, splits into chunks, and generates embeddings.


retriever.py: Performs FAISS vector search to retrieve top relevant chunks for a query.


db_faiss.py: Stores embeddings and provides similarity search.


schemas.py: Pydantic schemas for request/response models.


Flow:
Upload document → text extraction → chunking → embeddings → stored in FAISS.


User query → embedding → FAISS search → top-k relevant chunks.


LLM generates synthesized answer based on retrieved context.



2. 
Frontend
Tech Stack: React + Vite + Axios
Features:
Upload documents via drag & drop.


Input natural language query.


Display retrieved answer along with context used.


Modern UI with colorful cards, inputs, and result display.


Component Overview:
App.jsx: Main application, handles UI and API calls.


UploadForm.jsx: Handles document uploads.


QueryForm.jsx: Handles query submission and shows results.


ResultCard.jsx: Displays LLM answer and document context.


UX Flow:
User uploads documents.


Documents are processed in the backend.


User submits a query → backend returns answer.


Frontend displays answer with context.



Setup Instructions
Prerequisites
Python 3.12+


Node.js 18+


Git



Backend Setup
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Environment Variables:
Create .env file:
OPENAI_API_KEY=your_openai_api_key_here
Run backend server:
uvicorn main:app --reload
Access: http://localhost:8000

Frontend Setup
cd frontend
npm install
npm run dev
Access: http://localhost:5173

Usage
Open frontend in browser.


Upload documents (PDF/TXT).


Type a query in natural language.


Click Submit → answer appears along with context used.



Example
Query:
Summarize the key findings from the uploaded research report.”
Answer:“The report concludes with a comparison of the predicted peaks from two models: Polynomial and Random Forest. The final selection prefers the model with the higher predicted peak, with Random Forest favored if its predicted peak is greater or equal.”






Technical Details
Embeddings: SentenceTransformer("all-MiniLM-L6-v2")


Vector Search: FAISS IndexFlatL2, fast similarity search.


LLM Generation: OpenAI GPT-4o-mini via OpenAI Python client.


Document Chunking: Split text into 1000-character chunks for embeddings.



File Structure
rag-knowledge-search/
│
├─ backend/
│   ├─ main.py
│   ├─ embeddings.py
│   ├─ ingestion.py
│   ├─ retriever.py
│   ├─ db_faiss.py
│   └─ __pycache__/
│
├─ frontend/
│   ├─ src/
│   │   ├─ App.jsx
│   │   ├─ UploadForm.jsx
│   │   ├─ QueryForm.jsx
│   │   └─ ResultCard.jsx
│   └─ package.json
│
├─ .gitignore
├─ README.md
└─ requirements.txt

Submission Deliverables
GitHub repository: https://github.com/Rakshita03052004/rag-knowledge-search


Demo video: https://drive.google.com/file/d/1JYO8i8eLZvPyD0VND2NETczEydt5bmfa/view?usp=sharing




Screen recording showing


Document upload


Query submission


Generated answer display


PDF copy of README (this file)



Key Highlights
RAG-powered: Combines embeddings + LLM for retrieval & synthesis.


Extensible: Can add multiple LLM models or storage backends.


User-friendly: React frontend with clean and responsive UI.


Fully documented: README explains architecture, setup, and usage.




