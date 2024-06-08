from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as ggi

load_dotenv(".env")

fetched_api_key = os.getenv("API_Key")
if not fetched_api_key:
    st.error("API key is missing. Please check your .env file.")
    st.stop()

ggi.configure(api_key=fetched_api_key)

model = ggi.GenerativeModel("gemini-pro")
chat = model.start_chat()


def llm_response(question):
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


st.title("Barking Bot! Meow Meow")

user_quest = st.text_input("You are an Idiot, Tell me what you don't know?")

btn = st.button("Ask")

if btn and user_quest:
    result = llm_response(user_quest)
    if result:
        st.subheader("Response : ")
        for word in result:
            st.text(word.text)
