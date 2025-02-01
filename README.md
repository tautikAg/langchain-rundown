# Chatbot Demo

This project demonstrates a simple chatbot using the Langchain library and Streamlit. The chatbot is designed to help users with their homework by answering their questions.

## Requirements

- Python 3.7+
- Conda
- Streamlit
- Langchain
- dotenv

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/langchain_rundown.git
    cd langchain_rundown
    ```

2. Create and activate a Conda environment:
    ```sh
    conda create --name env python=3.12
    conda activate env
    ```

3. Install the required packages:
    ```sh
    pip install streamlit langchain python-dotenv
    ```

4. Create a [.env](http://_vscodecontentref_/2) file in the root directory with the following content:
    ```properties
    LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
    LANGSMITH_PROJECT="first-test"
    LANGCHAIN_API_KEY="your_langchain_api_key"
    ```

## Running the App

To run the Streamlit app, use the following command:
```sh
streamlit run chat/chatdemo.py
```
## Project Overview

This project uses the following components:

- **Langchain**: A library for building language models.
- **Streamlit**: A framework for creating interactive web applications.
- **dotenv**: A library for loading environment variables from a .env file.

The chatbot is powered by the Ollama model (deepseek-r1) and uses a prompt template to generate responses based on user questions.

## Code Explanation

The main script (`chat/chatdemo.py`) performs the following tasks:

1. Loads environment variables from the `.env` file.
2. Sets up Langsmith tracking.
3. Creates a prompt template for the chatbot.
4. Initializes the Ollama model.
5. Sets up a Streamlit app to interact with the chatbot.
