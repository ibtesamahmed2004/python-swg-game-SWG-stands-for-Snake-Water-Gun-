import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]


print(f"You Choose: {reverseDict[you]}\nComputer choose: {reverseDict[computer]}")

if(computer == you):
    print("Its Draw")
    
else:
    if(computer == -1 and you == 1):
        print("Winner Winner Chicken Dinner\n Congradulations You Won the Game")
        
    elif(computer == -1 and you == 0):
        print("You Lost the Game\nBetter Luck Next Time")
        
    elif(computer == 1 and you == -1):
        print("You Lost the Game\nBetter Luck Next Time")
        
    elif(computer == 1 and you == 0):
        print("Winner Winner Chicken Dinner\nCongradulations You Won the Game")
        
    elif(computer == 0 and you == -1):
        print("Winner Winner Chicken Dinner\nCongradulations You Won the Game")
        
    elif(computer == 0 and you == 1):
        print("You Lost the Game\nBetter Luck Next Time")
        
    else:
        print("SomeThing Went Wrong")
        