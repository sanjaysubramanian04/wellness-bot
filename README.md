# 🌿 Mental Wellness Companion Bot

A professional, empathetic AI chatbot for mental health support. Built with **FastAPI**, **LangChain**, **OpenAI**, and **RAG** from wellness PDFs. Features crisis detection, session memory, typing animations, and calming particle UI.

## 🚀 Live Demo
[Deployed Link] (Add after hosting)

## ✨ Features
- **Empathetic Responses**: Trained on coping strategies, mindfulness, stress relief.
- **RAG Knowledge Base**: Pulls from PDF docs (breathing exercises, coping skills).
- **Crisis Handling**: Detects keywords & provides Indian helplines (AASRA, Vandrevala).
- **Session Memory**: Remembers conversation history.
- **Pro UI**: Responsive, animated chat with particles, glassmorphism, typing effects.
- **Mobile-First**: Perfect on phones/tablets.

## 🛠 Tech Stack
- Backend: FastAPI + LangChain + OpenAI GPT-4o-mini
- Frontend: Vanilla HTML/CSS/JS (no frameworks for lightness)
- Vector DB: FAISS for PDF retrieval

## 📦 Quick Start
1. Clone & `pip install -r requirements.txt`
2. Add PDFs to `wellness_docs/` (see below)
3. Set `.env` with `OPENAI_API_KEY`
4. `uvicorn app:app --reload`
5. Open `http://localhost:8000/static/index.html`

## 📚 Wellness Docs (Download & Add)
- [101 Coping Skills](https://www.sacredheart.edu/media/shu-media/counseling-center/101_Coping_Skills_ADA.pdf)[web:49]
- [Coping Strategies Workbook](https://www.hse.ie/eng/about/who/cspd/ncps/mental-health/psychosis/coping-skills-workbook/coping-skills-developing-skills-for-ma...)[web:50]
- [Mindfulness Exercises](https://www.uhn.ca/Krembil/Clinics/Movement_Disorders/Documents/Mindfulness-Exercises.pdf)[web:57]
- [Stress Management](https://nams-india.in/downloads/LEAD/09-11May/Dr%20Sagar-Stress%20management%20for%20leaders.pdf)[web:55]

## 📱 Deployment
- Backend: Render.com (free)
- Frontend: Netlify (drag-drop static/)
- Fullstack: Vercel

## 🎯 Future Enhancements
- Voice input (Web Speech API)
- Mood analytics dashboard
- WhatsApp/Telegram integration
- Multi-language (Hindi/Tamil)

**Built for portfolio showcase. Demo video: [YouTube link]**

⭐ Star if helpful! #MentalHealth #AI #Python #FastAPI
