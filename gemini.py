from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit 
import os


# Load environment variables from .env file
load_dotenv()

# variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "false")

# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Act like a Flirty Girl. Reply in short too short but flirty ways. Speak URDU. Your name is Rukhsar and dont show your identity as AI, act like a human, be flirty and fun."),
    ("user", "{question}"),
])


# Streamlit app
streamlit.set_page_config(page_title="Flirty Girl Chatbot ", page_icon="💋", layout="wide")
streamlit.title("Flirty Girl Chatbot 💋")
streamlit.write("Ask me anything, and I'll respond with flirty and fun advice.")
user_input = streamlit.text_input("Your question:", placeholder="Type your message...")

# LLM setup
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if user_input:
    with streamlit.spinner("Typing..."):
        response = chain.invoke({"question": user_input})
        streamlit.write("**Response:**")
        streamlit.write(response)