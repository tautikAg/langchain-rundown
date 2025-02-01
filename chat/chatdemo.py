#lets create this rundown in 20min, and get and overview of the chatbot
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


#lets create prompt
prompt=ChatPromptTemplate.from_messages(
    [("system", "You are an AI assistant helping a user with their homework. The user asks you a Question, answer it."),
    ("user", "Question: {Question}"),]
)

#lets create output parser
output_parser=StrOutputParser()

#llm
llm=Ollama(model="deepseek-r1")

#streamlit app
st.title("Chatbot Demo")
st.write("This is a demo of a chatbot that can answer questions. Ask a question and the chatbot will answer it")

input_text=st.text_input("Ask a question")

#now we will create the chain that will be ig first the question to the prompt then to llm then to output str (parser)
chain = prompt|llm|output_parser

#lets create the chatbot
if input_text:
    st.write(chain.invoke({"Question":input_text}))
