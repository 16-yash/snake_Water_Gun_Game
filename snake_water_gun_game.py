"""
Game : 
SNAKE , WATER , GUN 

3 Conditions And Rules Of These Game : 

Snake kills water
Water kills Gun
Gun kills Snake

"""

import random 
game_char = ["SNAKE", "WATER", "GUN"]
system = random.choice(game_char)
sp =0
up =0
# print("Snake\nWater\nGun")
# uc = input.lower()("Enter Your Choice")
print("SNAKE , WATER , GUN\nYour Game is Against Computer\n")
turns = int(input("How Many Turns You Want To Take :\n"))
print("Snake - 'S' \nWater 'W' \nGun 'G'\n")
for a in range(0,turns):
    game_char = ["SNAKE", "WATER", "GUN"]
    system = random.choice(game_char)
    uc = input("Enter Your Choice  :\n")
    print("Computer  - ",system, "Player - ",uc)
    if uc == system:
        
        print("Both Are Equal\nBoth Got Equal Point\n")
        sp = sp+1
        up = up+1
    elif uc == 'G' and system == 'WATER':
        
        print("Computer Wins This Turn\n")
        sp = sp+1
    elif uc == 'G' and system == 'SNAKE':

        print("Player Wins This Turn\n")
        up = up +1

    elif uc == 'S' and system == 'GUN':
        
        print("Computer Wins Win This Turn\n")
        sp = sp+1
    elif uc == 'S' and system == 'WATER':






        

        print("Player Win This Turn\n")
        up = up+1

    elif uc == 'W' and system == 'SNAKE':
        
        print("Computer Wins This Turn\n")
        sp = sp+1
    elif uc == 'W' and system == 'GUN':

        print("Player Win This Turn\n")
        up =up+1
    elif uc == 'W' and system == 'WATER':
        print("Both Get One Point\nNo One Win This turn\n")  
        sp = sp+1
        up = up+1 
print("Computer Score - ",sp)
print("Player Score - ",up)   
if sp > up:
    print("COMPUTER WIN THE GAME\nTry Again")
elif up > sp:
    print("PLAYER WIN THE GAME\nTRY AGAIN")
elif up == sp:
    print("Tie Between Computer and Player\nTRY AGAIN")            

