import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path, override=True)
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(f"Gemini API key not found in {env_path}")

client = genai.Client(api_key=api_key)

prompt = input("Enter your prompt: ")
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"Answer in exactly five words.\n\nQuestion: {prompt}",
)
print(response.text)