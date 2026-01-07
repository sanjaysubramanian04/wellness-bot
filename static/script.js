const API_URL = 'http://localhost:8000/chat';
let sessionId = localStorage.getItem('sessionId') || null;

const messagesEl = document.getElementById('messages');
const inputEl = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const crisisNotice = document.getElementById('crisis-notice');

// Particles background
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
let particles = [];

class Particle {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 3 + 1;
        this.speedX = Math.random() * 0.5 - 0.25;
        this.speedY = Math.random() * 0.5 - 0.25;
    }
    update() {
        this.x += this.speedX;
        this.y += this.speedY;
        if (this.x > canvas.width || this.x < 0) this.speedX = -this.speedX;
        if (this.y > canvas.height || this.y < 0) this.speedY = -this.speedY;
    }
    draw() {
        ctx.fillStyle = 'rgba(255,255,255,0.5)';
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

for (let i = 0; i < 100; i++) particles.push(new Particle());

function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    requestAnimationFrame(animateParticles);
}
animateParticles();

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

function addMessage(role, content, isTyping = false) {
    const msg = document.createElement('div');
    msg.className = `message ${role} ${isTyping ? 'typing' : ''}`;
    msg.textContent = content;
    messagesEl.appendChild(msg);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

function typeMessage(content, callback) {
    const msg = document.createElement('div');
    msg.className = 'message assistant typing';
    messagesEl.appendChild(msg);
    messagesEl.scrollTop = messagesEl.scrollHeight;
    
    let i = 0;
    const typer = setInterval(() => {
        msg.textContent = content.slice(0, i);
        i++;
        if (i > content.length) {
            clearInterval(typer);
            msg.classList.remove('typing');
            if (callback) callback();
        }
    }, 30);
}

async function sendMessage() {
    const message = inputEl.value.trim();
    if (!message) return;
    
    addMessage('user', message);
    inputEl.value = '';
    sendBtn.disabled = true;
    
    try {
        const res = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message, session_id: sessionId })
        });
        const data = await res.json();
        sessionId = data.session_id;
        localStorage.setItem('sessionId', sessionId);
        
        if (data.is_crisis) {
            crisisNotice.textContent = data.reply + ' 💙';
            crisisNotice.classList.remove('hidden');
            setTimeout(() => crisisNotice.classList.add('hidden'), 10000);
        } else {
            typeMessage(data.reply);
        }
    } catch (err) {
        addMessage('assistant', 'Sorry, having trouble connecting. Try again?');
    }
    sendBtn.disabled = false;
}

sendBtn.addEventListener('click', sendMessage);
inputEl.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

// Welcome message
addMessage('assistant', 'Hello! I\'m your Wellness Companion. 🌱 Share how you\'re feeling, or ask for tips on stress, anxiety, or mindfulness.');
