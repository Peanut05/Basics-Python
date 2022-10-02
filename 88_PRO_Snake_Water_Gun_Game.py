import random
# Snake water gun game
def gamewin(comp , you):
    # if two values are equal,declare tie

    if comp == you:
        return None
    # if computer chose 's'

    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True   
    # if computer chose 'w'    
        
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True 
    # if computer chose 'g' 
    
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True     
   

print("comp turn: Snake(s) Water(w) or Gun(g)?")
randnumber = random.randint(1,3)
print(randnumber)
if randnumber == 1:
    comp = 's'
    
elif randnumber == 2:
    comp = 'w'

elif randnumber == 3:
    comp = 'g'

you = input("Your's turn: Snake(s) Water(w) or Gun(g)")

a = gamewin(comp , you)

print("Computer Chose",comp)
print("You Chose",you)
if a == None:
    print("The game is tie! ")
elif a:
    print("You Win !")
else:
    print("You Lose !")

    
