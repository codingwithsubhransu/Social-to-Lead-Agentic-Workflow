from services.intent_service import classify_intent
from services.rag_services import rag_answer
from services.extraction_service import extract_info
from tools.lead_capture import mock_lead_capture


def run_agent(state, user_input):

    state["messages"].append(user_input)

    # Step 1: Detect intent
    intent = classify_intent(user_input)
    state["intent"] = intent

    # Step 3: Decision logic

    if intent == "greeting":
        return state, "Hey! How can I help you today?"

    elif intent == "inquiry":
        answer = rag_answer(user_input)
        return state, answer

    elif intent == "high_intent":

        if not state.get("name") or not state.get("email") or not state.get("platform"):
            extracted_info = extract_info()
            state.update(extracted_info)

        else:
            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )
            return state, "You're all set! Our team will contact you soon."

    return state, "Can you clarify?"