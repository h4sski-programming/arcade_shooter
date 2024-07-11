import pygame
import math


class Ball_testing(pygame.sprite.Sprite):
    def __init__(self, surface:pygame.Surface) -> None:
        super().__init__()
        
        self.x = 100
        self.y = 100
        self.width = 20
        self.height = self.width
        self.radius = self.width/2
        
        self.surface = surface
        self.color = 'orange'
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        
        self.angle = 1.8
        self.speed = 2
    
    def update(self) -> None:
        surface_size = self.surface.get_size()
        new_x, new_y = self.get_new_xy()
        if new_y+self.height > surface_size[1] or new_y < 0:
            self.angle *= -1
        if new_x+self.width > surface_size[0] or new_x < 0:
            self.angle -= math.pi
            self.angle *= -1
        self.x, self.y = self.get_new_xy()
    
    def get_new_xy(self) -> list[float]:
        return (self.x + self.speed * math.cos(self.angle),
                self.y + self.speed * math.sin(self.angle))
    
    def draw(self) -> None:
        pygame.draw.circle(self.surface, self.color,
                           (self.x+self.radius, self.y+self.radius),
                           self.radius)