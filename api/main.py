from fastapi import FastAPI
from pydantic import BaseModel
import os
import google.generativeai as genai

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Xylo AI is ready 🚀"}


@app.post("/chat")
def chat(req: ChatRequest):
    user_input = req.message

    response = model.generate_content(user_input)

    return {"response": response.text}