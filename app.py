from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

#set up environment varibales
import os
from dotenv import load_dotenv

load_dotenv()


#implement langsmith tracking
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_tracing = os.getenv("LANGCHAIN_TRACING_V2", 'true')
langchain_project = os.getenv("LANGCHAIN_PROJECT")

#chatprompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', "You're a helpful assistant that provide response to any question aksed by the user"),
        ('human', "{question}")
    ]
)

#function to generate response from the chatbot
def generate_response(question, model, temperature, max_token):
    model = Ollama(model = model)
    chain = prompt | model | StrOutputParser()
    response = chain.invoke(
        {
            'question': question
        }
    )
    return response

#crreate the streamlit app
st.title("Enhance Q&A Chatbot with Ollama")

#dropdown to selecte various openai models
model = st.sidebar.selectbox("Select your prefered model", ['deepseek-r1', 'gemma2'])

#set the temperature and max token values  using slider
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_token = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=100)

##Main interface for user input,
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, model, temperature, max_token)
    st.write(response)

else:
    st.write("Please provide a query")