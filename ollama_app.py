import os 
from dotenv import load_dotenv
load_dotenv()


from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#langsmith tracking :--
os.environ["HF_API_KEY"] = os.getenv("HF_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful advanced technical assistant. summarize the context of output in a simple way "),
    ("user", "Question:{input}"),
])

# Initialize the Ollama model
model = OllamaLLM(model="llama3")
st.title("An simple chat bot llm uses ollama model and Langchain")
user_input = st.text_input("Enter your question:")

# if user_input:
#     # Format the prompt with user inputpip install python-dotenv langchain-ollama streamlit langchain
#     formatted_prompt = prompt.format_messages(input=user_input)
    
#     # Get the response from the model
#     response = model(formatted_prompt)
    
#     # Display the response
#     st.write("Response:", response)

# #streamlit run ollama_app.py

output_parser = StrOutputParser()
chain = prompt | model | output_parser

if user_input:
    st.write(chain.invoke({"input": user_input}))

