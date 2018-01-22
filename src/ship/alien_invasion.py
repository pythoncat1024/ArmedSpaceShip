# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     alien_invasion
   Description :  武装飞船：游戏入口 ！！！
   Author :       cat
   date：          2018/1/22
-------------------------------------------------
   Change Activity:
                   2018/1/22:
-------------------------------------------------
"""

import logging
import sys

import pygame

from ship.settings import Settings

# 设置log 显示的最低级别
logging.getLogger().setLevel(logging.DEBUG)


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # width_height = (1200,800)
    bg_color = (230, 230, 230)
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环🐖
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info("关闭窗口...")
                sys.exit()

        # 每次循环都绘制屏幕
        screen.fill(ai_settings.bg_color)
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == "__main__":
    run_game()
