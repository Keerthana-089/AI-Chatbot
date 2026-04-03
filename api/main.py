from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")


class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        response = model.generate_content(req.message)
        return {"response": response.text}
    except Exception as e:
        return {"response": "⚠️ Error: " + str(e)}