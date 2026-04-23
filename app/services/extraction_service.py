from services.config_gemini import model
import json

def extract_info():
    # prompt = f"""
    # Extract name, email, and platform if present.

    # Input: {query}

    # Output JSON format:
    # {{
    #   "name": "",
    #   "email": "",
    #   "platform": ""
    # }}
    # """
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    platform = input("Enter the platform (e.g., Twitter, LinkedIn): ")

    # response = model.generate_content(prompt)
    return json.loads(json.dumps({"name": name, "email": email, "platform": platform}))