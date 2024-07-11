import pygame

from character import Character
from tile import Tile, Tilemap


class Player(Character):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.alive = True
        self.v_velocity = 0
        self.mass = 0.2
        self.on_ground = False
        
    def update(self, tilemap:Tilemap) -> None:
        super().update()
        colliding_tiles = pygame.sprite.spritecollide(self, tilemap, False)
        if not colliding_tiles:
            self.on_ground = False
            self.free_fall()
            return None
        if not self.on_ground:
            for tile in colliding_tiles:
                self.collide_with_tile(tile)
        
    
    def collide_with_tile(self, tile:Tile) -> None:
        if not tile.walkable:
            return None
        if self.is_collide_bottom(tile) and not self.is_collide_top(tile):
            self.on_ground = True
            self.v_velocity = 0
            self.y = tile.y - self.height
        if self.is_collide_top(tile) and not self.is_collide_bottom(tile):
            self.v_velocity = 0
            self.y = tile.y + self.height
        if self.is_collide_left(tile):
            self.x = tile.x+tile.width
        if self.is_collide_right(tile):
            self.x = tile.x - self.width
            
    
    def is_collide_bottom(self, tile:Tile) -> bool:
        return self.y < tile.y < self.y+self.height
    def is_collide_top(self, tile:Tile) -> bool:
        return self.y < tile.y+tile.height < self.y+self.height
    def is_collide_left(self, tile:Tile) -> bool:
        return self.x < tile.x+tile.width < self.x+self.width
    def is_collide_right(self, tile:Tile) -> bool:
        return self.x < tile.x < self.x+self.width
    
    def free_fall(self):
        self.y += self.v_velocity
        self.v_velocity += self.mass
    
    def move_left(self) -> None:
        self.x -= 4
    def move_right(self) -> None:
        self.x += 4
    def jump(self) -> None:
        if self.on_ground:
            self.on_ground = False
            self.v_velocity = -5