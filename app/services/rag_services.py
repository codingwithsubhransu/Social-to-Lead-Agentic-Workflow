import json
from services.config_gemini import model

def load_data():
    with open(r"D:\Projects\Social to Lead Agentic Workflow\app\data\knowledge.json", "r") as f:
        data = json.load(f)
    return data

knowledge = load_data()

def rag_answer(query):
    context = f"""
    Pricing:
    Basic: {knowledge['plans']['Basic']}
    Pro: {knowledge['plans']['Pro']}

    Policies:
    Refund: {knowledge['policies']['refund']}
    Support: {knowledge['policies']['support']}
    """

    prompt = f"""
    Answer the question using this context only:

    {context}

    Question: {query}
    """

    response = model.generate_content(prompt)
    return response.text
