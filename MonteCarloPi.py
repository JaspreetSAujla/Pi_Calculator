import random
import sys
import math
import copy

again = "yes"
radius = 100
sample = 50
correctradius = False
correctsample = False
xyList = []
limit = 1
coordinate = []
storedcoords = []
validCoord = False
magnitude = 0
nCircle = 0
Pi = 0
Choice = "many"

#Statement explaining the program.
print("Monte Carlo approach to calculating Pi:")
print("Imagine a circle of radius 'r', inside a square box of length '2r'.")
print("We know the equations for working out the area of a square and a circle. \nTherefore we can take the ratio of the area of the circe and the area of the box. \nThen rearrange this for Pi to obtain:")
print("Pi = (4*A_(circle))/A_(box)")
print("To work out the area of the square and the box, we can use a simple method of counting the squares.")
print("Place the image we have of the square and circle onto a coordinate grid where the centre of the circle and square are at the origin.")
print("Then we can simply count how many squares are inside the circle and how many squares are inside the box. \n(we will assume each small square has an area of 1)")
print("The equation then becomes:")
print("Pi = (4*N_(circle))/N_(box)")
print("There is one problem, to get a more precise value of Pi, the radius of the circle and length of the square has to be really big. \n(to include more squares) \nOr the size of the small squares needs to decrease. \n(again, to include more squares, they both do the same thing)")
print("We will be increasing the size of the circle and square.")
print("If we increase the radius to a million, then it becomes taxing to count all the squares. \nSo a more statistical approach is taken where a small square is picked at random and is checked to see whether it is in the circle or not.")
print("The equation becomes:")
print("Pi = (4*n_(circle))/n_(total)")
print("n_(total) is the total number of squares being sampled as we restrict all sampled squares to be withiin the box.")

#Keeps the code looping for multiple tries.
while again == "yes":

    #Makes sure the values are integars.
    correctradius = False
    correctsample = False
    print("Would you like each square to be used only once if chosen, and then removed so it cannot be picked again?")
    print("Or allow squares to be used again if they are picked more than once?")
    Choice = input("(once/many) \n")
    print("Pick the radius and the number of samples you want to take. \n Make sure they are intergars.")
    while correctradius == False:
        radius = int(input("Radius = "))
        if type(radius) is int:
            correctradius = True
        else:
            print("Pick an integar, please.")
    while correctsample == False:
        sample = int(input("Sample size = "))
        if type(sample) is int:
            correctsample = True
        else:
            print("Pick an integar, please.")
    
    #Makes a list for x and y positions.
    xyList = list(range(-radius, radius+1))
    xyList.remove(0)
    
    if Choice == "once":
        #Makes sure sample size isnt larger than the area of the box.
        if sample > (4*(radius**(2))):
            print("The sample you have chosen is too large. It has been changed to", (radius**(2)))
            sample = radius**(2)

        #This picks a coordinate and checks it hasnt been used before.
        #Then works out whether the coordinate is within the circle or not.
        limit = 1
        nCircle = 0
        storedcoords = []
        while limit <= sample:
            validCoord = False
            while validCoord == False:
                coordinate = [random.choice(xyList), random.choice(xyList)]
                for i in range(len(storedcoords)):
                    if coordinate[0] == storedcoords[i][0] and coordinate[1] == storedcoords[i][1]:
                        break
                else:
                    storedcoords.append(copy.copy(coordinate))
                    validCoord = True
            magnitude = math.sqrt((coordinate[0]**(2)) + (coordinate[1]**(2)))
            if magnitude <= radius:
                nCircle += 1
            print(sample - limit)
            limit += 1
    else:
        #Picks a coordinate at random and sees whether it is within the circle.
        limit = 1
        nCircle = 0
        while limit <= sample:
            coordinate = [random.choice(xyList), random.choice(xyList)]
            magnitude = math.sqrt((coordinate[0]**(2)) + (coordinate[1]**(2)))
            if magnitude <= radius:
                nCircle = nCircle + 1
            print(sample - limit)
            limit = limit + 1
        

    #Now work out Pi.
    Pi = (4*nCircle)/sample
    print("This is the estimated value of Pi:\n", Pi)
    print("The actual value of Pi is:\n", math.pi)

    #Ask to go again.
    again = input("Would you like to go again? \n(yes/no) \n")
    
sys.exit