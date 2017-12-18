# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
LAVENDER = (209, 145, 255)
DPINK = (96, 16, 49)
PURPLE = (103, 61, 165)
BEIGE = (239, 213, 170)
LBLUE = (24, 182, 206)
LGREEN = (122, 206, 57)
WBLUE = (208, 231, 239)
SKY = (113, 206, 237)



# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(SKY)
    

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    pygame.draw.arc(screen, BEIGE, [100, 100, 100, 100], 0, math.pi/2, 40)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
