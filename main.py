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


# Text display stuff
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(score), True, BLACK)
textRect = text.get_rect()



background = (53,115,176)
game_board = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#playingSpace = tile(WHITE, width - (width / 4), height)
#playingSpace.rect.x = width/8
# grid = tile(RED, 5, 5)
# grid.rect.x = width/2
# grid.rect.y = height/2







print(FieldMaker.field)
numTiles = 0
for row in range(8):
    for col in range(FieldMaker.field.shape[1]):
        currentTile = FieldMaker.field[row][col]
        if 0 <= numTiles < 16:
            startRevealed = True
        else:
            startRevealed = False
        if currentTile == -1 and 0 <= numTiles < 16:
            boardTile = tile(RED, "resources/images/tileMine.png", not startRevealed, row, col)
        elif currentTile == -1:
            boardTile = tile(RED, "resources/images/tileMine.png", startRevealed, row, col)
        elif currentTile == 0:
            boardTile = tile(GRAY, "resources/images/tileEmpty.png", startRevealed, row, col)
        elif currentTile == 1:
            boardTile = tile(BLACK, "resources/images/tileOne.png", startRevealed, row, col)
        elif currentTile == 2:
            boardTile = tile(BROWN, "resources/images/tileTwo.png", startRevealed, row, col)
        elif currentTile == 3:
            boardTile = tile(YELLOW, "resources/images/tileThree.png", startRevealed, row, col)
        elif currentTile == 4:
            boardTile = tile(GREEN, "resources/images/tileFour.png", startRevealed, row, col)
        elif currentTile == 5:
            boardTile = tile(BLUE, "resources/images/tileFive.png", startRevealed, row, col)
        elif currentTile == 6:
            boardTile = tile(PURPLE, "resources/images/tileSix.png", startRevealed, row, col)
        elif currentTile == 7:
            boardTile = tile(CYAN, "resources/images/tileSeven.png", startRevealed, row, col)
        elif currentTile == 8:
            boardTile = tile(MAGENTA, "resources/images/tileEight.png", startRevealed, row, col)
        else:
            boardTile = tile(ORANGE, "resources/images/tileFlag.png", startRevealed, row, col)
        boardTile.rect.x = width/6 + col * 60
        boardTile.rect.y = height - row * 80 - 130

        numTiles += 1
        game_board.add(boardTile)
        all_sprites_list.add(boardTile)




#all_sprites_list.add(grid)
clock = pygame.time.Clock()
difficulty = 10
while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                for square in game_board:
                    square.rect.y += 10
                    if square.rect.y > height:
                        square.rect.y = 0

    #tileLeaveEvent = pygame.event.Event(pygame.USEREVENT, myID=TILE_LEAVE)
# Reserves a pygame.USEREVENT for a custom use.
# If too many events are made a pygame.errorstandard pygame exception is raised.
    for square in game_board:
        square.rect.y += 1
        if square.rect.y > height:
            #event_list.append(tileLeaveEvent)
            game_board.remove(square)
            if square.kill() == "dead":
                print("YOU ARE DEAD")
                running = False
            else:
                score += square.kill()

            # square.rect.y = 0


    screen.fill(background)
    # Display score

    text = font.render(str(score), True, BLACK)
    screen.blit(text,textRect)
    #
    game_board.update(event_list)
    all_sprites_list.draw(screen)
    pygame.display.update()


    clock.tick(difficulty)




pygame.quit()
