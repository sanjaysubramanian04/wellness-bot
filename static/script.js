const chatbox = document.getElementById("chatbox");
const input = document.getElementById("msgInput");
const sendBtn = document.getElementById("sendBtn");

/* -------- CHAT -------- */
function addMsg(text, type) {
  const div = document.createElement("div");
  div.className = `message ${type}`;
  div.textContent = text;
  chatbox.appendChild(div);
  chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
  const msg = input.value.trim();
  if (!msg) return;

  addMsg(msg, "user");
  input.value = "";

  const reply = getReply(msg);
  setTimeout(() => addMsg(reply, "bot"), 400);
}

/* MOBILE SAFE EVENTS */
sendBtn.addEventListener("click", sendMessage);
sendBtn.addEventListener("touchstart", e => {
  e.preventDefault();
  sendMessage();
});

input.addEventListener("keydown", e => {
  if (e.key === "Enter") sendMessage();
});

function quickSend(text) {
  input.value = text;
  sendMessage();
}

/* -------- BOT LOGIC -------- */
function getReply(msg) {
  msg = msg.toLowerCase();

  if (msg.includes("stress"))
    return "🧘 Stress relief:\n• Inhale 4 sec\n• Hold 4 sec\n• Exhale 6 sec\nRepeat 5 times.";

  if (msg.includes("anxiety") || msg.includes("anxious"))
    return "🌿 Anxiety grounding:\n5 things you see\n4 feel\n3 hear.";

  if (msg.includes("sad") || msg.includes("low"))
    return "💙 Feeling low?\nDrink water, sit in sunlight, write one good thought.";

  if (msg.includes("sleep"))
    return "😴 Better sleep:\nNo phone before bed\nDeep breathing\nDark room.";

  if (msg.includes("happy"))
    return "✨ Keep happiness alive:\nSmile\nShare joy\nDo what you love.";

  if (msg.includes("angry"))
    return "🔥 Anger reset:\nPause\nBreathe slow\nRelax body.";

  if (msg.includes("focus"))
    return "🎯 Focus tip:\n25 min work\n5 min break.";

  if (msg.includes("motivation"))
    return "🚀 Start for 2 minutes.\nAction creates motivation.";

  if (msg.includes("exam"))
    return "📚 Exam calm:\nTrust preparation\nBreathe slowly.";

  if (msg.includes("tired"))
    return "😌 Energy reset:\nWater\nStretch\nDeep breath.";

  if (msg.includes("overwhelmed"))
    return "🌊 Overwhelmed?\nWrite 3 tasks\nDo one.";

  return "🌱 Take a slow breath.\nYou’re doing your best.";
}

/* -------- PARTICLES -------- */
const canvas = document.getElementById("particles");
const ctx = canvas.getContext("2d");

function resize() {
  canvas.width = innerWidth;
  canvas.height = innerHeight;
}
resize();
window.addEventListener("resize", resize);

const particles = Array.from({ length: 40 }, () => ({
  x: Math.random() * canvas.width,
  y: Math.random() * canvas.height,
  r: Math.random() * 2 + 1,
  dx: Math.random() - 0.5,
  dy: Math.random() - 0.5
}));

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.x += p.dx;
    p.y += p.dy;
    if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
    if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(255,255,255,0.4)";
    ctx.fill();
  });
  requestAnimationFrame(animate);
}
animate();

/* WELCOME */
addMsg("Hi 🌱 How are you feeling today?", "bot");
