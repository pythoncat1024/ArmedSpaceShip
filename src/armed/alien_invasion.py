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

import pygame

from armed import game_functions as gf
from armed.settings import Settings
from armed.ship import Ship

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

    ship = Ship(screen)

    # 开始游戏的主循环🐖
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update(ai_settings)
        # 每次循环都绘制屏幕
        gf.update_screen(ai_settings, screen, ship)


if __name__ == "__main__":
    run_game()
