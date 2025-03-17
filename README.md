# OpenAI SDK with LLaMA 3.2 

This repository demonstrates the usage of the OpenAI SDK with the LLaMA 3.2 model from Ollama. It includes a basic test script, an agentic workflow for fetching and processing news, and a chatbot UI built using Chainlit.

## Project Structure

- `basic.py` - A simple script to test OpenAI SDK with the LLaMA 3.2 model.
- `newsAgent.py` - Implements an agentic workflow to fetch and process news articles using DuckDuckGo search tool.
- `newsUI.py` - A chatbot UI built with Chainlit to interact with the news agent.

## Installation

Ensure you have Python and Ollama installed. Then, install the required dependencies:

```bash
pip install -U openai-agents chainlit duckduckgo-search
ollama pull llama3.2
```

## Usage

### 1. Running `basic.py`

This script initializes an OpenAI-based agent and generates a meal plan using the LLaMA 3.2 model:

```bash
python basic.py
```

### 2. Running `newsAgent.py`

The script sets up a workflow to fetch news articles using DuckDuckGo search, process them with AI agents, and display the results in the terminal:

```bash
python newsAgent.py
```

Example usage inside the script:

```python
print(run_news_workflow("LLMs"))
```

### 3. Running `newsUI.py`

This script starts a chatbot UI using Chainlit that allows users to request news on any topic:

```bash
chainlit run newsUI.py
```

Once running, interact with the chatbot by entering a news topic.

## Features

- **Basic OpenAI SDK Implementation**: Uses the LLaMA 3.2 model via OpenAI SDK.
- **Agentic Workflow**: Implements a news-fetching assistant that retrieves and edits news.
- **Chainlit Chatbot UI**: Provides a user-friendly interface for interactive news retrieval.


## Notes

- The OpenAI SDK connects to a local server at `http://localhost:11434/v1`.
- Give dummy `api_key` and the ollama `base_url`.


## License

This project is open-source and free to use.

---

Enjoy building agentic AI workflows with OpenAI and LLaMA 3.2!

