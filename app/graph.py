from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import intent_node, greeting_node, rag_node, lead_node


# 🔹 Routing function
def route(state):
    intent = state["intent"]

    if intent == "greeting":
        return "greeting"

    elif intent == "inquiry":
        return "rag"

    elif intent == "high_intent":
        return "lead"

    return "rag"

def build_graph():

    builder = StateGraph(AgentState)

    # Nodes
    builder.add_node("intent", intent_node)
    builder.add_node("greeting", greeting_node)
    builder.add_node("rag", rag_node)
    builder.add_node("lead", lead_node)

    # Entry point
    builder.set_entry_point("intent")

    # Conditional routing
    builder.add_conditional_edges("intent", route, {
        "greeting": "greeting",
        "rag": "rag",
        "lead": "lead"
    })

    # End nodes
    builder.add_edge("greeting", END)
    builder.add_edge("rag", END)
    builder.add_edge("lead", END)

    return builder.compile()