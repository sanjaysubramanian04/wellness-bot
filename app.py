from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Dict, List

# --------------------------
# 1. Initialize app
# --------------------------
app = FastAPI(title="Mental Wellness Companion Bot")

# --------------------------
# 2. Static & Templates
# --------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --------------------------
# 3. Wellness Responses
# --------------------------
WELLNESS_RESPONSES = {
    "stress": "🌿 Box Breathing:\nInhale 4s → Hold 4s → Exhale 4s → Hold 4s\nRepeat 5x.",
    "anxious": "💙 5-4-3-2-1 grounding technique.\nYou are safe.",
    "sad": "❤️ Write 3 things you're grateful for.\nSmall wins matter.",
    "sleep": "😴 4-7-8 breathing.\nDark room, no phone.",
    "happy": "🎉 What made you smile today? Keep it going ✨",
    "angry": "🔥 Pause, breathe slow, relax fists.",
    "focus": "🧠 Pomodoro: 25 min work, 5 min break.",
    "motivation": "⚡ Start for just 2 minutes.",
    "exam": "📚 Revise → Walk → Sleep well.",
    "overwhelmed": "🌊 Write 3 tasks. Do 1.",
    "default": "🤗 I'm here for you. Tell me how you feel."
}

# --------------------------
# 4. Session Storage
# --------------------------
sessions: Dict[str, List[Dict]] = {}

# --------------------------
# 5. Request Model
# --------------------------
class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

# --------------------------
# 6. Root Route (FIXED)
# --------------------------
@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# --------------------------
# 7. GET Chat Endpoint
# --------------------------
@app.get("/chat")
def chat(message: str):
    msg = message.lower()
    response = next(
        (v for k, v in WELLNESS_RESPONSES.items() if k in msg),
        WELLNESS_RESPONSES["default"]
    )
    return {"reply": response}

# --------------------------
# 8. Run Locally
# --------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
