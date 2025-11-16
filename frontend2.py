import streamlit as st
import requests

st.set_page_config(page_title="Research AI Agent", page_icon="📄")
st.title("📄 Research AI Agent")

API_URL = "http://localhost:8000/ask"

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    st.chat_message("user").write(user_input)

    with st.spinner("Thinking..."):
        resp = requests.post(API_URL, json={"message": user_input})
        answer = resp.json().get("response", "")

    st.session_state.chat.append(("assistant", answer))
    st.chat_message("assistant").write(answer)