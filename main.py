import pygame
from tile import tile
import FieldMaker

pygame.init()
fxLineClear = pygame.mixer.Sound("resources/sounds/tilesRemoved.wav")
fxMineClicked = pygame.mixer.Sound("resources/sounds/mineClicked.wav")
fxTileClear = pygame.mixer.Sound("resources/sounds/tileCleared.wav")
fxFlagPlaced = pygame.mixer.Sound("resources/sounds/flagPlaced.wav")
fxStartGame = pygame.mixer.Sound("resources/sounds/recycle.wav")

fxLineClear.set_volume(.1)
fxMineClicked.set_volume(.1)
fxTileClear.set_volume(.1)
fxFlagPlaced.set_volume(.1)
fxStartGame.set_volume(.2)



size = 700, 640
width, height = size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Climb Sweeper")

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

just_removed = pygame.sprite.Group()
orderOfRemoved = []

ROWSIZE = 100


def titleLoop():
    running = True
    FieldMaker.newBoard(ROWSIZE)
    numTiles = 0
    all_sprites_list.empty()
    game_board.empty()
    just_removed.empty()

    # Creates mine field


    print(FieldMaker.field)
    for row in range(ROWSIZE):
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
            boardTile.rect.x = width / 6 + col * 60
            boardTile.rect.y = height - row * 80 - 130

            numTiles += 1
            game_board.add(boardTile)
            all_sprites_list.add(boardTile)

    font = pygame.font.Font('freesansbold.ttf', 50)
    titleText = font.render("CLIMB-SWEEPER", True, BLACK)
    titleTextRect = titleText.get_rect()
    titleTextRect.center = (width / 2, height / 5)


    startText = font.render("START", True, ORANGE)
    startTextRect = startText.get_rect()
    startTextRect.center = (width / 2, height / 2)

    startButton = pygame.Surface((250, 75), pygame.SRCALPHA)
    startButtonRect = startButton.get_rect()
    startButtonRect.center = (width/2, height/2)


    exitText = font.render("EXIT", True, ORANGE)
    exitTextRect = exitText.get_rect()
    exitTextRect.center = (width / 2, height / 1.5)

    exitButton = pygame.Surface((250, 75), pygame.SRCALPHA)
    exitButtonRect = exitButton.get_rect()
    exitButtonRect.center = (width/2, height / 1.5)

    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startButtonRect.collidepoint(event.pos):
                    fxStartGame.play()
                    running = False
                elif exitButtonRect.collidepoint(event.pos):
                    pygame.quit()

        screen.fill(background)

        screen.blit(titleText, titleTextRect)

        pygame.draw.rect(screen, BLACK, startButtonRect, 10, 10)
        screen.blit(startText, startTextRect)

        pygame.draw.rect(screen, BLACK, exitButtonRect, 10, 10)
        screen.blit(exitText, exitTextRect)

        pygame.display.update()




def gameLoop(difficulty):

    running = True
    selfKill = False
    # Text display stuff
    score = 0
    font = pygame.font.Font('freesansbold.ttf', 26)
    text = font.render(str(score), True, BLACK)
    textRect = text.get_rect()
    textRect.center = (15,25)
    clock = pygame.time.Clock()
    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.USEREVENT:
                # If mine is clicked event
                if event.myID == 1:
                    fxMineClicked.play()
                    print("You clicked on a mine!")
                    selfKill = True
                    running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    for square in game_board:
                        square.rect.y += 10
                        if square.rect.y > height:
                            square.rect.y = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for square in game_board:
                    if square.rect.collidepoint(event.pos):
                        fxTileClear.play()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for square in game_board:
                    if square.rect.collidepoint(event.pos):
                        fxFlagPlaced.play()



        for square in game_board:
            square.rect.y += 1
            if square.rect.y > height:
                if square.kill() == "dead":
                    fxMineClicked.play()
                    print("YOU ARE DEAD")
                    running = False
                    game_board.remove(square)
                    all_sprites_list.remove(square)
                    just_removed.add(square)
                    orderOfRemoved.append(square)
                    if len(just_removed) > 7:
                        for i in range(8):
                            just_removed.remove(orderOfRemoved[0])
                            orderOfRemoved.remove(orderOfRemoved[0])
                    break

                else:
                    score += square.kill()
                    fxLineClear.play()
                    game_board.remove(square)
                    all_sprites_list.remove(square)
                    just_removed.add(square)
                    orderOfRemoved.append(square)

                    # keeps track of the last 8 tiles so that they may be displayed again when the player loses
                    if len(just_removed) > 7:
                        for i in range(8):
                            just_removed.remove(orderOfRemoved[0])
                            orderOfRemoved.remove(orderOfRemoved[0])



                # print(len(just_removed))
                # square.rect.y = 0



        screen.fill(background)
        # Display score

        text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(text,textRect)
        #
        game_board.update(event_list)
        all_sprites_list.draw(screen)
        just_removed.draw(screen)
        pygame.display.update()


        clock.tick(difficulty)

    print(len(just_removed))
    if not selfKill:
        for _ in range(55):
            for square in just_removed:
                square.rect.y -= 1
            for square in all_sprites_list:
                square.rect.y -= 1
            screen.fill(background)
            all_sprites_list.draw(screen)
            just_removed.draw(screen)
            pygame.display.update()



def deadOverlay():
    running = True
    font = pygame.font.Font('freesansbold.ttf', 25)
    returnText = font.render("Menu", True, BLACK)
    returnTextRect = returnText.get_rect()
    returnTextRect.center = (60, height - 50)


    returnButton = pygame.Surface((100, 50), pygame.SRCALPHA)
    returnButtonRect = returnButton.get_rect()
    returnButtonRect.center = (60, height - 50)

    pygame.draw.rect(screen, BLACK, returnButtonRect, 5, 10)
    screen.blit(returnText, returnTextRect)

    pygame.display.update()

    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if returnButtonRect.collidepoint(event.pos):
                    running = False
            elif event.type == pygame.QUIT:
                pygame.quit()




        pygame.display.update()


while True:
    titleLoop()
    gameLoop(difficulty=10)
    deadOverlay()
