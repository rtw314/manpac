import os, sys
import pygame

def main():
    pygame.init()
    maze = pygame.image.load(os.path.join('maps', 'maze1.jpg'))
    screen = pygame.display.set_mode((900, 900))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    for y in range(30):
        for x in range(30):
            background.fill(maze.get_at((x, y)), pygame.Rect(x * 30, y * 30, x * 30 + 29, y * 30 + 29))
    background.blit(maze, (150, 150))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    screen.blit(background, (0, 0))
    pygame.display.flip()

if __name__ == '__main__': main()
