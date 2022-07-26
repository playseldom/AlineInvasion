import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并且创建游戏资源"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Aline Invasion")

        # 设置游戏背景色
        self.bg_color = (230, 230, 230)

        # 创建一艘飞船
        self.ship = Ship(self)
        """这个地方的语法非常有意思，把这个文件的一个对象传到了另一个类去"""

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()   # 更新控制符
            self.ship.update()     # 根据控制符移动
            self._update_screen()  # 更新画面


    def _check_events(self):
        """响应按键和鼠标事件,设置对应控制符"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 向右移动飞船
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时都重绘屏幕,‘fill’背景色填充
        self.screen.fill(self.settings.bg_colour)
        # 画飞船
        self.ship.blitme()
        # 让最近绘制的屏幕可见。
        pygame.display.flip()


if __name__ == '__main__':
    # 上面这段代码的作用确保这个文件作为唯一的运行入口
    # 创建游戏实列并且运行
    ai = AlienInvasion()
    ai.run_game()
