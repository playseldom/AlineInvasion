import pygame
from pygame.sprite import Sprite


class Aline(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始化外星人并且设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并且设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都生成在屏幕左上角附近，其实无关紧要
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确位置变化
        self.x = float(self.rect.x)
