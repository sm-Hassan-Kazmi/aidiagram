import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from pydantic.v1 import BaseModel, Field
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Initialize ChatOpenAI model
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
)

# Define the output schema for the diagram code
class Diagram(BaseModel):
    code: str = Field(description="Graphviz code")

# Function to generate a Graphviz diagram as a PNG file
def generate_graphviz_diagram(file_path):
    output_path = file_path.replace('.dot', '.png')
    try:
        result = subprocess.run(
            ["dot", "-Tpng", file_path, "-o", output_path],
            check=True, capture_output=True, text=True
        )
        print("Diagram generated successfully.")
        return output_path
    except subprocess.CalledProcessError as e:
        st.error(f"Error generating diagram: {e.stderr}")
    except FileNotFoundError as fnf_error:
        st.error(f"File not found: {fnf_error}")
    except Exception as ex:
        st.error(f"An unexpected error occurred: {ex}")
    return None

# Main function to run the LangChain model and generate the diagram code
def generate_diagram_code(scenario):
    system = (
        "You are an AI diagram code generator for Graphviz. Given any programming or logic scenario, "
        "you will only generate Graphviz code for it, without additional explanations or formatting markers like ```dot."
    )

    prompt = PromptTemplate(
        template="Answer the user query with Graphviz code only.\n{system}\n{text}",
        input_variables=["text"],
        partial_variables={"system": system}
    )

    prompt_text = prompt.format(text=scenario)
    response = llm.invoke(prompt_text)
    return response.content

# Streamlit app
def main():
    st.title("AI Diagram Generator")
    st.write("Enter a scenario below, and the AI will generate a Graphviz diagram based on it.")

    scenario = st.text_input("Describe the diagram scenario", "I want a UML USE CASE diagram for user interaction with an ATM")

    if st.button("Generate Diagram"):
        if scenario:
            with st.spinner("Generating Graphviz code..."):
                graphviz_code = generate_diagram_code(scenario)
                st.code(graphviz_code, language="dot")

                # Save Graphviz code to a .dot file
                file_path = "diagram.dot"
                with open(file_path, 'w') as file:
                    file.write(graphviz_code)

                # Generate and display the diagram
                output_path = generate_graphviz_diagram(file_path)
                if output_path:
                    st.image(output_path, caption="Generated Diagram")
        else:
            st.warning("Please enter a scenario to generate the diagram.")

if __name__ == "__main__":
    main()
