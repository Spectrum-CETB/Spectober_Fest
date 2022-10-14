'use strict';

//adding player names
let name0D=document.querySelector('#name--0');
let name1D=document.querySelector('#name--1');
name0D.textContent=prompt('Enter Player 1 Name');
name1D.textContent=prompt('Enter Player 2 Name');

//selecting elements
let currentScore = 0;
let activePlayer = 0;
const player0D = document.querySelector('.player--0');
const player1D = document.querySelector('.player--1');
const score0D = document.querySelector('#score--0');
const score1D = document.getElementById('score--1');
const dice = document.querySelector('.dice');
const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');


//starting conditions
score0D.textContent = 0;
score1D.textContent = 0;
dice.classList.add('hidden');
let finalScores = [0, 0];


//rolling dice funtionality
btnRoll.addEventListener('click', function () {
    const diceVal = Math.trunc(Math.random() * 6) + 1;
    dice.classList.remove('hidden');
    dice.src = `img/dice-${diceVal}.png`;
    if (diceVal !== 1) {
        //adding value to current score
        currentScore += diceVal;
        document.getElementById(`current--${activePlayer}`).textContent = currentScore;
    }
    else {
        //switching to next player
        switchPlayers();
    }

});

//hold button press functionality
btnHold.addEventListener('click', function () {
    if (activePlayer === 0) {
        finalScores[0] += currentScore;
        score0D.textContent=finalScores[0];
    }
    else {
        finalScores[1] += currentScore;
        score1D.textContent=finalScores[1];
    }
    if(finalScores[activePlayer]>=100){
        modal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        if(activePlayer==0){
            document.querySelector('.win').textContent=(name0D.textContent).toUpperCase();
        }
        else{
            document.querySelector('.win').textContent=(name1D.textContent).toUpperCase();
        }
        btnNew.style.top='63rem';
        btnNew.style.backgroundColor='white';
    }
    switchPlayers();
});

//switching players function
function switchPlayers(){
    document.getElementById(`current--${activePlayer}`).textContent = 0;
    activePlayer = activePlayer === 0 ? 1 : 0;
    currentScore = 0;
    player0D.classList.toggle('player--active');
    player1D.classList.toggle('player--active');
};

//reseting the game functionality
btnNew.addEventListener('click',function(){
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
    btnNew.style.top='10rem';
    currentScore=0;
    finalScores[0]=0;
    finalScores[1]=0;
    score0D.textContent=finalScores[0];
    score1D.textContent=finalScores[1];
    dice.classList.add('hidden');
    btnNew.style.backgroundColor='rgba(255, 255, 255, 0.6)';
    activePlayer=0;
    player0D.classList.add('player--active');
    player1D.classList.remove('player--active');
});