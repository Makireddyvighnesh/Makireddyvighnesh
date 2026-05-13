const header = document.querySelector("[data-header]");
const canvas = document.querySelector("#model-field");
const ctx = canvas.getContext("2d");
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

let width = 0;
let height = 0;
let ratio = 1;
let animationFrame = 0;

function setHeaderState() {
  header.classList.toggle("is-scrolled", window.scrollY > 18);
}

function resizeCanvas() {
  ratio = Math.min(window.devicePixelRatio || 1, 2);
  width = canvas.clientWidth;
  height = canvas.clientHeight;
  canvas.width = Math.floor(width * ratio);
  canvas.height = Math.floor(height * ratio);
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  drawField(0);
}

function drawField(time) {
  ctx.clearRect(0, 0, width, height);

  const grid = Math.max(52, Math.floor(width / 22));
  const drift = prefersReducedMotion.matches ? 0 : time / 2400;

  ctx.lineWidth = 1;
  for (let x = -grid; x < width + grid; x += grid) {
    const offset = Math.sin(x * 0.008 + drift) * 10;
    ctx.strokeStyle = "rgba(255, 255, 255, 0.045)";
    ctx.beginPath();
    ctx.moveTo(x + offset, 0);
    ctx.lineTo(x - offset * 0.6, height);
    ctx.stroke();
  }

  for (let y = -grid; y < height + grid; y += grid) {
    const offset = Math.cos(y * 0.009 + drift) * 8;
    ctx.strokeStyle = "rgba(255, 255, 255, 0.04)";
    ctx.beginPath();
    ctx.moveTo(0, y + offset);
    ctx.lineTo(width, y - offset);
    ctx.stroke();
  }

  ctx.strokeStyle = "rgba(241, 196, 109, 0.16)";
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  for (let x = 0; x <= width; x += 18) {
    const y = height * 0.34 + Math.sin(x * 0.012 + drift * 1.8) * 32;
    if (x === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.stroke();

  ctx.strokeStyle = "rgba(20, 107, 98, 0.22)";
  ctx.beginPath();
  for (let x = 0; x <= width; x += 18) {
    const y = height * 0.62 + Math.cos(x * 0.01 + drift * 1.4) * 36;
    if (x === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.stroke();
}

function animate(time) {
  drawField(time);
  animationFrame = requestAnimationFrame(animate);
}

function startField() {
  cancelAnimationFrame(animationFrame);
  if (prefersReducedMotion.matches) {
    drawField(0);
    return;
  }
  animationFrame = requestAnimationFrame(animate);
}

window.addEventListener("scroll", setHeaderState, { passive: true });
window.addEventListener("resize", resizeCanvas);
prefersReducedMotion.addEventListener("change", startField);

setHeaderState();
resizeCanvas();
startField();
