import pygame
from tile import tile
import FieldMaker


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
NULLCOLOR = (255, 255, 255)

background = (53,115,176)
game_board = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#playingSpace = tile(WHITE, width - (width / 4), height)
#playingSpace.rect.x = width/8
# grid = tile(RED, 5, 5)
# grid.rect.x = width/2
# grid.rect.y = height/2

print(FieldMaker.field)

for row in range(FieldMaker.field.shape[0]):
    for col in range(FieldMaker.field.shape[1]):
        currentTile = FieldMaker.field[row][col]
        if currentTile == -1:
            boardTile = tile(RED, 50, 50, "resources/images/tileMine.png")
        elif currentTile == 0:
            boardTile = tile(GRAY, 50, 50, "NONE")
        else:
            boardTile = tile(CYAN, 50, 50, "resources/images/tileFlag.png")
        boardTile.rect.x = width/6 + col * 60
        boardTile.rect.y = 20 + row * 75


        game_board.add(boardTile)
        all_sprites_list.add(boardTile)




#all_sprites_list.add(grid)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(pygame.mouse.get_pos())
            mouseX, mouseY = event.pos


           # for square in game_board:
            #    if square.rect.collidepoint(mouseX,mouseY):
              #      game_board.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_DOWN:
                for square in game_board:
                    square.rect.y += 5
                    if square.rect.y > height:
                        square.rect.y = 0
        #print(event)

    screen.fill(background)
    all_sprites_list.draw(screen)
    pygame.display.update()





pygame.quit()
