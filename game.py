import os, sys
import pygame

def main():
    pygame.init()
    maze = pygame.image.load(os.path.join('maps', 'maze1.png'))
    screen = pygame.display.set_mode((900, 900))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    player = pygame.image.load(os.path.join('sprites', 'player.png'))
    for y in range(30):
        for x in range(30):
            fill_color = maze.get_at((x, y))
            current_loc = (x * 30, y * 30)
            background.fill(fill_color, pygame.Rect(x * 30, y * 30, x * 30 + 29, y * 30 + 29))
            if fill_color.r == 0:
                if fill_color.g == 255:
                    background.blit(player, current_loc)
    #background.blit(maze, (150, 150))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    screen.blit(background, (0, 0))
    pygame.display.flip()

if __name__ == '__main__': main()
