def build_nl2sql_prompt(schema: str, question: str) -> str:
    prompt = f"""
You are an expert PostgreSQL SQL generator.

You are given the database schema below.
Use ONLY the tables and columns listed.
Do NOT hallucinate tables or columns.

Schema:
{schema}

User Question:
{question}

Rules:
- Generate exactly ONE SQL query
- Use valid PostgreSQL syntax
- Do NOT include explanations
- Do NOT include markdown
- Do NOT include comments
- Always use explicit column aliases for aggregates (e.g. SUM(sales) AS total_sales)

"""
    return prompt
