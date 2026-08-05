import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
import json


load_dotenv()

client = Groq(api_key=os.getenv("GROK_API_KEY"))


try:
    with open("data.json", "r") as file:
        institute_data = json.load(file)
        institute_context = json.dumps(institute_data, indent=2)

except FileNotFoundError:
    institute_context = "Knowledge Base Not Found."
    st.error("Could not find data.json")


st.set_page_config(
    page_title="HighQ AI Assistant",
    layout="wide"
)


SYSTEM_PROMPT = {
    "role": "system",
    "content": f"""
You are an enquiry chatbot for HighQ Training Institute.

Answer ONLY using the information provided below.

Knowledge Base:

{institute_context}

Rules:

1. Never invent information.
2. If information is unavailable, politely say:
   "I don't have information about that at the moment. Please contact the HighQ Training Institute admissions team for the latest details. They will be happy to assist you." 
3. Answer professionally.
4. Use bullets whenever appropriate.
"""
}

if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_chat_index" not in st.session_state:
    st.session_state.current_chat_index = None


with st.sidebar:

    st.image("assets/logo.jpg", width=70)

    st.title("HighQ")

    st.markdown("---")

    if st.button(" + New Chat", use_container_width=True):

        st.session_state.messages = [SYSTEM_PROMPT]
        st.session_state.current_chat_index = None
        st.rerun()

    st.markdown("---")

    st.subheader("Recent Chats")

    if len(st.session_state.chat_history) == 0:
        st.caption("No chats yet")

    for index, chat in enumerate(st.session_state.chat_history):

        if st.button(
            chat["title"],
            key=f"chat_{index}",
            use_container_width=True,
        ):

            st.session_state.messages = chat["messages"].copy()
            st.session_state.current_chat_index = index
            st.rerun()


for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.write(message["content"])


prompt = st.chat_input(
    "Ask anything about admissions, courses, placements..."
)

if prompt:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Assistant Response
    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        answer = ""

        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages,
            stream=True,
        )

        for chunk in stream:

            if chunk.choices[0].delta.content:

                token = chunk.choices[0].delta.content

                answer += token

                response_placeholder.markdown(answer + "▌")

        response_placeholder.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )



    title = "New Chat"

    for msg in st.session_state.messages:

        if msg["role"] == "user":
            title = msg["content"][:40]
            break

    chat_data = {
        "title": title,
        "messages": st.session_state.messages.copy(),
    }

    if st.session_state.current_chat_index is None:

        st.session_state.chat_history.append(chat_data)

        st.session_state.current_chat_index = (
            len(st.session_state.chat_history) - 1
        )

    else:

        st.session_state.chat_history[
            st.session_state.current_chat_index
        ] = chat_data