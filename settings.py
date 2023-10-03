class Settings:
    """存储游戏设置有关的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1500
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1

        # 子弹设置
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed = 0.6
        self.fleet_drop_speed = 10
        # 1表示右移
        self.fleet_direction = 1
