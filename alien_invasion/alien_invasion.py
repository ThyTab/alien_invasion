import sys   #用于退出
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()   #初始化背景
        self.settings = Settings()   #将实例作为参数
        #以下注释代码可实现全屏 
        '''self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width   
        self.settings.screen_height = self.screen.get_rect().height'''
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        #将surface（已配置大小）赋给self.screen的同时创建屏幕
        pygame.display.set_caption("Alien Invasion")   #为屏幕添加标题
        self.clock = pygame.time.Clock()   #为控制帧率做准备
        self.ship = Ship(self)

    def run_game(self):
        '''开始游戏的主循环'''
        while True:   #游戏的主循环
            self._check_event()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)   #控制帧率

    def _check_event(self):
        '''检查按键和鼠标事件'''
        #侦听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   #退出
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _update_screen(self):
        '''用于更新屏幕上的图形并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()   #让最近绘制的屏幕可见，刷新屏幕




if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
