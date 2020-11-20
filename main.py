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
PURPLE = (160,32,240)
ORANGE = (255, 165, 0)
BROWN = (150,75,0)



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
            boardTile = tile(RED, "resources/images/tileMine.png", False)
        elif currentTile == 0:
            boardTile = tile(GRAY, "resources/images/tileEmpty.png", False)
        elif currentTile == 1:
            boardTile = tile(BLACK, "resources/images/tileOne.png", False)
        elif currentTile == 2:
            boardTile = tile(BROWN, "resources/images/tileTwo.png", False)
        elif currentTile == 3:
            boardTile = tile(YELLOW, "resources/images/tileThree.png", False)
        elif currentTile == 4:
            boardTile = tile(GREEN, "resources/images/tileFour.png", False)
        elif currentTile == 5:
            boardTile = tile(BLUE, "resources/images/tileFive.png", False)
        elif currentTile == 6:
            boardTile = tile(PURPLE, "resources/images/tileSix.png", False)
        elif currentTile == 7:
            boardTile = tile(CYAN, "resources/images/tileSeven.png", False)
        elif currentTile == 8:
            boardTile = tile(MAGENTA, "resources/images/tileEight.png", False)
        else:
            boardTile = tile(ORANGE, "resources/images/tileFlag.png", False)
        boardTile.rect.x = width/6 + col * 60
        boardTile.rect.y = 20 + row * 75


        game_board.add(boardTile)
        all_sprites_list.add(boardTile)




#all_sprites_list.add(grid)

while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_DOWN:
                for square in game_board:
                    square.rect.y += 5
                    if square.rect.y > height:
                        square.rect.y = 0
        #print(event)
    game_board.update(event_list)
    screen.fill(background)
    all_sprites_list.draw(screen)
    pygame.display.update()





pygame.quit()
