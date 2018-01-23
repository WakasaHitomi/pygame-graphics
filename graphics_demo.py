# Imports
import random
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
DGREEN = (39, 114, 4)
YELLOW = (224, 213, 11)
BROWN = (135, 80, 13)


def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def flower(x, y):
    pygame.draw.rect(screen, DGREEN, [x, y, 3, 14])
    pygame.draw.ellipse(screen, YELLOW, [x - 4, y - 10, 13, 13])
    pygame.draw.ellipse(screen, LAVENDER, [x - 10, y - 8, 12, 8])
    pygame.draw.ellipse(screen, BLACK, [x - 10, y - 8, 12, 8], 1)
    pygame.draw.ellipse(screen, DPINK, [x - 3, y - 16, 8, 12])
    pygame.draw.ellipse(screen, LAVENDER, [x + 4, y - 8, 12, 8])
    pygame.draw.ellipse(screen, BLACK, [x + 4, y - 8, 12, 8], 1)
    pygame.draw.ellipse(screen, YELLOW, [x - 4, y - 10, 13, 13])
    
def tree(x, y):
    pygame.draw.rect(screen, BROWN, [x, y, 10, 80])
    pygame.draw.ellipse(screen, BROWN, [x - 1, y + 70, 13, 13])
    pygame.draw.ellipse(screen, DGREEN, [x - 8, y - 2 , 28, 20])
    pygame.draw.ellipse(screen, BLACK, [x - 8, y - 2 , 28, 20], 1)
    pygame.draw.ellipse(screen, DGREEN, [x - 18, y - 3 , 18, 15])
    pygame.draw.ellipse(screen, BLACK, [x - 18, y - 3 , 18, 15], 1)
    pygame.draw.ellipse(screen, DGREEN, [x + 15, y - 3 , 18, 15])
    pygame.draw.ellipse(screen, BLACK, [x + 15, y - 3 , 18, 15], 1)
    pygame.draw.ellipse(screen, DGREEN, [x - 8, y - 15 , 20, 20])
    pygame.draw.ellipse(screen, BLACK, [x - 8, y - 15 , 20, 20], 1)
    pygame.draw.ellipse(screen, DGREEN, [x + 1, y - 25 , 23, 25])
    pygame.draw.ellipse(screen, BLACK, [x + 1, y - 25 , 23, 25], 1)
    pygame.draw.ellipse(screen, DGREEN, [x + 5, y - 10 , 20, 20])
    pygame.draw.ellipse(screen, BLACK, [x + 5, y - 10 , 20, 20], 1)
    pygame.draw.ellipse(screen, DGREEN, [x - 2, y - 10 , 20, 20])

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(SKY)


    #back chimney
    pygame.draw.ellipse(screen, WHITE, [230, 265, 80, 65])
    pygame.draw.ellipse(screen, BLACK, [230, 265, 80, 65], 2)
    pygame.draw.rect(screen, BEIGE, [230, 300, 80, 120])
    pygame.draw.rect(screen, BLACK, [230, 300, 80, 120], 2)
    #WINDOWS
    pygame.draw.rect(screen, LBLUE, [232, 320, 45, 8])
    pygame.draw.rect(screen, LBLUE, [238, 343, 45, 8])
    
    #building shape(make a black outline)
    pygame.draw.ellipse(screen, BEIGE, [100, 300, 600, 700])
    pygame.draw.ellipse(screen, BLACK, [100, 300, 600, 700], 3)
    #grass
    pygame.draw.rect(screen, LGREEN, [0, 470, 800, 800])
    #building chimeney(make black circle outline and then cover some in beige circle to make roundness)
    pygame.draw.ellipse(screen, WHITE, [460, 220, 80, 65])
    pygame.draw.ellipse(screen, BLACK, [460, 220, 80, 65], 2)
    
    pygame.draw.ellipse(screen, BLACK, [460, 320, 81, 50], 1)
    pygame.draw.rect(screen, BEIGE, [460, 250, 80, 95])
    pygame.draw.rect(screen, BLACK, [460, 250, 80, 95], 2)
    pygame.draw.rect(screen, BEIGE, [462, 344, 78, 3])
    #sunshine lines
    pygame.draw.line(screen, YELLOW, [30, 10], [200,320], 8)
    # front door
    pygame.draw.rect(screen, LBLUE, [420, 435, 20, 35])
    pygame.draw.rect(screen, BLACK, [420, 435, 20, 35], 1)
    pygame.draw.rect(screen, LBLUE, [400, 435, 20, 35])
    pygame.draw.rect(screen, BLACK, [400, 435, 20, 35], 1)
    #clouds
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(650, 100)
    #flower behin the fence
    flower(6, 495)
    flower(55, 495)

    #fence
    y = 480
    for x in range(5, 800, 30):
        post = [x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]
        pygame.draw.polygon(screen, WHITE, post)

    
    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])


    #flower
    flower(104, 540)
    flower(32, 568)
    flower(10, 587)
    flower(75, 600)
    flower(37, 700)
    flower(55, 676)
    flower(84, 508)
    
    #tree
    tree(654, 510)
    tree(700, 484)
    tree(40, 490)
    tree(756, 500)

    
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
