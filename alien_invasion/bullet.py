import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞船发射的子弹的类'''
    def __init__(self, ai_game):
        '''在飞船的当前位置添加一个子弹对象'''
        super().__init__()   #调用super()来继承Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #在（0，0）处创建子弹矩形，再设置正确的位置