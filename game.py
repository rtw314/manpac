import os, sys
import pygame

def main():
    pygame.init()
    maze = pygame.image.load(os.path.join('maps', 'maze1.png'))
    screen = pygame.display.set_mode((300, 300))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    player = pygame.image.load(os.path.join('sprites', 'player_small.png'))
    for y in range(30):
        for x in range(30):
            fill_color = maze.get_at((x, y))
            current_loc = (x * 10, y * 10)
            background.fill(fill_color, pygame.Rect(x * 10, y * 10, x * 10 + 9, y * 10 + 9))
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
