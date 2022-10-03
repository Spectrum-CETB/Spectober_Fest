const SPEED_SCALE = 0.00001;

const game = document.querySelector("#game");
const scoreDisplay = document.querySelector("#score");
const startMessage = document.querySelector("#start-message");
const gameoverMessage = document.querySelector("#gameover-message");

document.addEventListener("keydown", startGame, { once: true });

let lastTime;
let speedScale;
let score;

// update animation frame
function update(time) {
  if (lastTime == null) {
    lastTime = time;
    window.requestAnimationFrame(update);
    return;
  }

  const timeDiff = time - lastTime;

  updateGround(timeDiff, speedScale);
  updateDino(timeDiff, speedScale);
  updateCactus(timeDiff, speedScale);
  updateSpeedScale(timeDiff);
  updateScore(timeDiff);

  if (checkGameOver()) return handleGameOver();

  lastTime = time;
  window.requestAnimationFrame(update);
}

function startGame() {
  lastTime = null;
  speedScale = 1;
  score = 0;
  setupGround();
  setupDino();
  setupCactus();
  startMessage.classList.add("hide");
  gameoverMessage.classList.add("hide");
  window.requestAnimationFrame(update);
}

/* speeds up the game over time */
function updateSpeedScale(timeDiff) {
  speedScale += timeDiff * SPEED_SCALE;
}

function updateScore(timeDiff) {
  score += timeDiff * 0.01;
  scoreDisplay.textContent = `Score:${Math.floor(score)}`;
}

/* check for collison */
function checkCollision(rect1, rect2) {
  return (
    rect1.left < rect2.right &&
    rect1.top < rect2.bottom &&
    rect1.right > rect2.left &&
    rect1.bottom > rect2.top
  );
}

function checkGameOver() {
  const dinoRect = getDinoRect();
  return getCactusRects().some((rect) =>
    checkCollision(rect, dinoRect)
  );
}

function handleGameOver() {
  setDinoLose();
  setTimeout(() => {
    document.addEventListener("keydown", startGame, {
      once: true,
    }); 
    gameoverMessage.classList.remove("hide");
  }, 100);
}

/* HANDLING CSS PROPERTIES */

/* get property value */
function getCustomProperty(elem, prop) {
  return parseFloat(getComputedStyle(elem).getPropertyValue(prop)) || 0;
}

/* set property value */
function setCustomProperty(elem, prop, value) {
  elem.style.setProperty(prop, value);
}

/* increment the property value */
function incrementCustomProperty(elem, prop, inc) {
  setCustomProperty(elem, prop, getCustomProperty(elem, prop) + inc);
}

/* GROUND MOVEMENT */

const GROUND_SPEED = 0.05;
const grounds = document.querySelectorAll(".ground");

function setupGround() {
  setCustomProperty(grounds[0], "--left", 0);
  setCustomProperty(grounds[1], "--left", 300);
}

function updateGround(timeDiff, speedScale) {
  grounds.forEach((ground) => {
    incrementCustomProperty(
      ground,
      "--left",
      timeDiff * speedScale * GROUND_SPEED * -1
    ); /* moves the ground according to game speed */

    if (getCustomProperty(ground, "--left") <= -300) {
      incrementCustomProperty(ground, "--left", 600); /* loop the elements */
    }
  });
}

/* DINOSAUR MOVEMENT */

const dino = document.querySelector("#dino");
const JUMP_SPEED = 0.45;
const GRAVITY = 0.0015;
const DINO_FRAME_COUNT = 2;
const FRAME_TIME = 100;

let isJumping;
let dinoFrame;
let currentFrameTime;
let yVel;

function setupDino() {
  isJumping = false;
  dinoFrame = 0;
  currentFrameTime = 0;
  yVel = 0;

  setCustomProperty(dino, "--bottom", 0);
  document.removeEventListener(
    "keydown",
    onJump
  );
  document.addEventListener("keydown", onJump);
}

function updateDino(timeDiff, speedScale) {
  handleRun(timeDiff, speedScale);
  handleJump(timeDiff);
}

function getDinoRect() {
  return dino.getBoundingClientRect();
}

function setDinoLose() {
  dino.src = "assets/dino-lose.png";
}

function handleRun(timeDiff, speedScale) {
  if (isJumping) {
    dino.src = `assets/dino-stationary.png`;
    return;
  }

  if (currentFrameTime >= FRAME_TIME) {
    dinoFrame = (dinoFrame + 1) % DINO_FRAME_COUNT;
    dino.src = `assets/dino-run-${dinoFrame}.png`;
    currentFrameTime -= FRAME_TIME;
  }
  currentFrameTime += timeDiff * speedScale;
}

function handleJump(timeDiff) {
  if (!isJumping) return;

  incrementCustomProperty(dino, "--bottom", yVel * timeDiff);

  if (getCustomProperty(dino, "--bottom") <= 0) {
    setCustomProperty(dino, "--bottom", 0);
    isJumping = false;
  }

  yVel -= GRAVITY * timeDiff;
}

function onJump(e) {
  if (e.code !== "Space" || isJumping) return;

  yVel = JUMP_SPEED;
  isJumping = true;
}

/* ADD CACTUS */

const CACTUS_SPEED = 0.05;
const CACTUS_INTERVAL_MIN = 500;
const CACTUS_INTERVAL_MAX = 2000;

let nextCactusTime;

function setupCactus() {
  nextCactusTime = CACTUS_INTERVAL_MIN;
  document.querySelectorAll(".cactus").forEach((cactus) => {
    cactus.remove(); 
  });
}

function updateCactus(timeDiff, speedScale) {
  document.querySelectorAll(".cactus").forEach((cactus) => {
    incrementCustomProperty(
      cactus,
      "--left",
      timeDiff * speedScale * CACTUS_SPEED * -1
    );
    if (getCustomProperty(cactus, "--left") <= -100) {
      cactus.remove();
    }
  });

  if (nextCactusTime <= 0) {
    createCactus();
    nextCactusTime =
      randomizer(CACTUS_INTERVAL_MIN, CACTUS_INTERVAL_MAX) / speedScale;
  }
  nextCactusTime -= timeDiff;
}

function getCactusRects() {
  return [...document.querySelectorAll(".cactus")].map((cactus) => {
    return cactus.getBoundingClientRect();
  });
}

function createCactus() {
  const cactus = document.createElement("img");
  cactus.src = "assets/cactus.png";
  cactus.classList.add("cactus");
  setCustomProperty(cactus, "--left", 100);
  game.append(cactus);
}

function randomizer(min, max) {
  return Math.floor(
    Math.random() * (max - min + 1) + min
  );
}
