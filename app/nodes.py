from services.intent_service import classify_intent
from services.rag_services import rag_answer
from services.extraction_service import extract_info
from tools.lead_capture import mock_lead_capture


# 🔹 Intent Node
def intent_node(state):
    user_input = state["messages"][-1]
    intent = classify_intent(user_input)

    state["intent"] = intent
    return state


# 🔹 Greeting Node
def greeting_node(state):
    state["response"] = "Hey! How can I help you today?"
    return state


# 🔹 RAG Node
def rag_node(state):
    query = state["messages"][-1]
    answer = rag_answer(query)

    state["response"] = answer
    return state


# 🔹 Lead Flow Node
def lead_node(state):

    # Extract info
    info = extract_info()
    state["name"] = info.get("name")
    state["email"] = info.get("email")
    state["platform"] = info.get("platform")

    if not state["name"] or not state["email"]:
        state["response"] = "I couldn't extract your contact info. Could you please provide your name and email?"
        return state
    
    else:
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )
        state["response"] = "You're all set! Our team will contact you soon."
        return state