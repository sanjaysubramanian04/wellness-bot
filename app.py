from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Dict, List

# --------------------------
# 1. Initialize app
# --------------------------
app = FastAPI(title="Mental Wellness Companion Bot")

# Serve static files (HTML/CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# --------------------------
# 2. Wellness Responses
# --------------------------
WELLNESS_RESPONSES = {
    "stress": "🌿 **Box Breathing Technique**:\n1. Inhale 4s\n2. Hold 4s\n3. Exhale 4s\n4. Hold 4s\nRepeat 5x. You got this!",
    "anxious": "💙 **5-4-3-2-1 Grounding**:\n• 5 things you see\n• 4 things you touch\n• 3 things you hear\n• 2 things you smell\n• 1 thing you taste. You are safe!",
    "sad": "❤️ **3 Gratitude Wins**:\n1. Today I'm grateful for...\n2. Someone who helped me...\n3. One small win I had today. Stay strong!",
    "sleep": "😴 **4-7-8 Breathing**:\n1. Inhale 4s\n2. Hold 7s\n3. Exhale 8s\nRepeat 4x. Sweet dreams!",
    "happy": "🎉 **Joy Amplifier**! What made you smile today? Keep shining! ✨",
    "angry": "🔥 **Anger Reset**:\n1. Clench fists 10s\n2. Release slowly\n3. Deep breath\n4. Count to 10. Relax!",
    "focus": "🧠 **Pomodoro Hack**:\nWork 25min → Break 5min. Keep phone away. Start now!",
    "motivation": "⚡ **2-Min Rule**: Start the task 2min only. Momentum kicks in. You can do it! 🚀",
    "exam": "📚 **Exam Brain Hack**:\nStudy 50min → Walk 10min → Teach concept → Sleep 8hrs. You've got this! 🏆",
    "relationship": "💔 **Connection Reset**:\nWrite what hurts, call friend, self-care. You deserve peace.",
    "overwhelmed": "🌊 **Priority Matrix**:\nDo now: urgent + important\nSchedule: important only\nDelegate: urgent only\nDelete: rest. Breathe!",
    "default": "🤗 I'm listening. Try these phrases:\n• 'I'm stressed'\n• 'Feeling anxious'\n• 'Can't sleep'\n• 'Sad today'\n• 'Need focus'"
}

# --------------------------
# 3. Session Storage
# --------------------------
sessions: Dict[str, List[Dict]] = {}

# --------------------------
# 4. ChatRequest Model
# --------------------------
class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

# --------------------------
# 5. Root Route (serve UI)
# --------------------------
@app.get("/")
def root():
    return FileResponse("static/index.html")

# --------------------------
# 6. GET Chat Endpoint
# --------------------------
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

    return {
        "message": message,
        "reply": response,
        "session_history": sessions[session_id][-5:]
    }

# --------------------------
# 7. POST Chat Endpoint
# --------------------------
@app.post("/chat")
def chat_post(request: ChatRequest):
    msg_lower = request.message.lower()
    response = next(
        (v for k, v in WELLNESS_RESPONSES.items() if k in msg_lower),
        WELLNESS_RESPONSES["default"]
    )
    
    sessions.setdefault(request.session_id, []).append(
        {"user": request.message, "bot": response}
    )

    return {"reply": response, "session_id": request.session_id}

# --------------------------
# 8. Run Locally
# --------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
