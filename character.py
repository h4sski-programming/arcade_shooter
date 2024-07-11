import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, width:int, height:int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (190, 20, 20)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
    
    def update(self) -> None:
        self.rect.x = self.x
        self.rect.y = self.y
        # self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        # pass
    
    def draw(self, surface) -> None:
        pygame.draw.rect(surface=surface, color=self.color, rect=self.rect)