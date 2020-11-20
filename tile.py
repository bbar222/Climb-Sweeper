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

    def __init__(self, color, width, height, image):
        super().__init__()
        self.revealed = False
        self.imageBorder = pygame.Surface([width,height])
        #pygame.draw.rect(self.imageBorder, color)
        self.image = pygame.Surface([width, height])

        self.rect = self.image.get_rect()
        if image == "NONE":
            pygame.draw.rect(self.image, color, (0, 0, width, height))
        else:
            self.image = pygame.image.load(image)

        #self.image.blit(self.tileBG, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

        if self.revealed:
            pygame.draw.rect(self.image, color, (0, 0, width, height), 4)
        else:
            pygame.draw.rect(self.image, COLORHIDDEN, (0, 0, width, height))


    def revealTile(self):
        if not self.revealed:
            self.revealed = True
        else:
            self.revealed = False

