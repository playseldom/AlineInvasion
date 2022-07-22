import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from aline import Aline


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并且创建游戏资源"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        """记下来，为这个未知的全屏确定长度和宽度"""
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Aline Invasion")

        # 设置游戏背景色
        self.bg_color = (230, 230, 230)

        # 创建一艘飞船
        self.ship = Ship(self)
        """这个地方的语法非常有意思，把这个文件的一个对象传到了另一个类去"""

        # 创建用于存储子弹的编组
        self.bullets = pygame.sprite.Group()

        # 创建外星人编组
        self.alines = pygame.sprite.Group()
        self._creat_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()   # 更新控制符
            self.ship.update()     # 根据控制符移动
            self.bullets.update()  # 更新子弹位置
            self._update_alines()   # 更新外星人位置，与子弹有先后顺序
            self.delect_bullet(self.bullets)  # 删除消失的子弹
            self._update_screen()  # 更新画面

    def _check_events(self):
        """响应按键和鼠标事件,设置对应控制符"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        # 按键退出程序
        if event.key == pygame.K_q:
            sys.exit()
        # 向右移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # 向左移动
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 开火
        if event.key == pygame.K_SPACE:
            self._fire_buttle()

    def _check_keyup_events(self, event):
        """按键松开"""
        # 停止向右移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # 停止向左移动
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环时都重绘屏幕,‘fill’背景色填充
        self.screen.fill(self.settings.bg_colour)
        # 画飞船
        self.ship.blitme()
        # 画外星人
        self.alines.draw(self.screen)
        # 画子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 让最近绘制的屏幕可见。
        pygame.display.flip()

    def _fire_buttle(self):
        """创建一颗子弹，并将其加入编组"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def delect_bullet(self, bullets):
        """删除过界子弹，根据copy对实体进行操作"""
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_alines(self):
        """
        更新外星人群中所有外星人的位置
        更新整群外星人的位置
        """
        self._check_fleet_edges()
        self.alines.update()

    def _creat_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可以容纳多少个外星人
        # 设外星人之间的间距为一个外星人的单位
        aline = Aline(self)
        aline_width, aline_hight = aline.rect.size
        available_space_x = self.settings.screen_width - (2 * aline_width)
        available_space_y = self.settings.screen_height - self.ship.rect.height - (6 * aline_hight)
        numble_aline_x = available_space_x // (2 * aline_width)
        numble_aline_y = available_space_y // (2 * aline_hight)

        # 创建行和列的外星人
        for y_aline_number in range(numble_aline_y):
            for x_aline_number in range(numble_aline_x):  # 0, 1, 2……
                self._create_aline(x_aline_number, y_aline_number)

    def _create_aline(self, aline_number_x, aline_number_y):
        # 创建一个外星人并将其加入当前行和列
        aline = Aline(self)
        aline_width, aline_height = aline.rect.size
        aline.x = aline_width + 2 * aline_width * aline_number_x  # 设置每一行每个外星人的初始地
        aline.y = aline_height + 2 * aline_height * aline_number_y
        aline.rect.x = aline.x
        aline.rect.y = aline.y
        self.alines.add(aline)

    def _check_fleet_edges(self):
        """有外星人碰到边界时采取相应措施"""
        for aline in self.alines.sprites():
            if aline.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并且改变他们的方向"""
        for aline in self.alines.sprites():  # 遍历每个外星人，每个外星人都执行相同的操作
            aline.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        # 这里很奇怪！！！


if __name__ == '__main__':
    # 上面这段代码的作用确保这个文件作为唯一的运行入口
    # 创建游戏实列并且运行
    ai = AlienInvasion()
    ai.run_game()
