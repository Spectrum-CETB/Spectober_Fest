# input the strings
s = input()
t = input()
inputstr = [*s]
outputstr = [*t]
if sorted(inputstr) != sorted(outputstr):
    print('FALSE')
else:
    print('TRUE')    
        
