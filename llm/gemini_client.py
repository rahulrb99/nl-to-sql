import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_sql(prompt: str) -> str:
    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )
    return response.text.strip()
