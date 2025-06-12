import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="FAQ Chatbot", layout="centered")

st.markdown("<h2 style='text-align: center;'>📲 Internship FAQ Chatbot</h2>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Reverse chat history: newer messages at the bottom
with st.container():
    st.markdown("### 💬 Chat History")
    for msg in reversed(st.session_state.messages):
        sender = msg["sender"]
        text = msg["text"]

        if sender == "user":
            st.markdown(
                f"<div style='text-align: right; background-color: #DCF8C6; padding: 8px; border-radius: 10px; margin-bottom: 5px;'>{text}</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div style='text-align: left; background-color: #F1F0F0; padding: 8px; border-radius: 10px; margin-bottom: 5px;'>{text}</div>",
                unsafe_allow_html=True,
            )

# Create a bottom input box using form to avoid rerender
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:", placeholder="Type your question here...", label_visibility="collapsed")
    submit = st.form_submit_button("Send")

if submit and user_input.strip():
    # Append user message
    st.session_state.messages.append({"sender": "user", "text": user_input})

    try:
        # Send user input to Rasa
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_input},
        )

        if response.status_code == 200:
            bot_responses = response.json()
            for bot_msg in bot_responses:
                if "text" in bot_msg:
                    st.session_state.messages.append({"sender": "bot", "text": bot_msg["text"]})
        else:
            st.session_state.messages.append({"sender": "bot", "text": "❌ Error: Unable to get response from Rasa server."})

    except Exception as e:
        st.session_state.messages.append({"sender": "bot", "text": f"❌ Exception occurred: {str(e)}"})
