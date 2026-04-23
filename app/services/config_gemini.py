import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Ensure the key name matches your .env file (e.g., GEMINI_API_KEY or GOOGLE_API_KEY)
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key not found in environment variables.")

genai.configure(api_key=api_key)

# Use the correct model name
model = genai.GenerativeModel("gemini-2.5-flash")   