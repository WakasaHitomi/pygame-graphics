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

tor1 = pygame.image.load('Tornado!!!!-1.png')
tor2 = pygame.image.load('Tornado!!!!-2.png')
tor3 = pygame.image.load('Tornado!!!!-3.png')
tor4 = pygame.image.load('Tornado!!!!-4.png')
tor5 = pygame.image.load('Tornado!!!!-5.png')
tor6 = pygame.image.load('Tornado!!!!-6.png')
tor7 = pygame.image.load('Tornado!!!!-7.png')
tor8 = pygame.image.load('Tornado!!!!-8.png')

tornado = [tor1, tor2, tor3, tor4, tor5, tor6, tor7, tor8]


sun = pygame.image.load('sun.png')
moon = pygame.image.load('moon.png')

cat = pygame.image.load('maze cat-1.png')


# Block
place = [380, 280]
vel = [0, 0]
speed = 8

def George(place, frame):
    x = place[0]
    y = place[1]
    
    screen.blit(bikini_babe[frame], (x, y))

place1 = [200, 280]
vel1 = [0, 0]
speed = 12

def kitty(place1):
    x = place1[0]
    y = place1[1]

    screen.blit(cat, (x, y))



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

def dusty_gusty_boi(cord, frames):
    x = cord[0]
    y = cord[1]

    screen.blit(tornado[frames], (x, y))

    
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

num_tornadoes = 10
tornadoess = []

for i in range(num_tornadoes):
    x = random.randrange(-50, 1600)
    y = random.randrange(-50, 50)
    cord = [x, y]
    tornadoess.append(cord)
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
droplet = pygame.mixer.Sound("creepy/droplet.ogg")



# Game loop
pygame.mixer.music.play(-1)

daytime = True
lights_on = False

done = False

tick = 0
frames = 0

ticks = 0
frame = 0

while not done:
    # Event processing


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            

    pressed = pygame.key.get_pressed()

    day = pressed[pygame.K_TAB]
    night = pressed[pygame.K_q]
    sunn = pressed[pygame.K_n]
    moonn = pressed[pygame.K_m]

    
    water = pressed[pygame.K_SPACE]
    
    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    up1 = pressed[pygame.K_w]
    down1 = pressed[pygame.K_s]
    left1 = pressed[pygame.K_a]
    right1 = pressed[pygame.K_d]


    if left:
        vel[0] = -speed
    elif right:
        vel[0] = speed
    else:
        vel[0] = 0
    
    
    if left:
        vel[0] = -speed
    elif right:
        vel[0] = speed
        
    else:
        vel[0] = 0

    
    if up:
        vel[1] = -speed
    elif down:
        vel[1] = speed
    else:
        vel[1] = 0


    if left1:
        vel1[0] = -speed
    elif right:
        vel1[0] = speed
    else:
        vel1[0] = 0
    
    
    if left1:
        vel1[0] = -speed
    elif right1:
        vel1[0] = speed
        
    else:
        vel1[0] = 0

    
    if up1:
        vel1[1] = -speed
    elif down1:
        vel1[1] = speed
    else:
        vel1[1] = 0


        

    if water:
        droplet.play()

    if day:
        daytime = True

    if night:
        daytime = False
    
                
    # Game logic
    place[0] += vel[0]
    place[1] += vel[1]

    place1[0] += vel1[0]
    place1[1] += vel1[1]

    tick += 1
    if tick%30 == 0:
        frames += 1
        if frames > 7:
            frames = 0


    ticks += 1
    if ticks%30 == 0:
        frame += 1
        if frame > 8:
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

    for t in tornadoess:
        t[0] += 4

        if t[0] > 890:
            t[0] = random.randrange(-50, 1600)
            t[1] = random.randrange(-50, 200)

            

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

    '''nado'''
    for t in tornadoess:
        screen.blit(tornado[frames], (x, y))

    if sunn:
        screen.blit(sun, (-20, -10))

    if moonn:
        screen.blit(moon, (500, -380))


    font = pygame.font.Font(None, 48)
    text = font.render("She Stood Alone...", 3, WHITE)
    screen.blit(text, [350, 100])
    

    George(place, frame)
    kitty(place1)
    dusty_gusty_boi(cord, frames)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
