# GOF 1
#Kollin Schalhamer
#CIS-125
import random
def main():

    world =[]
    height = 22
    width = 80

    for x in range(h):
        row = []
    for y in range(w):
        r = random.randint(0,1)    
        if r == 0:
            row.append("_")
        else:
            row.append("*")
        
        stuff.append(row)

#Function display
#Pre condtion
#   world is populated
#Post condtion none
def display(petri_dish, h = height, w = width):
    worldString = ""
    for x in range(h):
        rowString = ""
        for y in range(w):
            rowString += petri_dish[x][y]
        worldString += rowString +"\n"
    print(worldString)
    

    populate(world,h,w)
    display(world,h,w)
    
    userIn = input("Press any key, Q stops the program: ")
    while userIn != "Q":
        
        display (world,h,w)
        generation(world,h,w)
        
        UserIn = input("Press a key, Q stops the program: ")
    print("Goodbye!")
#This function populates the world    
    
def populate(world,h,w):
    
    pass 
#this function displays the world

def display(world,h,w):
    
    
    pass
#this function creates a new world for each generation and decided on whether cells live or die
def generation(world,h,w):
    pass

main() 

    
