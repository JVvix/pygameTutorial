# Youtube PyGame Tutorial

import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First Game")

x = 50
y = 440 
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pygame.K_a] and x > vel:
        x -= vel
    if keys[pygame.K_d] and x < 500 - width - vel:
        x += vel
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
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

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit() 