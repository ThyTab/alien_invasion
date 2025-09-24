import pygame

class Ship:
    '''管理飞船的类'''
    def __init__(self,ai_game):
        '''初始化飞船并设置初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()   #获取屏幕的外接矩形

        '''加载飞船图形并获取其外接矩形'''
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        '''每艘新飞船都放在屏幕底部的中央'''
        self.rect.midbottom = self.screen_rect.midbottom 

    def blitem(self):
        '''在特定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
        #blit() 是将一个图像（Surface）绘制到另一个图像（通常是屏幕）上的核心方法
        #语法：目标图像.blit(源图像, 位置/矩形)     位置：（x,y）   矩形：即矩形对象

        