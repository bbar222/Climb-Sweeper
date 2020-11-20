import pygame

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

class tile(pygame.sprite.Sprite):

    def __init__(self, color, image, startRevealed):
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

        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.original_image = pygame.image.load(image)
        pygame.draw.rect(self.original_image, color, self.original_image.get_rect(),5)

        self.click_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        # pygame.draw.rect(self.click_image, color, self.click_image.get_rect(),50)
        pygame.draw.rect(self.click_image, (50, 200, 200), self.click_image.get_rect())

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


    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    if not self.isRevealed:
                        self.isRevealed = not self.isRevealed
                    self.isFlag = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.rect.collidepoint(event.pos):
                    if not self.isFlag:
                        self.isFlag = True
                    else:
                        self.isFlag = False

        if self.isRevealed:
            self.image = self.original_image
        elif self.isFlag:
            self.image = self.flag_image
        else:
            self.image = self.click_image
