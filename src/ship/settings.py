# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     settings
   Description :
   Author :       cat
   date：          2018/1/22
-------------------------------------------------
   Change Activity:
                   2018/1/22:
-------------------------------------------------
"""


class Settings(object):
    """
    存储《外星人入侵》的所有设置类
    """

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置 (1200,800)
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 210, 200)
