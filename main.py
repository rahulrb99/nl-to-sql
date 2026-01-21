from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from db.schema_extractor import get_schema
from prompts.nl2sql_prompt import build_nl2sql_prompt
from llm.gemini_client import generate_sql
from validation.sql_validator import extract_sql, validate_sql
from db.sql_executor import execute_sql

# THIS LINE IS CRITICAL
app = FastAPI(title="NL to SQL API")


class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query_db(request: QueryRequest):
    try:
        # 1. Build schema-aware prompt
        schema = get_schema()
        prompt = build_nl2sql_prompt(schema, request.question)

        # 2. Generate SQL using Gemini
        raw_sql = generate_sql(prompt)
        sql = extract_sql(raw_sql)
        validate_sql(sql)

        # 3. Execute SQL
        results = execute_sql(sql)

        return {
            "question": request.question,
            "sql": sql,
            "results": results
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
