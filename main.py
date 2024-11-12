from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
# from pydantic import BaseModel, Field
from langchain_community.chat_models import ChatOpenAI
from pydantic.v1 import BaseModel, Field
import os

from dotenv import load_dotenv
load_dotenv()
# Initialize ChatGroq with the given model and API key
# chat = ChatGroq(temperature=0, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama-3.1-8b-instant")
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    )
import subprocess

def generate_graphviz_diagram(file_path):
    """
    Generate a Graphviz diagram by invoking dot through subprocess.

    Args:
        file_path (str): Path to the Graphviz .dot file containing the diagram code.
    """
    try:
        output_path = file_path.replace('.dot', '.png')
        result = subprocess.run(
            ["dot", "-Tpng", file_path, "-o", output_path],
            check=True, capture_output=True, text=True
        )
        print("Diagram generated successfully.")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error generating diagram:", e.stderr)
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Usage example

# Define the output schema for the diagram code (if needed for reference or future parsing)
class Diagram(BaseModel):
    code: str = Field(description="Graphviz code")

def main():
    # System message to instruct the AI to respond with Graphviz code only, no extra delimiters
    system = (
        "You are an AI diagram code generator for Graphviz. Given any programming or logic scenario, "
        "you will only generate Graphviz code for it, without additional explanations or formatting markers like ```dot."
        "Please create a diagram in Graphviz DOT format that represents the logic or structure of the input scenario, "
        "and provide only the Graphviz code as the output."
    )

    # Create the prompt template
    prompt = PromptTemplate(
        template="Answer the user query with Graphviz code only.\n{system}\n{text}",
        input_variables=["text"],
        partial_variables={"system": system}
    )

    # Step 1: Generate the prompt text
    prompt_text = prompt.format(text="I want a UML USE CASE diagram for user interaction with a ATM ")
    print("Generated Prompt Text:\n", prompt_text)
    
    # Step 2: Invoke the chat model with the generated prompt as a string input
    response = llm.invoke(prompt_text)
    print("Response from ChatGroq:\n", response)
    with open('file.dot', 'w') as file:
        file.write(response.content)
    
    generate_graphviz_diagram("file.dot")

main()
