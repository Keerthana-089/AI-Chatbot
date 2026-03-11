import json
import random
import pickle
import speech_recognition as sr
import pyttsx3

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open("intents.json") as f:
    intents = json.load(f)

user_name = None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def get_response(text):
    global user_name

    vec = vectorizer.transform([text])
    tag = model.predict(vec)[0]

    if tag == "set_name":
        words = text.split()
        if len(words) > 2:
            user_name = words[-1].capitalize()
            return f"Okay {user_name}, I will remember your name"

    if tag == "get_name":
        return f"Your name is {user_name}" if user_name else "I don't know your name yet"

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand that"

r = sr.Recognizer()
print("Chatbot started. Say 'exit' to stop.")

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, 0.5)
        audio = r.listen(source)

    try:
        user_text = r.recognize_google(audio)
        print("You:", user_text)

        if "exit" in user_text.lower():
            speak("Bye")
            break

        reply = get_response(user_text.lower())
        print("Bot:", reply)
        speak(reply)

    except:
        print("Could not understand")
