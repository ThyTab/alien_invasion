import sys   #用于退出
import pygame
from settings import Settings

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()   #初始化背景
        self.settings = Settings()   #将实例作为参数
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))   
        #将surface（已配置大小）赋给self.screen的同时创建屏幕
        pygame.display.set_caption("Alien Invasion")   #为屏幕添加标题
        self.clock = pygame.time.Clock()   #为控制帧率做准备

    def run_game(self):
        '''开始游戏的主循环'''
        while True:   #游戏的主循环
            #侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()   #退出
            pygame.display.flip()   #让最近绘制的屏幕可见，刷新屏幕
            self.clock.tick(60)   #控制帧率
            self.screen.fill(self.settings.bg_color)

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
