const chatbox = document.getElementById("chatbox");
const input = document.getElementById("msgInput");
const sendBtn = document.getElementById("sendBtn");

/* -------- CHAT UI -------- */
function addMsg(text, type) {
  const div = document.createElement("div");
  div.className = `message ${type}`;
  div.innerHTML = text.replace(/\n/g, "<br>");
  chatbox.appendChild(div);
  chatbox.scrollTop = chatbox.scrollHeight;
}

/* -------- SEND MESSAGE -------- */
async function sendMessage() {
  const msg = input.value.trim();
  if (!msg) return;

  addMsg(msg, "user");
  input.value = "";

  try {
    const res = await fetch(`/chat?message=${encodeURIComponent(msg)}`);
    const data = await res.json();

    addMsg(data.reply, "bot");
  } catch (err) {
    addMsg("⚠️ Server not responding. Please try again.", "bot");
    console.error(err);
  }
}

/* -------- EVENTS (MOBILE SAFE) -------- */
sendBtn.addEventListener("click", sendMessage);
sendBtn.addEventListener("touchstart", e => {
  e.preventDefault();
  sendMessage();
});

input.addEventListener("keydown", e => {
  if (e.key === "Enter") sendMessage();
});

/* QUICK BUTTONS */
function quickSend(text) {
  input.value = text;
  sendMessage();
}

/* -------- PARTICLES -------- */
const canvas = document.getElementById("particles");
const ctx = canvas.getContext("2d");

function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
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

/* -------- WELCOME -------- */
addMsg("Hi 🌱 How are you feeling today?", "bot");
function addTyping() {
  const div = document.createElement("div");
  div.className = "message bot";
  div.textContent = "Typing...";
  chatbox.appendChild(div);
  chatbox.scrollTop = chatbox.scrollHeight;
  return div;
}
