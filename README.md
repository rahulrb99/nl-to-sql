# Natural Language to SQL API

This project converts natural language business questions into safe, executable SQL queries using a Large Language Model (LLM).  
It exposes a FastAPI backend that validates generated SQL and executes read-only analytical queries on a relational dataset.

---

## 🚀 Features
- Converts natural language questions into SQL
- Enforces **SELECT-only** queries for safety
- Schema-aware prompt design
- FastAPI backend with clean API responses
- Handles invalid or unsafe queries gracefully

---

## 🧱 Tech Stack
- Python
- FastAPI
- SQL (SQLite / PostgreSQL)
- Large Language Model (Gemini)
- HTML / JavaScript (simple frontend)

---

## 🏗️ System Architecture


1. User submits a natural language question  
2. Question is combined with database schema in the prompt  
3. LLM generates a SQL query  
4. SQL validator ensures only SELECT queries are allowed  
5. Query is executed on the database  
6. Results are returned via API

**Why validation?**  
LLMs are probabilistic. SQL validation ensures only safe, read-only queries are executed.


## 📊 Dataset
The project uses a structured retail dataset containing:
- Orders
- Sales
- Profit
- Categories
- Regions
- Dates

This makes it suitable for analytical business questions.

---

## 🧪 Example Queries
- Which category has the highest and lowest total profit?
- Total sales by region for 2014
- Top 5 sub-categories by profit
- Average profit per order by category

---

## 🔐 Safety Measures
- Only `SELECT` statements are allowed
- Queries with `UPDATE`, `DELETE`, `DROP`, etc. are rejected
- Invalid SQL is never executed
- Clear error messages returned to the user

---

## ▶️ How to Run

### 1. Install dependencies
pip install -r requirements.txt

2. Set environment variables
Create a .env file:
GEMINI_API_KEY=your_api_key_here

3. Start the server
uvicorn main:app --reload

The API will be available at:
http://127.0.0.1:8000

🧠 Key Learnings
LLM outputs must be validated before execution

Prompt design significantly affects SQL accuracy

Backend safeguards are essential for AI systems

System design matters more than model choice

📌 Future Improvements
Authentication and rate limiting

Support for multiple datasets

Query performance optimization

Enhanced frontend UI

📄 License
This project is for educational and portfolio purposes.

