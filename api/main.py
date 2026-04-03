from fastapi import FastAPI
from pydantic import BaseModel
import json
import random
import pickle
from pathlib import Path

app = FastAPI()

# Resolve assets from project root so this works regardless of launch directory.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load model + data
with open(BASE_DIR / "model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open(BASE_DIR / "vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

with open(BASE_DIR / "intents.json", "r", encoding="utf-8") as intents_file:
    intents = json.load(intents_file)

user_name = None

# Request schema
class ChatRequest(BaseModel):
    message: str

# Chatbot logic (your code reused)
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

# Routes
@app.get("/")
def home():
    return {"message": "AI Chatbot running 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    user_input = req.message.lower()
    response = get_response(user_input)
    return {"response": response}