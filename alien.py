import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示外星人的类"""

    def __init__(self, ai_game):
        """外星人初始化"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect = self.image.get_rect()

        # 存储外星人的精准水平位置
        self.x = float(self.rect.x)