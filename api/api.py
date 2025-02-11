from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI # for creating chat application
from langserve import add_routes # for creating all the routes for api like - openai, llama
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

app = FastAPI(
  title="Langchain Server",
  version = '1.0',
  description="A Simple API Serve"
)

# add_routes(app, ChatOpenAI(),path="/openai")
# model = ChatOpenAI()

# ollama llama2
llm = Ollama(model="gemma2:2b")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} around 250 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} around 250 words")

add_routes(
  app,
  prompt2 | llm,
  path="/poem"
)

if __name__ == "__main__":
  uvicorn.run(app,host="localhost", port = 8000)