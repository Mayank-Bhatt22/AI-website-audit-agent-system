import React, { useState } from "react";
import UrlForm from "./components/UrlForm";
import Report from "./components/Report";

function App() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUrlSubmit = async (url) => {
    setLoading(true);
    try {
      const response = await fetch(`/audit?url=${encodeURIComponent(url)}`);
      const data = await response.json();
      setReport(data);
    } catch (error) {
      console.error("Error fetching audit:", error);
      alert("Error analyzing website. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>AI Website Auditor</h1>
      <UrlForm onSubmit={handleUrlSubmit} />
      {loading && <p>Analyzing website...</p>}
      <Report report={report} />
    </div>
  );
}

export default App;
