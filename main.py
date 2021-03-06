import pygame
from tile import tile
import FieldMaker

# Sounds are remixed from windows 10 alert sounds
pygame.init()
fxLineClear = pygame.mixer.Sound("resources/sounds/tilesRemoved.wav")
fxMineClicked = pygame.mixer.Sound("resources/sounds/mineClicked.wav")
fxTileClear = pygame.mixer.Sound("resources/sounds/tileCleared.wav")
fxFlagPlaced = pygame.mixer.Sound("resources/sounds/flagPlaced.wav")
fxStartGame = pygame.mixer.Sound("resources/sounds/recycle.wav")

fxLineClear.set_volume(1)
fxMineClicked.set_volume(.1)
fxTileClear.set_volume(.1)
fxFlagPlaced.set_volume(.1)
fxStartGame.set_volume(.2)

fontStyle = 'freesansbold.ttf'

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
LIGHTBLUE = (0,128,255)

background = (53,115,176)
game_board = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
visibleSquares = pygame.sprite.Group()

just_removed = pygame.sprite.Group()

ROWSIZE = 8192

# sets saved highscore
global userHighScore
highScoreFile = open("highscore.txt", "r")
savedScore = highScoreFile.readline()
highScoreFile.close()


if savedScore == "":
    highScoreFile = open("highscore.txt", "w")
    highScoreFile.write("0")
    highScoreFile.close()
    userHighScore = 0
else:
    userHighScore = savedScore


def printBoard(numTiles, currentRow):
    row = currentRow
    for col in range(8):
        currentTile = FieldMaker.field[row][col]
        if 0 <= numTiles < 16:
            startRevealed = True
        else:
            startRevealed = False
        if currentTile == -1 and 0 <= numTiles < 16:
            boardTile = tile(RED, "resources/images/tileMine - transp.png", not startRevealed, row, col)
        elif currentTile == -1:
            boardTile = tile(RED, "resources/images/tileMine - transp.png", startRevealed, row, col)
        elif currentTile == 0:
            boardTile = tile(GRAY, "resources/images/tileEmpty - transp.png", startRevealed, row, col)
        elif currentTile == 1:
            boardTile = tile(LIGHTBLUE, "resources/images/tileOne - transp.png", startRevealed, row, col)
        elif currentTile == 2:
            boardTile = tile(BROWN, "resources/images/tileTwo - transp.png", startRevealed, row, col)
        elif currentTile == 3:
            boardTile = tile(YELLOW, "resources/images/tileThree - transp.png", startRevealed, row, col)
        elif currentTile == 4:
            boardTile = tile(GREEN, "resources/images/tileFour - transp.png", startRevealed, row, col)
        elif currentTile == 5:
            boardTile = tile(BLUE, "resources/images/tileFive - transp.png", startRevealed, row, col)
        elif currentTile == 6:
            boardTile = tile(PURPLE, "resources/images/tileSix - transp.png", startRevealed, row, col)
        elif currentTile == 7:
            boardTile = tile(CYAN, "resources/images/tileSeven - transp.png", startRevealed, row, col)
        elif currentTile == 8:
            boardTile = tile(MAGENTA, "resources/images/tileEight - transp.png", startRevealed, row, col)
        else:
            boardTile = tile(ORANGE, "resources/images/tileFlag.png", startRevealed, row, col)
        boardTile.rect.x = width / 6 + col * 60
        if numTiles < 80:
            boardTile.rect.y = height - row * 80 - 130
        else:
            boardTile.rect.y = -160
        numTiles += 1
        game_board.add(boardTile)
        all_sprites_list.add(boardTile)

    return numTiles


def titleLoop():
    running = True
    all_sprites_list.empty()
    game_board.empty()
    just_removed.empty()
    visibleSquares.empty()

    initDifficulty = 10
    font = pygame.font.Font(fontStyle, 50)
    subtitleFont = pygame.font.Font(fontStyle, 35
                                    )
    titleText = font.render("CLIMB-SWEEPER", True, BLACK)
    titleTextRect = titleText.get_rect()
    titleTextRect.center = (width / 2, height / 5)

    highScoreText = subtitleFont.render("Highscore: " + str(userHighScore), True, BLACK)
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.center = (width / 2, height / 5 + 50)

    startText = font.render("NORMAL", True, ORANGE)
    startTextRect = startText.get_rect()
    startTextRect.center = (width / 2, height / 2)

    startButton = pygame.Surface((250, 75), pygame.SRCALPHA)
    startButtonRect = startButton.get_rect()
    startButtonRect.center = (width/2, height/2)


    startEasyText = font.render("EASY", True, ORANGE)
    startEasyTextRect = startEasyText.get_rect()
    startEasyTextRect.center = (width / 6, height / 2)

    startEasyButton = pygame.Surface((175,75), pygame.SRCALPHA)
    startEasyButtonRect = startEasyButton.get_rect()
    startEasyButtonRect.center = (width/6, height/2)


    startHardText = font.render("HARD", True, ORANGE)
    startHardTextRect = startHardText.get_rect()
    startHardTextRect.center = (width - width/6, height / 2)

    startHardButton = pygame.Surface((175,75), pygame.SRCALPHA)
    startHardButtonRect = startHardButton.get_rect()
    startHardButtonRect.center = (width - width/6,height/2)


    exitText = font.render("EXIT", True, ORANGE)
    exitTextRect = exitText.get_rect()
    exitTextRect.center = (width / 2, height / 1.5)

    exitButton = pygame.Surface((175, 75), pygame.SRCALPHA)
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
                    initDifficulty = [10,86]
                    # initDifficulty =  Speed, mine density
                elif startEasyTextRect.collidepoint(event.pos):
                    fxStartGame.play()
                    running = False
                    initDifficulty = [7,90]
                elif startHardTextRect.collidepoint(event.pos):
                    fxStartGame.play()
                    running = False
                    initDifficulty = [11,81]
                elif exitButtonRect.collidepoint(event.pos):
                    pygame.quit()

        screen.fill(background)

        screen.blit(titleText, titleTextRect)

        pygame.draw.rect(screen, BLACK, startButtonRect, 10, 10)
        screen.blit(startText, startTextRect)

        pygame.draw.rect(screen, BLACK, startEasyButtonRect, 10, 10)
        screen.blit(startEasyText, startEasyTextRect)

        pygame.draw.rect(screen, BLACK, startHardButtonRect, 10, 10)
        screen.blit(startHardText, startHardTextRect)

        pygame.draw.rect(screen, BLACK, exitButtonRect, 10, 10)
        screen.blit(exitText, exitTextRect)

        screen.blit(highScoreText, highScoreTextRect)

        pygame.display.update()


    return initDifficulty



