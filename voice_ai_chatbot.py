import os
import speech_recognition as sr
import pyttsx3
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

r = sr.Recognizer()

print("Voice AI started. Say 'exit' to stop.")

conversation = [
    {"role": "system", "content": "You are a friendly, intelligent AI assistant. Talk naturally like ChatGPT."}
]

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=8)


        user_text = r.recognize_google(audio)
        print("You:", user_text)

        if user_text.lower() in ["exit", "quit", "stop"]:
            speak("Bye, take care!")
            break

        conversation.append({"role": "user", "content": user_text})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation
        )

        reply = response.choices[0].message.content
        print("AI:", reply)

        conversation.append({"role": "assistant", "content": reply})

        speak(reply)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except Exception as e:
        print("Error:", e)
