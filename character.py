import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, width:int, height:int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (190, 20, 20)
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
    
    def update(self) -> None:
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
    
    def draw(self, surface) -> None:
        pygame.draw.rect(surface=surface, color=self.color, rect=self.rect)