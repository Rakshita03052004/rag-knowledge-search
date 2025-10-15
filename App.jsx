import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadFile = async () => {
    if (!file) return;
    setLoading(true);
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await axios.post("http://127.0.0.1:8000/upload", formData);
      alert(res.data.message);
    } catch (err) {
      alert("Upload failed");
    }
    setLoading(false);
  };

  const askQuestion = async () => {
    if (!question) return;
    setLoading(true);
    try {
      const formData = new FormData();
      formData.append("question", question);
      const res = await axios.post("http://127.0.0.1:8000/query", formData);
      setAnswer(res.data.answer);
    } catch (err) {
      alert("Query failed");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1 className="title">🎯 RAG Document Explorer</h1>

      <div className="card gradient-card">
        <h2>📄 Upload Document</h2>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button className="gradient-btn" onClick={uploadFile}>
          {loading ? "Uploading..." : "Upload"}
        </button>
      </div>

      <div className="card gradient-card">
        <h2>💡 Ask a Question</h2>
        <input
          type="text"
          value={question}
          placeholder="Type your query..."
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button className="gradient-btn" onClick={askQuestion}>
          {loading ? "Querying..." : "Submit"}
        </button>
      </div>

      {answer && (
        <div className="card answer-card gradient-card">
          <h2>📝 Answer</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default App;