from fastapi import FastAPI
from pydantic import BaseModel
import os
import google.generativeai as genai

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
print("API KEY:", os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Xylo AI is ready 🚀"}


@app.post("/chat")
def chat(req: ChatRequest):
    try:
        print("User:", req.message)

        response = model.generate_content(req.message)

        print("Gemini:", response.text)

        return {"response": response.text}

    except Exception as e:
        print("ERROR:", str(e))
        return {"response": "⚠️ Error: " + str(e)}