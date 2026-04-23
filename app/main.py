from graph import build_graph

def main():
    graph = build_graph()

    state = {
        "messages": [],
        "intent": None,
        "name": None,
        "email": None,
        "platform": None,
        "response": None
    }

    print("AutoStream LangGraph Agent Ready!")

    while True:
        user_input = input("You: ")

        state["messages"].append(user_input)

        state = graph.invoke(state)

        print("Agent:", state["response"])


if __name__ == "__main__":
    main()