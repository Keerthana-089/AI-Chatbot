<<<<<<< HEAD
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Error:", e)
=======
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Error:", e)
>>>>>>> 85e5519c1167f1606a3bd7aa42cf6912b89b92fc
