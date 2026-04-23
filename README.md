# Social to Lead Agentic Workflow

An intent-driven conversational workflow built with LangGraph and Gemini.

This project routes user input into one of three paths:
- greeting: polite assistant reply
- inquiry: answer from a small knowledge base (RAG-style context prompt)
- high_intent: collect lead details and simulate lead capture

## What This Project Does

The agent loop in `app/main.py`:
1. Accepts user input.
2. Classifies intent (`greeting`, `inquiry`, `high_intent`).
3. Routes through a LangGraph state machine.
4. Returns a response and keeps conversation state in memory.

## Project Structure

```
.
|- README.md
|- requirements.txt
|- app/
|  |- main.py                 # CLI entrypoint for the LangGraph agent
|  |- graph.py                # Graph definition and routing
|  |- nodes.py                # Node logic: intent, greeting, rag, lead
|  |- state.py                # Agent state schema
|  |- data/
|  |  |- knowledge.json       # Pricing/policy knowledge used in inquiry flow
|  |- services/
|  |  |- config_gemini.py     # Gemini model configuration via .env
|  |  |- intent_service.py    # Intent classifier
|  |  |- extraction_service.py# Lead data collection
|  |  |- rag_services.py      # Context-based answer generation
|  |- tools/
|     |- lead_capture.py      # Mock lead capture sink
```

## Prerequisites

- Python 3.9+ (recommended: 3.11)
- A Gemini API key

## Quick Start

### 1. Clone and enter the project

```powershell
https://github.com/codingwithsubhransu/Social-to-Lead-Agentic-Workflow.git
cd "Social to Lead Agentic Workflow"
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
pip install python-dotenv
```

Note: `python-dotenv` is required by `config_gemini.py` and should be installed.

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run the Main Agent

From the project root:

```powershell
cd app
python main.py
```

You should see:

```text
AutoStream LangGraph Agent Ready!
```

Then interact in a loop:

- greeting example: `Hi`
- inquiry example: `What is your pro pricing?`
- high intent example: `I want to buy this`

For `high_intent`, the app asks for:
- name
- email
- platform

After successful capture, it prints a confirmation and simulates lead storage.

## Run the Playground App

This is a simpler loop for intent testing.

```powershell
cd test_app
python main.py
```

Type `exit` to stop.

## How Routing Works

Defined in `app/graph.py`:
- `intent_node` runs first.
- `route()` maps intent to one of:
	- `greeting_node`
	- `rag_node`
	- `lead_node`
- Each node ends the graph run after producing `state["response"]`.

## Knowledge Source

Inquiry responses are grounded using `app/data/knowledge.json`:
- plan pricing
- refund policy
- support policy

Update this file to change what the inquiry flow can answer.

## Troubleshooting

- `API Key not found in environment variables.`
	- Ensure `.env` exists in project root and contains `GEMINI_API_KEY`.

- `ModuleNotFoundError: No module named dotenv`
	- Install dotenv: `pip install python-dotenv`.

- Poor intent labels from model output
	- The classifier expects exact values: `greeting`, `inquiry`, `high_intent`.
	- Consider normalizing output if you extend this project.

- File path issues on non-Windows systems
	- `rag_services.py` currently uses an absolute Windows path for `knowledge.json`.
	- Replace with a relative path strategy (`pathlib`) for portability.