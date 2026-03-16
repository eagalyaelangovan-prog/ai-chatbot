import streamlit as st
import google.generativeai as genai

genai.configure(api_key="3Aw8VJrHJv6gFqoHen07U9TwIJQ_2K4HQnd5Yg3Sgkp7Vix9D")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🤖 AI Study Assistant Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role":"user","content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.generate_content(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.text)

    st.session_state.messages.append({"role":"assistant","content":response.text})
