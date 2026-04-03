from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# 🔑 Paste your API key here
genai.configure(api_key="AIzaSyDTTsEIvtcAO9PNoeCy_Q2Bbmp8RbgkAUo")

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