from random import randint

print('welcome to snakes & ladders game')

color=['blue','yellow','red','green']
A=input('player 1!choose any colour from blue,yellow,red,green: ')
print(f'a choose: {A}')
B=input('player 1!choose any colour from blue,yellow,red,green: ')
print(f'a choose: {B}')
snakes={97:10,
            93:12,
           85:23,
           75:45,
           78:56,
           63:43,
           54:28,
           42:4,
           32:18}

ladders={5:36,
             12:25,
             20:57,
             31:83,
             40:59,
             55:84,
             66:71,
             72:92,
             81:95
             }


pos1=0
pos2=0
last_pos=100

def newpos(pos):
        dice = randint(1, 6)
        print(dice)
        pos=pos+dice
        if pos in snakes:
            print(f'bitten by snake at {pos}')
            pos=snakes[pos]
        if pos in ladders:
            print(f'climbed a ladder at {pos}')
            pos=ladders[pos]
        if pos >>last_pos:
            pos=pos-dice

        return pos

while True:
    d=input(f'{A} player 1 enter A to roll the dice ')
    pos1=newpos(pos1)
    print(pos1)
    if pos1 == 100:
        print("game over")
        print(f'{A} player won! ')
        break

    e = input(f'{B} player 2 enter A to roll the dice ')
    pos2 = newpos(pos2)
    print(pos2)
    if pos2 == 100:
        print("game over")
        print(f'{B} player won! ')
        break




