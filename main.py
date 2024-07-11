import pygame

from settings import *
from tile import Tilemap
from player import Player
from ball_testing import Ball_testing

class Game():
    def __init__(self) -> None:
        pygame.font.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Arcade shooter @ h4sski')
        
        self.main_screen = pygame.Surface(size=MAIN_SCREEN_SIZE)
        self.bottom_bar = pygame.Surface(size=BOTTOM_BAR_SIZE)
        
        self.tilemap = Tilemap()
        self.player = Player(100, 400, 15, 35)
        # testing purpouse
        # self.ball_testing = Ball_testing(self.main_screen)
        
        self.run()
        
        
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        # for tile_clodie in pygame.sprite.spritecollide(self.player, self.tilemap, False):
        #     self.player.v_velocity = 0
        #     self.player.collide_with_tile(tile=tile_clodie)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.move_left()
        if keys[pygame.K_d]:
            self.player.move_right()
        if keys[pygame.K_w]:
            self.player.jump()
    
    def update(self) -> None:
        self.player.update(self.tilemap)
        # testing purpouse
        # self.ball_testing.update()
    
    def draw(self) -> None:
        self.window.fill(0)
        
        # main_screen
        self.main_screen.fill(BG_COLOR)
        # draw the tilemap
        for tile in self.tilemap.sprites():
            tile.draw(self.main_screen)
        # draw player
        self.player.draw(self.main_screen)
        
        # testing purpouse
        # self.ball_testing.draw()
        
        # pygame.draw.rect(self.main_screen, self.ball_testing.color,
        #                  self.ball_testing.rect)
        # print(f'{self.ball_testing.width = }    {self.ball_testing.height = }')
        
        # bottom_bar
        self.bottom_bar.fill(BOTTOM_BAR_BG)
        
        
        # blit all surfaces into main window
        self.window.blit(self.main_screen, (0, 0))
        self.window.blit(self.bottom_bar, (0, MAIN_SCREEN_SIZE[1]))
        
        pygame.display.flip()
    
    
    def run(self) -> None:
        while self.running:
            self.events()
            self.update()
            self.draw()
        
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == '__main__':
    game = Game()