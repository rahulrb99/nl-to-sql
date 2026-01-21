from db.schema_extractor import get_schema
from prompts.nl2sql_prompt import build_nl2sql_prompt
from llm.gemini_client import generate_sql
from db.sql_executor import execute_sql
from validation.sql_validator import extract_sql, validate_sql

question = "Total sales by region in 2014"

# 1. Build prompt
schema = get_schema()
prompt = build_nl2sql_prompt(schema, question)

# 2. Generate SQL
raw_sql = generate_sql(prompt)
sql = extract_sql(raw_sql)
validate_sql(sql)

print("Executing SQL:\n", sql)

# 3. Execute SQL
results = execute_sql(sql)

print("\nResults:")
for row in results:
    print(row)
