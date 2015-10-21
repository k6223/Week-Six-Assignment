# GOF 1
#Kollin Schalhamer
#CIS-125
#Week 6 assignment

#Function populate
#Pre Conditions
#World is a list

#Post conditions 
#World will contain random cells

def populate(world, h =22, w =80):
    import random
    for x in range(h):
        row = []
        for y in range(w):
            r = random.randint(0,1)
            if r == 0:
                row.append('_')
            else:
                row.append('*')
        world.append(row)
#Function display

#Pre Conditions
#World is populated

#post Conditions
#no post conditions


def display(world, h =22, w =80):
    worldString = ''
    for x in range(h):
        rowString = ''
        for y in range(w):
            rowString += world[x][y]
        rowString += rowString + "\n"
    print(worldString)
    
    
#function generate
#generates new world based on whether cells are dead or alive

def generate(petri_dish, h =22, w =80):
    new_world = []
    for x in range(h):
        row = []
        for y in range(w):
            row.append(0)
        new_world.append(1)
        
    print("New World")
    print(new_world)
    n = 0
    for x in range(1, h-1):
        for y in range(1,w-1):
            n = petri_dish[x-1][y-1] + \
                petri_dish[x-1][y] + \
                petri_dish[x-1][y+1] + \
                petri_dish[x][y-1] + \
                petri_dish[x][y+1] + \
                petri_dish[x+1][y-1] + \
                petri_dish[x+1][y] + \
                petri_dish[x+1][y+1] + \
        if petri_dish[x][y]:
            if n== 3:
                new_world[x][y] = 0
                
                
        else:
            if n < 2 or n > 3:
                new_world[x][y] = 0
                
    petri_dish = new_world
    
    
#Function main

    world = []
    height = 22
    width = 80
    populate(world, height, width)
    display(world, height, width)
    k = input("Press any key to continue (q to quit): ")
    if k != "q":
        generate(world, height, width)
        display(world, height, width)
        k = input("Press any key to continue (q to quit): ")
        if k == "q":
            print("Goodbye!")
            
            
if __name__ == "__main__":
    main()
    
    
            