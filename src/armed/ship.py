# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Ship
   Description :  负责管理飞船的大部分行为
   Author :       cat
   date：          2018/1/22
-------------------------------------------------
   Change Activity:
                   2018/1/22:
-------------------------------------------------
"""
import pygame

import os


class Ship(object):
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('../../images/ship_small_alpha.png')

        # print("---path===",os.getcwd())
        # E:\py\ArmedSpaceship\src\armed
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right:
            self.rect.centerx += 1
        if self.move_left:  # 注意：这里用if 而不是 elif 是为了让 条件1，条件2 机会均等，而不是条件1优先
            self.rect.centerx -= 1
