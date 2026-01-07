from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List, Dict

app = FastAPI(title="Mental Wellness Companion Bot")

app.mount("/static", StaticFiles(directory="static"), name="static")

sessions: Dict[str, List[Dict]] = {}

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/chat")
def chat(message: str = "hello"):
    msg_lower = message.lower()
    response = next(
        (v for k, v in WELLNESS_RESPONSES.items() if k in msg_lower),
        WELLNESS_RESPONSES["default"]
    )

    session_id = "user1"
    sessions.setdefault(session_id, []).append(
        {"user": message, "bot": response}
    )

    return {"reply": response}
