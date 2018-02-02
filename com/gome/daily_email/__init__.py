# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       cat
   date：          2018/1/24
-------------------------------------------------
   Change Activity:
                   2018/1/24:
-------------------------------------------------
"""


def timer(delay, func):
    import threading
    threading.Timer(delay, func).start()


def showPower(delay):
    """
    好像只能通过这种所谓“闭包”的方式实现无限定时任务了
    :param delay:
    :return:
    """

    def show():
        import time
        import threading
        print(threading.current_thread().getName(), time.time())
        threading.Timer(delay, show).start()

    show()


if "__main__" == __name__:
    showPower(3)
    pass
