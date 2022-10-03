import random

i = 1
minePoints = 0
compPoints = 0
numOfTurns = int(input("Number of turns: "))

while(i <= numOfTurns):
    options = {
        1 : "rock",
        2 : "paper",
        3 : "scissor"
    }
    a = random.randint(1, 3)
    b = input("Enter your choice (rock(r)/paper(p)/scissor(s)): ").lower()
    if (b in ["rock", "r", "1" ]):
        x = 1
        i = i + 1
    elif (b in ["paper", "p", "2" ]):
        x = 2
        i = i + 1
    elif (b in ["scissor", "s", "3" ]):
        x = 3
        i = i + 1
    else:
        print("Enter a valid option")
        continue

    print(f"Computer showed {options[a]}.")
    if(x == a):
        print("Draw.\n")
    elif((x == 1 and a == 3) or (x == 2 and a == 1) or (x == 3 and a == 2)):
        print("You Win.\n")
        minePoints = minePoints + 1
    else:
        print("You Lose.\n")
        compPoints = compPoints + 1


if (minePoints > compPoints):
    print(f"You are the winner! You won by {minePoints-compPoints} points.")
elif(minePoints < compPoints):
    print(f"Comp is the winner. You lost by {compPoints-minePoints} points.")
else:
    print("Match Draw.")