def gameLoop(initDifficulty):
    scrollSpeed = initDifficulty[0]
    density = initDifficulty[1]
    FieldMaker.newBoard(ROWSIZE, density)

    tileSpeed = 1
    # Creates mine field
    totalTiles = 0
    displayedRows = 10
    for currentRow in range(displayedRows):
        totalTiles = printBoard(totalTiles, currentRow)

    completedRows = []
    orderOfRemoved = []
    running = True
    selfKill = False
    tilesCleared = 0


    # Text display stuff
    gameScore = 0
    font = pygame.font.Font(fontStyle, 26)
    scoreTextWords = font.render("Score:", True, BLACK)
    scoreTextWordsRect = scoreTextWords.get_rect()
    scoreTextWordsRect.center = (55,25)
    scoreText = font.render(str(gameScore), True, BLACK)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (55,55)
    clock = pygame.time.Clock()


    # Display time-stop
    clockImageRegular = pygame.image.load("resources/images/clock.png")
    clockImage = clockImageRegular
    clockImageCooldown = pygame.image.load("resources/images/clock on cooldown.png")
    clockImageActive = pygame.image.load("resources/images/clock Active.png")
    clockRect = pygame.Rect(width-75,height-75,50,50)
    powerEndTime = 0
    powerCooldownTime = 0


    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.USEREVENT:
                # If mine is clicked do event
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
                if clockRect.collidepoint(event.pos) and powerCooldownTime == 0:
                    clockImage = clockImageCooldown
                    timeClicked = pygame.time.get_ticks()
                    powerEndTime = timeClicked + 5000
                    powerCooldownTime = timeClicked + 45000
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for square in game_board:
                    if square.rect.collidepoint(event.pos):
                        fxFlagPlaced.play()



        for square in game_board:
            square.rect.y += tileSpeed
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
                        while len(orderOfRemoved) > 8:
                            just_removed.remove(orderOfRemoved[0])
                            orderOfRemoved.remove(orderOfRemoved[0])
                    continue

                else:
                    gameScore += square.kill()
                    pygame.mixer.Channel(2).play(fxLineClear)
                    tilesCleared += 1
                    game_board.remove(square)
                    all_sprites_list.remove(square)
                    just_removed.add(square)
                    orderOfRemoved.append(square)

                    # keeps track of the last 8 tiles so that they may be displayed again when the player loses
                    if len(just_removed) > 7:
                        while len(orderOfRemoved) > 8:
                            just_removed.remove(orderOfRemoved[0])
                            orderOfRemoved.remove(orderOfRemoved[0])



        # Will render new row if there are less than ten drawn rows
        if int(tilesCleared/8) > displayedRows - 10:
            totalTiles = printBoard(totalTiles, displayedRows)
            displayedRows += 1


        # Visuals rendering:
        screen.fill(background)

        # Display time stop powerup
        if pygame.time.get_ticks() > powerCooldownTime != 0:
            clockImage = clockImageRegular
            powerCooldownTime = 0
            # time stop over
        elif pygame.time.get_ticks() > powerEndTime != 0:
            clockImage = clockImageCooldown
            powerEndTime = 0
            tileSpeed = 1
            # time stop on cooldown
        elif pygame.time.get_ticks() < powerEndTime != 0:
            clockImage = clockImageActive
            tileSpeed = 0
            # time stop active
        screen.blit(clockImage, clockRect)


        # Display score
        screen.blit(scoreTextWords,scoreTextWordsRect)
        # Re-render text because score may have updated
        scoreText = font.render(str(gameScore), True, BLACK)
        screen.blit(scoreText,scoreTextRect)

        game_board.update(event_list)
        for square in all_sprites_list:
            if square.rect.y > -100:
                visibleSquares.add(square)
            elif square.rect.y >= height:
                visibleSquares.remove(square)
        visibleSquares.draw(screen)
        pygame.display.update()


        if tilesCleared % 8 == 0 and tilesCleared/8 not in completedRows:
            # if new row is completed:
            completedRows.append(tilesCleared/8)
            scrollSpeed += 0.2

        clock.tick(scrollSpeed)

    # Scrolls the tiles upwards so the player sees what they died to, if they died due to time.
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

    return gameScore



def deadOverlay():
    running = True
    font = pygame.font.Font(fontStyle, 25)
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
    startDifficulty = titleLoop()
    score = gameLoop(startDifficulty)
    deadOverlay()
    if int(userHighScore) < score:
        userHighScore = score
        highScoreFile = open("highscore.txt", "w")
        highScoreFile.write(str(score))
        highScoreFile.close()
