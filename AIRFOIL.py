"""
Created by Benny Chase
Made with a Raspberry Pi 3B+, screenshots may malfunction on other devices.
Screenshot should go to the folder the program is in.
You should have Python 3.5 or higher installed, and you must have Pygame.
I have set up my Github Repository so that it should install Python and Pygame.
If you experience any issues, bugs or you want to contribute, please post all
bugs in the 'issues' section of my repository. If you want to contribute, please
do! You are welcome to contribute by making yourself a contributer, or contact
me through Github (BennyThePythonCoder). This airfoil designer and simulator is
designed for beginners so they can get a basic understanding of airfoil.
Licensed under an MIT license, for more info, please look at the "LICENSE" file.
"""
# Imports
import pygame, sys, os, time, math
from pygame.locals import *

# Initiate everything
pygame.init()

winWidth = 1280
winHeight = 720

halfWinWidth = winWidth / 2
halfWinHeight = winHeight / 2

COORDINATES = []

CENTER = halfWinWidth, halfWinHeight

# Set colors
#         R    G    B
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
#########################

# Get input for values in equations

print("If you don't know what any of this means, please look at the diagram I have included in the folder. (airfoilDiagram.png)")

print("\n")

points = input("How many points should there be? (use 'x' for example): ")

print("\n")

print("If you don't know what the following prompts mean, please look at the variables (B, T, P, C, E, and R), and the other diagram (variablesDiagram.png)")

print("\n")

Bval = input("What is the base shape coefficient? (2 is recommended) (use 'x' for example): ")
Tval = input("What is the thickness value? (as fraction of chord), (0.1 is recommended) (use 'x' for example): ")
Pval = input("What is the taper exponent? (1 is recommended) (use 'x' for example): ")
Cval = input("What is the chamber value? (as fraction of chord), (0.05 is recommended) (use 'x' for example): ")
Eval = input("What is the chamber exponent? (1 is recommended) (use 'x' for example): ")
Rval = input("What is the reflex parameter? (positive = trailing edge, negative = flaps), (-0.005 to 0.005 is recommended) (use 'x' for example): ")

# ***Change the color value of 'AIRFOILCOLOR' to a custom color of the 'set colors' listed above (BLACK, WHITE...).***

AIRFOILCOLOR = BLUE

# Initiate Screen/Window
DISPLAYSURF = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Airfoil Model, press SPACE to take a picture')

# Background color
DISPLAYSURF.fill(WHITE)

# Get default values or entered values
if points == "x":
    pointsValue = 1000
else:
    pointsValue = points

if Bval == "x":
    B = 2
else:
    B = Bval

if Tval == "x":
    T = 0.1
else:
    T = Tval

if Pval == "x":
    P = 1
else:
    P = Pval

if Cval == "x":
    C = 0.05
else:
    C = Cval

if Eval == "x":
    E = 1
else:
    E = Eval

if Rval == "x":
    R = 0
else:
    R = Rval

# Equations
# defines pi
pi = 3.1415926535
# for every point
for i in range(1, int(pointsValue)):
    # gets x coordinate
    X = 0.5 + 0.5 * (abs(math.cos(i)) ** float(B)) / (math.cos(i))
    # gets y coordinate
    Y = (float(T) / 2) * ((abs(math.sin(i)) ** float(B)) / math.sin(i)) * (1 - X ** float(P)) + (float(C) * math.sin(X ** float(E) * pi) + float(R) * math.sin(X * 2 * pi))
    # adds X and Y cooordinates to COORDINATES list of points
    COORDINATES.append(((round(X*1000, 0) + 100, winHeight - round(Y*1000, 0) - 300)))

# tells you the coordinates
print("\n"+str(COORDINATES)+"\n")
# uses pygame to draw the airfoil
pygame.draw.polygon(DISPLAYSURF, AIRFOILCOLOR, (COORDINATES))

print("Done modeling!")

# Forever
while True:
    # Gets events
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_x or event.key == pygame.K_q:
                # Exits when you press 'x' or 'q'
                print("exiting...")
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE:
                # Captures Screenshot when space is pressed, works on Raspberry Pi 3B+
                os.system("scrot")
                print("Screenshot Captured!")
        # Exits when you press the 'X', close button for the window
        elif event.type == QUIT:
            print("exiting...")
            pygame.quit()
            sys.exit()
