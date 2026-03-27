import React, { useState } from "react";

function UrlForm({ onSubmit }) {
  const [url, setUrl] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(url);
  };

  return (
    <div>
      <h2>Website Auditor</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="url"
          placeholder="https://example.com"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button type="submit">Analyze Website</button>
      </form>
    </div>
  );
}

export default UrlForm;