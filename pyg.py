import pygame
import sys
import random

# Constants
MAXTRIES = 14
WIDTH = 600
HEIGHT = 800
COLOURS = {0:"red", 1:"green", 2:"blue", 3:"yellow", 4:"purple", 5:"orange", 6:"pink", 7:"brown", 8:"black", 9:"white"}
 

# Variables
toBeGuessed = []
BASEcontrol = ["grey70", "grey70", "grey70", "grey70", "grey70"]
control = ["grey70", "grey70", "grey70", "grey70", "grey70"]
BASEguess = ["grey70", "grey70", "grey70", "grey70", "grey70"]
currentGuess = ["grey70", "grey70", "grey70", "grey70", "grey70"]
MADEguesses = []
MADEcontrols = []
columns = 0
for i in COLOURS:
    columns += 1
columns += 8 # | | x | x | x | x | x || 8  8  8  8  8 | 
usedTries = 1 # base value = 1, else column management issues, => 11 means 10 tries, which is max!
colour = None


# Functions
def getCurrectGuess():
    guess = input("Enter num: ")
    guesses = []
    for i in guess:
        guesses.append(int(i))
    return guesses

def checkGuess():
    global control
    global currentGuess
    global toBeGuessed
    global MADEcontrols

    for i in range(len(currentGuess)):
        if currentGuess[i] == toBeGuessed[i]:
            control[i] = "red"
        elif currentGuess[i] in toBeGuessed and currentGuess[i] != toBeGuessed[i]:
            control[i] = "yellow"
        else:
            control[i] = "grey70"
            
    print(control)
    MADEcontrols.append(control.copy())

def colourPick(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            for i in range(len(COLOURS)):
                if i < 5:
                    if event.pos[0] > i*WIDTH/len(COLOURS)+160 and event.pos[0] < i*WIDTH/len(COLOURS)+200 and event.pos[1] > HEIGHT-140 and event.pos[1] < HEIGHT-100:
                        return i
                elif i >= 5:
                    if event.pos[0] > (i-5)*WIDTH/len(COLOURS)+160 and event.pos[0] < (i-5)*WIDTH/len(COLOURS)+200 and event.pos[1] > HEIGHT-80 and event.pos[1] < HEIGHT-40:
                        return i
    return None

def getMousePos():
    return pygame.mouse.get_pos()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")
clock = pygame.time.Clock()

# Generate random numbers
for i in range(5):
    rn = random.randint(0, len(COLOURS)-1)
    for j in COLOURS:
        if rn == j:
            toBeGuessed.append(COLOURS[j])
        #
print(toBeGuessed)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            gap = 20
            if getMousePos()[1] > HEIGHT-195:
                colour = colourPick(event)
            if getMousePos()[1] > HEIGHT-270-gap and getMousePos()[1] < HEIGHT-230+gap and colour != None:
                if getMousePos()[0] > 40-gap and getMousePos()[0] < 80+gap:
                    currentGuess[0] = COLOURS[colour]
                elif getMousePos()[0] > 160-gap and getMousePos()[0] < 200+gap:
                    currentGuess[1] = COLOURS[colour]
                elif getMousePos()[0] > 280-gap and getMousePos()[0] < 320+gap:
                    currentGuess[2] = COLOURS[colour]
                elif getMousePos()[0] > 400-gap and getMousePos()[0] < 420+gap:
                    currentGuess[3] = COLOURS[colour]
                elif getMousePos()[0] > 520-gap and getMousePos()[0] < 560+gap:
                    currentGuess[4] = COLOURS[colour]
            if getMousePos()[1] > 660 and getMousePos()[1] < 730 and getMousePos()[0] > 25 and getMousePos()[0] < 95:
                MADEguesses.append(currentGuess.copy())
                usedTries += 1
                if usedTries < MAXTRIES:
                    checkGuess()
    
    screen.fill("grey40")
    
    for j in range(columns+1):
        currentColumn = i*WIDTH//(columns+1)
        columnWidth = WIDTH//(columns+1)
        pygame.draw.line(screen, "black", (j*WIDTH/(columns+1), 0), (j*WIDTH/(columns+1), HEIGHT))

    if len(MADEguesses) > 0:
        for i in range(len(MADEguesses)):
            for j in range(columns+1):
                currentColumn = i*WIDTH//(columns+1)
                columnWidth = WIDTH//(columns+1)
                if j == 3:
                    index = 0
                    pygame.draw.circle(screen, MADEguesses[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                if j == 5:
                    index = 1
                    pygame.draw.circle(screen, MADEguesses[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                if j == 7:
                    index = 2
                    pygame.draw.circle(screen, MADEguesses[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                if j == 9:
                    index = 3
                    pygame.draw.circle(screen, MADEguesses[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                if j == 11:
                    index = 4
                    pygame.draw.circle(screen, MADEguesses[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                
    if len(MADEcontrols) > 0:
        for i in range(len(MADEcontrols)):
            for j in range(columns+1):
                currentColumn = i*WIDTH//(columns+1)
                columnWidth = WIDTH//(columns+1)
                if j == 14:
                    index = 0
                    pygame.draw.circle(screen, MADEcontrols[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                if j == 15:
                    index = 1
                    pygame.draw.circle(screen, MADEcontrols[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                if j == 16:
                    index = 2
                    pygame.draw.circle(screen, MADEcontrols[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                if j == 17:
                    index = 3
                    pygame.draw.circle(screen, MADEcontrols[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
                if j == 18:
                    index = 4
                    pygame.draw.circle(screen, MADEcontrols[i][index], (j*WIDTH//(columns+1)-15, i*42+20), 15)
    
    #Create a window for getting input
    pygame.draw.rect(screen, "grey10", (0, HEIGHT-300, WIDTH, HEIGHT))
    for i in range(len(toBeGuessed)+1):
        pygame.draw.circle(screen, "grey70", (i*WIDTH/5+60, HEIGHT-250), 20)

    for i in COLOURS:
        if i < 5:
            pygame.draw.circle(screen, COLOURS[i], (i*WIDTH/len(COLOURS)+180, HEIGHT-120), 20)
        elif i >= 5:
            pygame.draw.circle(screen, COLOURS[i], ((i-5)*WIDTH/len(COLOURS)+180, HEIGHT-60), 20)
    
    if colour != None:
        pygame.draw.circle(screen, COLOURS[colour], (getMousePos()[0], getMousePos()[1]), 20)
    for i in range(5):
        pygame.draw.circle(screen, currentGuess[i], (i*WIDTH/5+60, HEIGHT-250), 20)

    #box
    pygame.draw.rect(screen, "white", (25, 660, 70, 70))


    if control == ["red", "red", "red", "red", "red"]:
        #make me some super duper animation for winning
        pass


    clock.tick(60)
    pygame.display.flip()
