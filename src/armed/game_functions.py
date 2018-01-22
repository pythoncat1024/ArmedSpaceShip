# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     game_functions
   Description :  存储大量让游戏运行的函数
   Author :       cat
   date：          2018/1/22
-------------------------------------------------
   Change Activity:
                   2018/1/22:
-------------------------------------------------
"""
import sys
import pygame
import logging

# 设置log 显示的最低级别
logging.getLogger().setLevel(logging.INFO)


def check_events(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logging.info("关闭窗口...")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            logging.debug('KEY_DOWN')
            if event.key == pygame.K_d:
                ship.move_right = True
            elif event.key == pygame.K_a:
                ship.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.move_right = False
            elif event.key == pygame.K_a:
                ship.move_left = False


def update_screen(ai_settings, screen, ship):
    # 每次循环都绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
