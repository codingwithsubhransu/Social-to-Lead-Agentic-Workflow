from services.config_gemini import model

def classify_intent(query):
    prompt = f"""
    Classify the user intent strictly into one of:
    greeting, inquiry, high_intent

    Examples:
    Hi → greeting
    What is pricing → inquiry
    I want to buy → high_intent

    Input: {query}
    Output:
    """

    response = model.generate_content(prompt)
    return response.text.strip().lower()