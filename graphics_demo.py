# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Calm Day at Capsule corp."
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


def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])
    
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(SKY)

    #building shape(make a black outline)
    pygame.draw.ellipse(screen, BEIGE, [100, 300, 600, 700])
    #grass
    pygame.draw.rect(screen, LGREEN, [0, 470, 800, 800])
    #building chimeney(make black circle outline and then cover some in beige circle to make roundness)
    pygame.draw.rect(screen, BEIGE, [230, 300, 80, 120])
    pygame.draw.rect(screen, BEIGE, [460, 250, 80, 120])
    #clouds
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(650, 100)
    #palm tree recipie~~~~~~~~~~~~~~~~~~
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
