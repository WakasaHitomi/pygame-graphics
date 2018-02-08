# Computer Programming 1
# Unit 11 - Graphics
#
# A stormy day


# Imports
import pygame
import random


# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Rainy Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (100, 125, 75)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (200, 200, 100)
BLACK = (0, 0, 0)


def draw_cloud(loc, color):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])

def draw_raindrop(drop):
    rect = drop[:4]
    pygame.draw.ellipse(screen, DARK_BLUE, rect)

''' Make clouds '''
num_clouds = 8
near_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 100)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 16
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)

''' Make rain '''
num_drops = 700
rain = []

for i in range(num_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(1, 5)
    stop = random.randrange(400, 700)
    drop = [x, y, r, r, stop]
    rain.append(drop)

# Lightning stuff
lightning_prob = 300 # (higher is less frequent)
lightning_timer = 0

# Sound Effects
pygame.mixer.music.load("creepy/humming.ogg")
thunder = pygame.mixer.Sound("creepy/thunder.ogg")

#image
babe1 = pygame.image.load('Bikini Babe-1.png')
babe2 = pygame.image.load('Bikini Babe-2.png')
babe3 = pygame.image.load('Bikini Babe-3.png')
babe4 = pygame.image.load('Bikini Babe-4.png')
babe5 = pygame.image.load('Bikini Babe-5.png')
babe6 = pygame.image.load('Bikini Babe-6.png')

bikini_babe = [babe1, babe2, babe3, babe4, babe5, babe6]

# Block
loc = [380, 280]
vel = [0, 0]
speed = 8

def George(loc, frame):
    x = loc[0]
    y = loc[1]
    
    screen.blit(bikini_babe[frame], (x, y))

# Game loop
pygame.mixer.music.play(-1)

daytime = True
lights_on = False

done = False

ticks = 0
frame = 0

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on

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
    if ticks%20 == 0:
        frame += 1
        if frame > 5:
            frame = 0

             # google 'pygame key constants' for more keys
    # Game logic
    ''' move clouds '''
    for c in far_clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    for c in near_clouds:
        c[0] -= 2

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    ''' set sky color '''
    if daytime:
        sky = GRAY
    else:
        sky = BLACK

    ''' set window color (if there was a house)'''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE
        


    ''' move rain '''
    for r in rain:
        r[0] -= 1
        r[1] += 4

        if r[1] > r[4]:
            r[0] = random.randrange(0, 1000)
            r[1] = random.randrange(-100, 0)

    ''' flash lighting '''
    if random.randrange(0, 300) == 0:
        lightning_timer = 5
        thunder.play()
    else:
        lightning_timer -= 1
    
    # Drawing code
    ''' sky '''
    if lightning_timer > 0:
        screen.fill(YELLOW)
    else:
        screen.fill(sky)

    ''' sun '''
    #pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' clouds '''
    for c in far_clouds:
        draw_cloud(c, NOT_QUITE_DARK_GRAY)

    ''' rain ''' 
    for r in rain:
        draw_raindrop(r)

    ''' clouds '''
    for c in near_clouds:
        draw_cloud(c, DARK_GRAY)

    George(loc, frame)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()