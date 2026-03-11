import streamlit as st
import speech_recognition as sr
import pyttsx3
import ollama
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="My AI Chatbot",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")
voice_enabled = st.sidebar.toggle("🔊 Voice Reply", value=True)

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = [{
        "role": "system",
        "content": "You are a friendly AI assistant. Keep replies concise unless asked otherwise."
    }]
    st.session_state.user_name = None
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption("Local • Free • Streamlit")

# ---------------- HEADER ----------------
st.title("🤖 My AI Chatbot")
st.caption("Local • Free • Voice Enabled")

# ---------------- INIT STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": "You are a friendly AI assistant. Keep replies concise unless asked otherwise."
    }]

if "user_name" not in st.session_state:
    st.session_state.user_name = None

# ---------------- TTS ----------------
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ---------------- SHOW CHAT ----------------
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# ---------------- INPUT ----------------
user_input = st.chat_input("Type your message here...")

col1, col2 = st.columns([1, 6])
with col1:
    speak_btn = st.button("🎤 Speak")
with col2:
    st.empty()

# ---------------- VOICE INPUT ----------------
if speak_btn:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        r.adjust_for_ambient_noise(source, 0.5)
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
    try:
        user_input = r.recognize_google(audio)
        st.success(f"You said: {user_input}")
    except:
        st.warning("Could not understand audio")

# ---------------- HANDLE INPUT ----------------
if user_input:
    # Name memory
    m = re.search(r"(my name is|call me)\s+(\w+)", user_input.lower())
    if m:
        st.session_state.user_name = m.group(2).capitalize()
        reply = f"Nice to meet you, {st.session_state.user_name} 😊"
    else:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = ollama.chat(
            model="phi3",  # switch to "mistral" if you want
            messages=st.session_state.messages
        )
        reply = response["message"]["content"]

        if st.session_state.user_name:
            reply = reply.replace("you", st.session_state.user_name, 1)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    if voice_enabled:
        speak(reply)

    st.rerun()
