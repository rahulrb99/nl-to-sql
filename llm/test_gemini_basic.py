from google import genai
import os

# Initialize the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    print("Sending request to Gemini 2.0 Flash...")
    
    # Using the EXACT string found in your list
# Change the model to the standard 1.5 Flash
    response = client.models.generate_content(
     model="models/gemini-flash-latest", 
     contents="Convert to SQL: Show all employees."
)
    print("\n--- Success! ---")
    print("SQL Output:")
    print(response.text)

except Exception as e:
    print(f"\n--- Error ---\n{e}")