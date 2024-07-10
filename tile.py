import pygame
import random

from settings import *


class Tilemap(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        
        self.generate_tilemap()
    
    def generate_tilemap(self) -> None:
        for x in [TILE_SIZE[0] * i for i in range(20)]:
            self.add(Tile(x, 600, tile_type=random.randint(0,1)))
            


class Tile(pygame.sprite.Sprite):
    # def __init__(self, tile_type:int = 0, *groups: AbstractGroup[_SpriteSupportsGroup]) -> None:
    def __init__(self, x:int, y:int, tile_type:int = 0) -> None:
        # super().__init__(*groups)
        super().__init__()
        self.width, self.height = TILE_SIZE
        self.tile_type = tile_type
        self.x = x
        self.y = y
        
        self.image = 0
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
        # self.surface = surface
        
        self.assign_tile_type()
    
    def assign_tile_type(self):
        self.walkable = TILE_TYPES[self.tile_type]['walkable']
        self.color = TILE_TYPES[self.tile_type]['color']
        
    def draw(self, surface):
        # super().draw()
        pygame.draw.rect(surface, self.color, self.rect)


TILE_TYPES = {
    0: {
        'walkable': True,
        'color': (30, 90, 30),
    },
    1: {
        'walkable': True,
        'color': (30, 110, 50),
    },
}