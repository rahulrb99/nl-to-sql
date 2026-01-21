import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [sql, setSql] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function runQuery() {
    setLoading(true);
    setError("");
    setSql("");
    setResults([]);

    try {
      const response = await fetch("http://127.0.0.1:8000/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.detail || "Request failed");
      }

      const data = await response.json();
      setSql(data.sql);
      setResults(data.results);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.title}>NL → SQL Analytics</h1>
        <p style={styles.subtitle}>
          Ask business questions in natural language. The system converts them
          into safe SQL and queries the database.
        </p>

        <textarea
          rows={3}
          style={styles.textarea}
          placeholder="e.g. Total sales by region in 2014"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button
          onClick={runQuery}
          disabled={loading || !question.trim()}
          style={{
            ...styles.button,
            opacity: loading || !question.trim() ? 0.6 : 1,
          }}
        >
          {loading ? "Running query..." : "Run Query"}
        </button>

        {error && <div style={styles.error}>⚠️ {error}</div>}

        {sql && (
          <div style={styles.section}>
            <h3 style={styles.sectionTitle}>Generated SQL</h3>
            <pre style={styles.sqlBox}>{sql}</pre>
          </div>
        )}

        {results.length > 0 && (
          <div style={styles.section}>
            <h3 style={styles.sectionTitle}>Results</h3>

            <div style={styles.tableWrapper}>
              <table style={styles.table}>
                <thead>
                  <tr>
                    {Object.keys(results[0]).map((key) => (
                      <th key={key} style={styles.th}>
                        {key}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {results.map((row, idx) => (
                    <tr key={idx}>
                      {Object.values(row).map((value, i) => (
                        <td key={i} style={styles.td}>
                          {typeof value === "number"
                            ? value.toLocaleString()
                            : value}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    background: "linear-gradient(135deg, #f4f7fb, #e9eef5)",
    display: "flex",
    justifyContent: "center",
    alignItems: "flex-start",
    padding: "60px 20px",
    fontFamily: "Segoe UI, sans-serif",
  },
  card: {
    background: "#ffffff",
    width: "100%",
    maxWidth: "900px",
    padding: "32px",
    borderRadius: "12px",
    boxShadow: "0 10px 30px rgba(0,0,0,0.08)",
  },
  title: {
    margin: 0,
    fontSize: "28px",
    color: "#1f2937",
  },
  subtitle: {
    marginTop: "8px",
    marginBottom: "24px",
    color: "#4b5563",
    lineHeight: 1.5,
  },
  textarea: {
    width: "100%",
    padding: "12px",
    fontSize: "16px",
    borderRadius: "8px",
    border: "1px solid #d1d5db",
    outline: "none",
    resize: "none",
    marginBottom: "16px",
  },
  button: {
    background: "#2563eb",
    color: "#ffffff",
    border: "none",
    padding: "10px 18px",
    fontSize: "16px",
    borderRadius: "8px",
    cursor: "pointer",
  },
  error: {
    marginTop: "16px",
    color: "#b91c1c",
    background: "#fee2e2",
    padding: "10px",
    borderRadius: "8px",
  },
  section: {
    marginTop: "28px",
  },
  sectionTitle: {
    marginBottom: "8px",
    color: "#111827",
  },
  sqlBox: {
    background: "#f9fafb",
    padding: "14px",
    borderRadius: "8px",
    border: "1px solid #e5e7eb",
    overflowX: "auto",
  },
  tableWrapper: {
    overflowX: "auto",
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
    marginTop: "8px",
  },
  th: {
    textAlign: "left",
    padding: "10px",
    background: "#f3f4f6",
    borderBottom: "2px solid #e5e7eb",
  },
  td: {
    padding: "10px",
    borderBottom: "1px solid #e5e7eb",
  },
};

export default App;
