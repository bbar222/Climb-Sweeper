import pygame
from square import square
pygame.init()
size = 700, 640
width, height = size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Climb Sweeper")

running = True
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (254, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
background = GRAY

all_sprites_list = pygame.sprite.Group()

#playingSpace = square(WHITE, width - (width / 4), height)
#playingSpace.rect.x = width/8
grid = square(WHITE, 50, 50)
grid.rect.x = width/2
grid.rect.y = height/2
all_sprites_list.add(grid)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
        #print(event)

    screen.fill(background)
    all_sprites_list.draw(screen)
    pygame.display.update()





pygame.quit()
