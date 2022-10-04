const engtoMorseDict = {
  A: ".-",
  B: "-...",
  C: "-.-.",
  D: "-..",
  E: ".",
  F: "..-.",
  G: "--.",
  H: "....",
  I: "..",
  J: ".---",
  K: "-.-",
  L: ".-..",
  M: "--",
  N: "-.",
  O: "---",
  P: ".--.",
  Q: "--.-",
  R: ".-.",
  S: "...",
  T: "-",
  U: "..-",
  V: "...-",
  W: ".--",
  X: "-..-",
  Y: "-.--",
  Z: "--..",
  1: ".----",
  2: "..---",
  3: "...--",
  4: "....-",
  5: ".....",
  6: "-....",
  7: "--...",
  8: "---..",
  9: "----.",
  0: "-----",
  " ": ".......",
};

const morsetoEngDict = {
  ".-": "a",
  "-...": "b",
  "-.-.": "c",
  "-..": "d",
  ".": "e",
  "..-.": "f",
  "--.": "g",
  "....": "h",
  "..": "i",
  ".---": "j",
  "-.-": "k",
  ".-..": "l",
  "--": "m",
  "-.": "n",
  "---": "o",
  ".--.": "p",
  "--.-": "q",
  ".-.": "r",
  "...": "s",
  "-": "t",
  "..-": "u",
  "...-": "v",
  ".--": "w",
  "-..-": "x",
  "-.--": "y",
  "--..": "z",
  ".----": "1",
  "..---": "2",
  "...--": "3",
  "....-": "4",
  ".....": "5",
  "-....": "6",
  "--...": "7",
  "---..": "8",
  "----.": "9",
  "-----": "0",
  ".......": " ",
};

function convertToMorse(word) {
  let result = "";
  for (let char of word) {
    char = char.toLocaleUpperCase();
    result += engtoMorseDict[char] + " ";
  }
  return result;
}

function convertToEng(morse) {
  let word = " ";
  let morseArr = morse.split(" ");
  for (let code of morseArr) {
    word += morsetoEngDict[code];
  }
  return word;
}
function handleClick() {
  const textbox = document.querySelector("input").value;
  const check = document.querySelector("input:checked");
  const display = document.querySelector("p");
  if (check === null) {
    alert("Choose a type of conversion...");
    return;
  }
  if (check.value == 1) {
    if (textbox == "") {
      alert("Enter some text to get started -__-");
      return;
    } else {
      let result = convertToMorse(textbox);
      display.textContent = result;
    }
  }
  else if (check.value == 0) {
    if (textbox == "") {
      alert("Enter some text to get started -__-");
      return;
    } else {
      let result = convertToEng(textbox);
      display.textContent = result;
    }
  }
}
