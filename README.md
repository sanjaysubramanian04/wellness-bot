# 🤖 Mental Wellness Companion Bot – Rule-Based AI System

The Mental Wellness Companion Bot is a web-based application designed to provide **basic emotional support through structured conversations**.  
This system uses a **rule-based AI approach**, ensuring predictable and controlled responses without relying on machine learning models or databases.

---

# 🌐 Live Demo
https://wellness-bot.vercel.app/

---

# 🏗️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript  

### Backend
- Python  
- FastAPI  

### AI Approach
- Rule-Based Logic System  
- Keyword and pattern-based responses  
- Predefined conversational flows  

### Deployment
- Vercel (Frontend Hosting)  
- FastAPI backend deployed as API service  

---

# 🔄 Complete System Workflow

## 1️⃣ User Interaction
- User enters a message in the chat interface  
- Input is captured using JavaScript  

---

## 2️⃣ Frontend Processing
- Sends request to backend API using `fetch`  
- Displays user messages instantly  
- Waits for backend response  

---

## 3️⃣ API Communication
- Frontend sends a `POST` request:
- Data is sent in JSON format  

---

## 4️⃣ Backend Processing (FastAPI)

### 🔹 Input Handling
- Receives user message  
- Preprocesses text (lowercase, keyword detection)  

---

### 🔹 Rule-Based Engine
- Matches user input with predefined rules:
  - Greetings  
  - Stress / anxiety keywords  
  - General conversation patterns  

- Selects appropriate response based on rules  

---

### 🔹 Response Generation
- Returns structured response:
  - Message text  
  - Context-based reply  

---

## 5️⃣ No Database Design
- No user data is stored  
- Ensures:
  - Privacy  
  - Lightweight system  
  - Faster response time  

---

## 6️⃣ Frontend Display
- Displays chatbot response dynamically  
- Maintains chat-like UI  
- Smooth and responsive interaction  

---

# 🔗 Project Link

- Live Application: https://wellness-bot.vercel.app/ 

---

# 🔒 Project Note
This repository contains the **complete implementation of the chatbot system**, focusing on simplicity, privacy, and structured interaction.

---
## 📄 License
This project is licensed under the MIT License.

---

# 🎯 Key Highlights
- Rule-based AI chatbot (No ML/LLM used)  
- Built using FastAPI for high performance  
- No database dependency  
- Privacy-focused design  
- Clean
