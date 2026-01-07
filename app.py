from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Mental Wellness Companion Bot")

# Serve HTML/CSS/JS from static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

sessions: Dict[str, List[Dict]] = {}

WELLNESS_RESPONSES = {
    # Stress (keywords: stress, stressed, exam pressure, work stress, tension)
    "stress": "🌿 **Box Breathing Technique** (proven by US Navy SEALs):\n1. Inhale 4s (nose)\n2. Hold 4s\n3. Exhale 4s (mouth)\n4. Hold 4s\n**Repeat 5x**. Lowers cortisol 20% in 2 mins. You're doing great! 💪",
    
    # Anxiety (anxious, panic, worry, nervous, overthinking)
    "anxious": "💙 **5-4-3-2-1 Grounding** (stops panic attacks instantly):\n• 5 things you **see**\n• 4 things you **touch**\n• 3 things you **hear**\n• 2 things you **smell**\n• 1 thing you **taste**\n**Works 95% first try**. Breathe—you're safe now.",
    
    # Sad/Depressed (sad, depressed, down, lonely, empty)
    "sad": "❤️ **3 Gratitude Wins** (Harvard study: boosts happiness 25%):\n1. Today I'm grateful for...\n2. Someone who helped me...\n3. One small win I had...\n**Journal this**. Sadness passes—you matter. 🌟",
    
    # Sleep (sleep, insomnia, can't sleep, tired)
    "sleep": "😴 **Dr. Weil's 4-7-8 Method** (90% success rate):\n1. Inhale 4s (nose)\n2. Hold 7s\n3. Exhale 8s (mouth 'whoosh')\n**Repeat 4x**. + No screens 1hr before. Sleep coming... Zzz",
    
    # Happy/Joy (happy, good, great, excited)
    "happy": "🎉 **Joy Amplifier**! What made you smile today? 😊\n**Pro tip**: Share 1 positive daily → happiness x3 (psychology fact). Keep shining! ✨",
    
    # Anger (angry, mad, frustrated, rage)
    "angry": "🔥 **Anger Reset** (fist clench technique):\n1. Make tight fists (10s)\n2. Release slowly\n3. Deep breath\n4. Count to 10\n**Reduces rage 70%**. What triggered it? Let's process.",
    
    # Focus/Concentration (focus, concentrate, distracted, can't focus)
    "focus": "🧠 **Pomodoro + Environment Hack**:\n• Work 25min → Break 5min\n• Phone FACE DOWN, screen OFF\n• White noise (rain sounds)\n**Productivity +200%**. Start timer now! ⏱️",
    
    # Motivation (lazy, no motivation, procrastinate)
    "motivation": "⚡ **2-Min Rule** (from Atomic Habits):\n**Start 2min only** → momentum kicks in.\n+ Eat frog (hardest task first)\n**You're capable**—one step now! 🚀",
    
    # Exam/Study (exam, study, test, interview)
    "exam": "📚 **Exam Brain Hack**:\n1. Study 50min → Walk 10min\n2. Teach concept to rubber duck\n3. Sleep 8hrs (memory consolidates)\n**You know more than you think**. You've got this! 🏆",
    
    # Relationship (lonely, breakup, fight, relationship)
    "relationship": "💔 **Connection Reset**:\n1. Write what hurts (don't send)\n2. Call friend (not ex)\n3. Self-care date (bath/music)\n**Healthy boundaries first**. You deserve peace. 🌸",
    
    # Overwhelmed (overwhelmed, too much, busy)
    "overwhelmed": "🌊 **Priority Matrix**:\n**Do now**: Urgent + Important\n**Schedule**: Important only\n**Delegate**: Urgent only\n**Delete**: Rest\n**Breathe**. One task at a time—you're enough.",
    
    # Default (anything else)
    "default": "🤗 **Quick Check-in**:\nI'm listening. Try these **exact phrases**:\n• 'I'm stressed'\n• 'Feeling anxious'\n• 'Can't sleep'\n• 'Sad today'\n• 'Need focus'\nWhat's bothering you? 💬"
}


@app.get("/")
def root():
    return {"status": "Mental Wellness Bot ✅ LIVE", "chat": "http://127.0.0.1:8000/static/index.html"}

@app.get("/chat")
def chat(message: str = "hello"):
    msg_lower = message.lower()
    response = next((v for k, v in WELLNESS_RESPONSES.items() if k in msg_lower), WELLNESS_RESPONSES["default"])
    
    session_id = "user1"
    if session_id not in sessions:
        sessions[session_id] = []
    sessions[session_id].append({"user": message, "bot": response})
    
    return {
        "message": message,
        "reply": response,
        "session_history": sessions[session_id][-5:],
        "tip": "💡 Save this for your portfolio!"
    }

@app.post("/chat")
def chat_post(request: ChatRequest):
    msg_lower = request.message.lower()
    response = next((v for k, v in WELLNESS_RESPONSES.items() if k in msg_lower), WELLNESS_RESPONSES["default"])
    
    if request.session_id not in sessions:
        sessions[request.session_id] = []
    sessions[request.session_id].append({"user": request.message, "bot": response})
    
    return {"reply": response, "session_id": request.session_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
