class Settings:
    """存储游戏《外星人入侵》中所有设置的 类"""

    def __init__(self):
        """初始化游戏设置"""

        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 6

        # 外星人设置
        self.aline_speed = 10
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移，-1表示向左移
        self.fleet_direction = 1

