# GOF 1
#Kollin Schalhamer
#CIS-125
import random

world =[]
height = 22
width = 80

#Function populate world
#Pre conditions
#World is a list

#Post conditions
#World will contain random cells
def populate(stuff, h = height, w = width):
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