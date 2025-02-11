from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is set
api_key = os.getenv('LANGCHAIN_API_KEY')
if api_key is None:
    st.error("LANGCHAIN_API_KEY is missing. Please check your .env file or environment variables.")
else:
    os.environ['LANGCHAIN_API_KEY'] = api_key

os.environ['LANGCHAIN_TRACING_V2'] = "true"

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries"),
    ("user", "Question: {question}")
])

# Streamlit framework
st.title('LangChain Chatbot with Ollama')
input_text = st.text_input('Enter your question')

# Use the available Gemma model instead of Llama2
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke(input_text))
