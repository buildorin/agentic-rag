import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const askAgent = async () => {
    const res = await axios.post('http://localhost:8000/query/', null, {
      params: { query },
    });
    setResponse(res.data.answer);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Agentic RAG App</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a question..."
        style={{ padding: '10px', width: '300px' }}
      />
      <button onClick={askAgent} style={{ marginLeft: '10px', padding: '10px' }}>
        Ask
      </button>
      <p style={{ marginTop: '20px' }}>{response}</p>
    </div>
  );
}

export default App;