class Settings:
    """存储游戏设置有关的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1500
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        self.ship_speed = 0.5