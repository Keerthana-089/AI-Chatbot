from fastapi import FastAPI
from pydantic import BaseModel
import os
import google.generativeai as genai

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(req.message)

        return {"response": response.text}

    except Exception as e:
        return {"response": "⚠️ Error: " + str(e)}