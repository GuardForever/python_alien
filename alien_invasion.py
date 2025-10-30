import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    '''
    管理游戏资源和行为的类
    '''                                                                                                                                                                                                                     
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bg_color = self.settings.bg_color


    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()  

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  
                self._check_keyup_events(event)
                    

    def _check_keydown_events(self,event):
        '''响应按下'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key ==  pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()    
        elif event.key == pygame.K_q:
            sys.exit()    

    def _check_keyup_events(self,event):
        '''响应释放'''
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = False
        elif event.key ==  pygame.K_LEFT:
            self.ship.moving_left = False        

    def _fire_bullet(self):
        '''创建子弹'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        #删除超出屏幕的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()