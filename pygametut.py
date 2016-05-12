import pygame

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Slither')

gameExit = False
lead_x = 300
lead_y = 300
move_x, move_y = 0, 0

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x, move_y = -10, 0
            if event.key == pygame.K_RIGHT:
                move_x, move_y = 10, 0
            if event.key == pygame.K_UP:
                move_x, move_y = 0, -10
            if event.key == pygame.K_DOWN:
                move_x, move_y = 0, 10

    lead_x, lead_y = lead_x + move_x, lead_y + move_y

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])

    pygame.display.update()

pygame.quit()
quit()
