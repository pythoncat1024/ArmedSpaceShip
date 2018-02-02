# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     daily_build
   Description :
   Author :       cat
   date：          2018/2/2
-------------------------------------------------
   Change Activity:
                   2018/2/2:
-------------------------------------------------
"""


def func():
    import os
    import threading
    import logging
    cmd = r'source build/envsetup.sh && lunch full_gm12b-userdebug && repo sync -j8 && make clean && source build/envsetup.sh && lunch full_gm12b-userdebug && make update-api && make -j8 2>&1 | tee build.log'
    cmd = r'source build/envsetup.sh && lunch full_gm12b-userdebug'
    print("command--==", cmd)
    os.system(cmd)
    threading.Timer(3, func)


def get_now(format="%Y-%m-%d %H:%M:%S"):
    """
    获取今天的日期 --> 返回字符串 ：2018-01-24
    :param format: "%Y-%m-%d"
    :return: 返回字符串 ：2018-01-24
    """
    import time
    formatTime = time.strftime(format, time.localtime(time.time()))
    print(formatTime)
    import threading
    threading.Timer(1,get_now).start()


def show_print(delay=1):
    import threading
    timer = threading.Timer(delay, get_now)
    timer.start()


if "__main__" == __name__:
    # print(get_now())
    show_print(1)
    pass
