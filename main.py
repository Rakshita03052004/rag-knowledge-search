import os
import pdfplumber
import faiss
import numpy as np
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from openai import OpenAI  # new client

load_dotenv()

print("Loaded OpenAI key:", os.getenv("OPENAI_API_KEY"))  # debug check

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model & FAISS index
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
dimension = embedding_model.get_sentence_embedding_dimension()
index = faiss.IndexFlatL2(dimension)

documents = []  # store chunks of text

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Document Upload ---
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    text = ""

    # Extract text
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    else:
        text = (await file.read()).decode("utf-8")

    # Split into chunks and create embeddings
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    embeddings = embedding_model.encode(chunks)

    for chunk, emb in zip(chunks, embeddings):
        index.add(np.array([emb]))
        documents.append(chunk)

    return {"message": f"{file.filename} uploaded & processed", "chunks": len(chunks)}

# --- Query API ---
@app.post("/query")
async def query_docs(question: str = Form(...)):
    if len(documents) == 0:
        return {"error": "No documents uploaded yet."}

    q_emb = embedding_model.encode([question])
    D, I = index.search(q_emb, k=3)
    retrieved_texts = [documents[i] for i in I[0] if i < len(documents)]

    context = "\n\n".join(retrieved_texts)
    prompt = f"Using these documents, answer the question:\n\n{context}\n\nQuestion: {question}\nAnswer succinctly:"

    # Generate answer using OpenAI v1.0+ client
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content
    return {"answer": answer, "context_used": len(retrieved_texts)}

@app.get("/")
def root():
    return {"status": "RAG backend alive"}