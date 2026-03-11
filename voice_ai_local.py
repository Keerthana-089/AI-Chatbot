import speech_recognition as sr
import pyttsx3
import ollama

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

r = sr.Recognizer()

print("FREE Local Voice AI started. Say 'exit' to stop.")

conversation = [
    {
        "role": "system",
        "content": "You are a friendly assistant. Keep answers short and clear."
    }
]


while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, 0.5)
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=8)

        user_text = r.recognize_google(audio)
        print("You:", user_text)

        if user_text.lower() in ["exit", "quit", "stop"]:
            speak("Bye, take care")
            break

        conversation.append({"role": "user", "content": user_text})

        response = ollama.chat(
            model="mistral",
            messages=conversation
        )

        reply = response["message"]["content"]
        print("AI:", reply)

        conversation.append({"role": "assistant", "content": reply})

        speak(reply)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except Exception as e:
        print("Error:", e)
