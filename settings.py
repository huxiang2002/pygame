class Settings:
    """存储游戏设置有关的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1500
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # 外星人设置
        self.fleet_drop_speed = 10
        # 加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化动态设置"""
        self.ship_speed = 1.0
        self.bullet_speed = 2.0
        self.alien_speed = 0.3

        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
