# Imports
import pygame

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Moving Block"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#image
babe1 = pygame.image.load('Bikini Babe-1.png')
babe2 = pygame.image.load('Bikini Babe-2.png')
babe3 = pygame.image.load('Bikini Babe-3.png')
babe4 = pygame.image.load('Bikini Babe-4.png')
babe5 = pygame.image.load('Bikini Babe-5.png')
babe6 = pygame.image.load('Bikini Babe-6.png')
babe7 = pygame.image.load('Bikini Babe-7.png')
babe8 = pygame.image.load('Bikini Babe-8.png')
babe9 = pygame.image.load('Bikini Babe-9.png')

bikini_babe = [babe1, babe2, babe3, babe4, babe5, babe6, babe7, babe8, babe9]

# Block
loc = [380, 280]
vel = [0, 0]
speed = 8

def George(loc, frame):
    x = loc[0]
    y = loc[1]
    
    screen.blit(bikini_babe[frame], (x, y))


    
    
# Game loop
done = False

ticks = 0
frame = 0

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel[0] = speed
            elif event.key == pygame.K_LEFT:
                vel[0] = -speed
            elif event.key == pygame.K_DOWN:
                vel[1] = speed
            elif event.key == pygame.K_UP:
                vel[1] = -speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel[0] = 0
            elif event.key == pygame.K_LEFT:
                vel[0] = 0
            elif event.key == pygame.K_DOWN:
                vel[1] = 0
            elif event.key == pygame.K_UP:
                vel[1] = 0

                
    # Game logic
    loc[0] += vel[0]
    loc[1] += vel[1]

    ticks += 1
    if ticks%50 == 0:
        frame += 1
        if frame > 8:
            frame = 0
    # Drawing code
    screen.fill(BLACK)
    George(loc, frame)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
