class Settings:
    """存储游戏《外星人入侵》中所有设置的 类"""

    def __init__(self):
        """初始化游戏的静态设置"""

        # 计分
        self.aline_points = 20

        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 10.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 6

        # 外星人设置
        self.fleet_drop_speed = 20

        # 加快游戏节奏的速度
        self.speedup_scale = 1.5
        # 外星人分数提高的速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 5
        self.bullet_speed = 3
        self.aline_speed = 5

        # fleet_direction 为1表示向右移，-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度和外星人分数设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.aline_speed *= self.speedup_scale

        self.aline_points = int(self.aline_points *  self.score_scale)
        print(f"当前等级的分数为:{self.aline_points}")