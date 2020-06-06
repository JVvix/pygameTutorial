# Youtube PyGame Tutorial

import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First Game")

img = pygame.image.load()

walkRight = [img('R1.png'), img('R2.png'),img('R3.png'),img('R4.png'),img('R5.png'),img('R6.png'),img('R7.png'),img('R8.png'),img('R9.png')]
walkLeft = [img('L1.png'), img('L2.png'),img('L3.png'),img('L4.png'),img('L5.png'),img('L6.png'),img('L7.png'),img('L8.png'),img('L9.png')]
bg = img('bg.png')
char = img('standing.png')

x = 50
y = 440 
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def reddrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0 

    if left:
        win.blit(walkLeft[walkCount])
    pygame.display.update()

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_d] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10 and y > vel:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    if keys[pygame.K_q]:
       event.type = pygame.QUIT
    redrawGameWindow

pygame.quit() 
