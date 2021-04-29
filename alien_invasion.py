import sys
import pygame
from settings import Settings


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):  # 初始化游戏屏幕
        pygame.init()
        self.settings = Settings()  # 创造了Settings实例并赋值self.settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def ren_game(self):
        while True:
            """开始游戏的主循环"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.ren_game()
