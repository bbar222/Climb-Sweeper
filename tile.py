import pygame
import FieldMaker

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
COLORNULL = (255, 255, 255)
COLORHIDDEN = (123, 143, 93)
PURPLE = (160, 32, 240)
ORANGE = (255, 165, 0)
BROWN = (150, 75, 0)
LIGHTBLUE = (0, 128, 255)

screen = pygame.display.set_mode((700, 640))

# Tile images made by Brian (me)

CLICK_MINE = pygame.event.Event(pygame.USEREVENT, myID=1)
CLICK_ZERO = pygame.event.Event(pygame.USEREVENT, myID=2)


class tile(pygame.sprite.Sprite):

    # Concept from https://stackoverflow.com/questions/53660333/pygame-drawing-multiple-rectangles

    def __init__(self, color, image, startRevealed, boardR, boardC):
        super().__init__()

        self.boardR = boardR
        self.boardC = boardC
        self.revealedTile = pygame.image.load(image)
        pygame.draw.rect(self.revealedTile, color, self.revealedTile.get_rect(), 5)

        self.unrevealedTile = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.rect(self.unrevealedTile, (75, 175, 200), self.unrevealedTile.get_rect())

        self.flag_image = pygame.image.load("resources/images/tileFlag - transp.png")
        pygame.draw.rect(self.flag_image, ORANGE, self.flag_image.get_rect(), 5)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.isRevealed = startRevealed
        self.isFlag = False

    def kill(self):
        if self.image == self.flag_image and FieldMaker.field[self.boardR, self.boardC] == FieldMaker.tiles.get("mine"):
            # print("A flagged mine escaped! Yay!")
            return 1
        elif self.image == self.unrevealedTile:
            # print("an unmarked tile escaped! yikes!")
            return "dead"
        elif self.image == self.flag_image and not FieldMaker.field[self.boardR, self.boardC] == FieldMaker.tiles.get(
                "mine"):
            # print("You falsely flagged a tile!")
            return "dead"
        else:
            return 0

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):

                    if not self.isRevealed:
                        self.isRevealed = not self.isRevealed
                    self.isFlag = False
                    if FieldMaker.field[self.boardR, self.boardC] == FieldMaker.tiles.get("mine"):
                        pygame.event.post(CLICK_MINE)
                if FieldMaker.field[self.boardR, self.boardC] == FieldMaker.tiles.get("empty"):
                    # for all tiles which are 0:
                    pass

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.rect.collidepoint(event.pos):
                    if not self.isFlag:
                        self.isFlag = True
                    else:
                        self.isFlag = False

        if self.isRevealed:
            self.image = self.revealedTile
        elif self.isFlag:
            self.image = self.flag_image
        else:
            self.image = self.unrevealedTile
