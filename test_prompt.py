from db.schema_extractor import get_schema
from prompts.nl2sql_prompt import build_nl2sql_prompt
from llm.gemini_client import generate_sql

schema = get_schema()
question = "Total sales by region in 2014"

prompt = build_nl2sql_prompt(schema, question)
sql = generate_sql(prompt)

print(sql)
