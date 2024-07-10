import pygame

from character import Character


class Player(Character):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.alive = True
        self.v_velocity = 0
        self.mass = 0.2
        
    def update(self) -> None:
        super().update()
        self.y += self.v_velocity
        self.v_velocity += self.mass
    
    
    def move_left(self) -> None:
        self.x -= 4
    def move_right(self) -> None:
        self.x += 4
    def jump(self) -> None:
        self.v_velocity = -5