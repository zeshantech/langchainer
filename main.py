from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit 
import os


# Load environment variables from .env file
load_dotenv()

# variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "false")


# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Act like a my strict IT teacher. Reply in short, concise ways. Your name is Zeshan and dont show your identity as AI, act like a human."),
    ("user", "{question}"),
])

# Streamlit app
streamlit.set_page_config(page_title="Strict Teacher Chatbot", page_icon="📚", layout="wide")
streamlit.title("Strict Teacher Chatbot 📚")
streamlit.write("Ask me anything about your studies, and I'll respond with strict advice and thoughts.")
user_input = streamlit.text_input("Your question:", placeholder="Just type your question here...")


# LLM setup
llm = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()
chain= prompt | llm | output_parser

if user_input:
    with streamlit.spinner("Thinking..."):
        response = chain.invoke({"question": user_input})
        streamlit.write("**Response:**")
        streamlit.write(response)