# AI Diagram Generator

This project is a Streamlit-based web application that generates Graphviz diagrams based on natural language descriptions provided by the user. Leveraging LangChain, OpenAI, and Graphviz, it translates user input scenarios into visual representations, such as UML or flow diagrams, that can be saved and displayed in the app.

## Features
- **User Interface**: Simple Streamlit UI for inputting scenarios and viewing generated diagrams.
- **AI-Powered Diagram Code Generation**: Generates Graphviz code based on natural language descriptions using OpenAI's GPT model.
- **Graphviz Diagram Rendering**: Converts generated Graphviz code into PNG images for easy viewing.

## Prerequisites
- **OpenAI API Key**: Sign up on [OpenAI](https://openai.com/) and get your API key.
- **Graphviz**: Ensure Graphviz is installed for generating the diagrams.

### Installation

1. Clone this repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Install Graphviz if not already installed:
    - On **Ubuntu**:
        ```bash
        sudo apt-get install graphviz
        ```
    - On **Mac**:
        ```bash
        brew install graphviz
        ```
    - On **Windows**:
        Download and install Graphviz from [graphviz.org](https://graphviz.org/download/).

5. Set up environment variables:
    - Rename `.env.example` to `.env`, and add your OpenAI API key:
        ```env
        OPENAI_API_KEY=your_openai_api_key
        ```

### Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the URL provided in the terminal to access the application.

3. Enter a scenario (e.g., "Create a UML use case diagram for user interaction with an ATM") and click **Generate Diagram**.

4. View the Graphviz code and generated diagram in the app.