# 🤖 Internship FAQ Chatbot (Rasa + Streamlit)

A smart chatbot built with [Rasa](https://rasa.com/) and [Streamlit](https://streamlit.io/) to answer frequently asked questions related to internships, applications, and more.

---

## 🚀 How It Works

1. **User Input**: Users type a message into the chatbot interface (via Streamlit).
2. **Frontend**: Streamlit sends the message to the Rasa backend via REST API.
3. **NLU**: Rasa extracts intent and entities from the message.
4. **Core**: Based on the conversation history and trained rules/stories, Rasa decides the appropriate response.
5. **Response**: The response is sent back to Streamlit and displayed to the user above the input box (like WhatsApp).

---
## ✨ Features

- 🔍 **FAQ Bot**: Pre-trained on common internship and application questions.
- 📜 **Rule-based Logic**: Uses `rules.yml` to handle simple logic flows.
- 💬 **Streamlit UI**: Simple chat interface.
- ⚙️ **REST API Integration**: Connects frontend and backend smoothly.
- 📦 **Modular Design**: Easy to maintain and extend.

---
## 🛠️ Tech Stack

| Component    | Tool / Library        |
|--------------|------------------------|
| Chatbot NLP  | Rasa                   |
| Interface    | Streamlit              |
| Programming  | Python 3.8+            |
| Deployment   | Localhost / Cloud-ready|
| Communication | REST API              |

  

# Backend server

Sever handling the user quries 

https://github.com/user-attachments/assets/adaea8d2-74e7-4446-90bb-00311d9377f0

# User Interface 

This is  theInterface of Chatbot  
![Screenshot 2025-06-12 180609](https://github.com/user-attachments/assets/839bd789-2e0a-4710-b42c-ac0d8a9fa379)





---
## 🔮 Future Enhancements

- ✅ Add **support for contextual conversations** using stories.
- ✅ Integrate with **custom action server** for dynamic data (e.g., fetching deadlines).
- ✅ Add **voice input/output** using speech-to-text and text-to-speech.
- ✅ Deploy using **Docker** or on **cloud platforms** (Render, Azure, GCP).
- ✅ Add **authentication or session tracking** for users.
- ✅ Store chat logs in a **database** (MongoDB or PostgreSQL).
- ✅ Multilingual support with language detection.

---



---


##  Clone the Repo

```bash
git clone https://github.com/Syam-Doppasani/MIT-chatbot
cd MIT-chatbot
```
