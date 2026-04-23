from state import init_state
from agent import run_agent

def main():
    state = init_state()

    print("AutoStream Agent Ready!")

    while True:
        user_input = input("You: ")

        state, response = run_agent(state, user_input)

        print("Agent:", response)


if __name__ == "__main__":
    main()