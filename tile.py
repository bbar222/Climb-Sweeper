
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
COLORNULL = (255,255,255)
COLORHIDDEN = (123,143,93)


CLICK_MINE = pygame.event.Event(pygame.USEREVENT, myID=1)
CLICK_ZERO = pygame.event.Event(pygame.USEREVENT, myID=2)


class tile(pygame.sprite.Sprite):


    def __init__(self, color, image, startRevealed, boardR, boardC):
        super().__init__()

        # self.revealed = False
        # self.imageBorder = pygame.Surface([width,height])
        # # pygame.draw.rect(self.imageBorder, color)
        # self.image = pygame.Surface([width, height])
        #
        # self.rect = self.image.get_rect()
        # if image == "NONE":
        #     pygame.draw.rect(self.image, color, (0, 0, width, height))
        # else:
        #     self.image = pygame.image.load(image)
        # self.tileUnknown = pygame.image.load("resources/images/tileUnknown.png")
        # #self.image.blit(self.tileBG, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        # self.unknownTile = pygame.Surface([width,height])
        # pygame.draw.rect(self.unknownTile, color, self.unknownTile.get_rect())
        # self.revealedTile = pygame.Surface([width,height])
        # pygame.draw.rect(self.revealedTile, color, self.revealedTile.get_rect())
        # self.image = self.unknownTile
        # self.rect = self.image.get_rect()
        # self.revealed = False

        self.boardR = boardR
        self.boardC = boardC
        self.revealedTile = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.revealedTile = pygame.image.load(image)
        pygame.draw.rect(self.revealedTile, color, self.revealedTile.get_rect(), 5)


        self.unrevealedTile = pygame.Surface((50, 50), pygame.SRCALPHA)
        # pygame.draw.rect(self.unrevealedTile, color, self.unrevealedTile.get_rect(),50)
        pygame.draw.rect(self.unrevealedTile, (50, 200, 200), self.unrevealedTile.get_rect())

        self.flag_image = pygame.Surface((50,50), pygame.SRCALPHA)
        self.flag_image = pygame.image.load("resources/images/tileFlag.png")
        pygame.draw.rect(self.flag_image, BLACK, self.flag_image.get_rect(),5)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.isRevealed = startRevealed
        self.isFlag = False




    # def update(self, event_list):
    #     for event in event_list:
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if self.rect.collidepoint(event.pos):
    #                 self.revealed = True
    #     self.image = self.revealedTile



    def kill(self):
        # print(self.boardR,",",self.boardC,"IS DEAD")
        if self.image == self.flag_image and FieldMaker.field[self.boardR, self.boardC] == FieldMaker.tiles.get("mine"):
            print("A flagged mine escaped! Yay!")
            return 1
        elif self.image == self.unrevealedTile:
            print("an unmarked tile escaped! yikes!")
            return "dead"
        elif self.image == self.flag_image and not FieldMaker.field[self.boardR, self.boardC] == FieldMaker.tiles.get("mine"):
            print("You falsely flagged a tile!")
            return "dead"
        else:
            return 0


    def update(self, event_list):
        # print(event_list)
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # #### wtf is this   self.image.get_rect().move(100,100)
                if self.rect.collidepoint(event.pos):

                    if not self.isRevealed:
                        self.isRevealed = not self.isRevealed
                    self.isFlag = False
                    if FieldMaker.field[self.boardR, self.boardC] == FieldMaker.tiles.get("mine"):
                        pygame.event.post(CLICK_MINE)
                if FieldMaker.field[self.boardR, self.boardC] == FieldMaker.tiles.get("empty"):
                    # for all tiles which are 0:
                    pass
                    # if self.boardR != 99 and self.boardR != 0 and self.boardC != 0 and FieldMaker.field[self.boardR, self.boardC - 1] == FieldMaker.tiles.get("empty") and FieldMaker.field[self.boardR - 1, self.boardC] == FieldMaker.tiles.get("empty") and FieldMaker.field[self.boardR + 1, self.boardC] == FieldMaker.tiles.get("empty"):
                    #     self.image.fill(BLUE)

                    # https://stackoverflow.com/questions/19106911/recursive-minesweeper-0-fill
                    # maybe useful ?




                    #   TODO: Auto-clear other surrounding zeroes
                  # zeroLoc = event.pos
                  #  self.revealArea(self, zeroLoc)
                    #print(self.rect.x,",",self.rect.y, "EVENTPOS = ",event.pos[0],",",event.pos[1])
                    # if abs(self.rect.centerx - event.pos[0]) < 60:
                    #     self.image.fill(BLUE)




            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.rect.collidepoint(event.pos):
                    if not self.isFlag:
                        self.isFlag = True
                    else:
                        self.isFlag = False

            # elif event.type == pygame.USEREVENT:
            #     #print("its happening")
            #     if event.myID == 1:
            #         if self.image == self.flag_image:
            #             pass
            #             #print("A flag escaped")


        if self.isRevealed:
            self.image = self.revealedTile
        elif self.isFlag:
            self.image = self.flag_image
        else:
            self.image = self.unrevealedTile


    def revealArea(self, location):
        pass



    def reveal(self, curRow, curCol):
        if FieldMaker.field[self.boardR+1, self.boardC] == FieldMaker.field[curRow, curCol]:
            print("hehehehehe")

            # self.image.fill(BLUE)