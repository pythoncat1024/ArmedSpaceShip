# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     dailyEmail
   Description :
   Author :       cat
   date：          2018/1/24
-------------------------------------------------
   Change Activity:
                   2018/1/24:
-------------------------------------------------
"""

"""
GM12E 1月24日 每日版本已经上传服务器：
请大家拷贝到本地刷机，不要直接用下面共享路径下刷机

开发分支版本：
userdebug：\\192.168.59.62\release\dailybuild\aus6797_6m_n\GM12E_7.1_mtk6797_dev_171016\2018-01-24-06-37-42_userdebug
--->                            Z:\dailybuild\aus6797_6m_n\GM12E_7.1_mtk6797_dev_171016\2018-01-24-06-37-42_userdebug

登录方法：\\192.168.59.62   用户名：build 密码：build
南京服务器地址：\\192.168.63.218\share\dailybuild\SH-ReleaseVersion\aus6797_6m_n\GM12E_7.1_mtk6797_dev_171016\2018-01-24-06-37-42_userdebug
------------>                    W:\dailybuild\SH-ReleaseVersion\aus6797_6m_n\GM12E_7.1_mtk6797_dev_171016\2018-01-24-06-37-42_userdebug

=================================================================================

GMOS2.X 1月23日 每日版本已经上传服务器：
请大家拷贝到本地刷机，不要直接用下面共享路径下刷机

开发分支版本：
user:\\192.168.59.62\release\dailybuild\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-23-04-05-50_user
                          Z:\dailybuild\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-23-04-05-50_user
userdebug：\\192.168.59.62\release\dailybuild\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-23-04-11-13_userdebug
                                W:\dailybuild\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-23-04-11-13_userdebug

登录方法：\\192.168.59.62   用户名：build 密码：build



南京服务器地址：
user: \\192.168.63.218\share\dailybuild\SH-ReleaseVersion\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-23-04-05-50_user
                           V:\dailybuild\SH-ReleaseVersion\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-23-04-05-50_user
userdebug: \\192.168.63.218\share\dailybuild\SH-ReleaseVersion\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-23-04-11-13_userdebug
                                V:\dailybuild\SH-ReleaseVersion\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-23-04-05-50_user
"""


def today(format="%Y-%m-%d"):
    """
    获取今天的日期 --> 返回字符串 ：2018-01-24
    :param format: "%Y-%m-%d"
    :return: 返回字符串 ：2018-01-24
    """
    import time
    formatTime = time.strftime(format, time.localtime(time.time()))
    return formatTime


def today_target(rootPath, mode='userdebug'):
    """
    获取今天的每日版本路径 --> 返回一个可以刷机的daily 版本路径
    :param rootPath:  根目录
    :param mode: 编译模式: userdebug user eng
    :return: 返回一个可以刷机的daily 版本路径
    """
    import os
    import logging
    target = ""
    listdir = os.listdir(rootPath)
    for name in listdir:
        if name.startswith(today()) and name.endswith(mode):
            # 就是你了，今天要发的版本
            target = name
            break
    else:
        target = "ERROR:今天的每日版本没有-###{}###-{}".format(mode, rootPath)
        logging.error("ERROR:今天的每日版本没有-###{}###-{}".format(mode, rootPath))

    return os.path.join(rootPath, target)


def trans_WXYZ_to_realPath(srcPath):
    import os
    import logging
    """
    todo: 这个转换仅仅在我本地有效！
    将 X:\share --> 转换为 \\192.168.59.xx\share
    :return: 转换后的路径
    """
    dest = ""
    z = r"Z:"  # \\192.168.59.62\release
    y = r"Y:"  # cdz --> 发版本用不到
    x = r"X:"  # 27 ---> 发版本用不到
    w = r"W:"  # \\192.168.63.218\share
    v = r"V:"  # \\192.168.63.218\share
    if srcPath.startswith(z):
        dest = os.path.join(r"\\192.168.59.62\release", srcPath[len(z) + 1:])
    elif srcPath.startswith(y):
        logging.error("ERROR:这个路径没有去适配！{}".format(srcPath))
        pass
    elif srcPath.startswith(x):
        logging.error("ERROR:这个路径没有去适配！{}".format(srcPath))
        pass
    elif srcPath.startswith(w):
        dest = os.path.join(r"\\192.168.63.218\share", srcPath[len(w) + 1:])
    elif srcPath.startswith(v):
        dest = os.path.join(r"\\192.168.63.218\share", srcPath[len(v) + 1:])
    if not os.path.exists(dest):
        logging.error("ERROR: 目标目录不存在！！{}".format(dest))
    return dest


def date_today(format1="%m", format2="%d"):
    """
        获取今天的日期 --> 返回字符串 ：1月23日
        :param format: "%Y-%m-%d"
        :return: 返回字符串 ：1月23日
        """
    import time
    month = time.strftime(format1, time.localtime(time.time()))
    day = time.strftime(format2, time.localtime(time.time()))
    return "{}月{}日".format(month, day)


def send_text_12e():
    import time
    text = r"""GM12E {} 每日版本已经上传服务器：
请大家拷贝到本地刷机，不要直接用下面共享路径下刷机

开发分支版本：
userdebug：{}

登录方法：\\192.168.59.62   用户名：build 密码：build
南京服务器地址：{}
"""
    rootPath_12e_sh = r"Z:\dailybuild\aus6797_6m_n\GM12E_7.1_mtk6797_dev_171016"
    rootPath_12e_nj = r"W:\dailybuild\SH-ReleaseVersion\aus6797_6m_n\GM12E_7.1_mtk6797_dev_171016"
    daily_12e_sh_userdebug = trans_WXYZ_to_realPath(today_target(rootPath_12e_sh))
    daily_12e_nj_userdebug = trans_WXYZ_to_realPath(today_target(rootPath_12e_nj))
    day = date_today()
    time.sleep(0.5)  # 休眠500ms
    text_format = text.format(day, daily_12e_sh_userdebug, daily_12e_nj_userdebug)
    info = ""
    for line in text_format.split(sep='\n'):
        if line.find("ERROR:") == -1:
            info += line
            info += '\n'
    print(info)


def send_text_os2x():
    import time
    text = r"""GMOS2.X {} 每日版本已经上传服务器：
请大家拷贝到本地刷机，不要直接用下面共享路径下刷机

开发分支版本：
user:{}
userdebug：{}

登录方法：\\192.168.59.62   用户名：build 密码：build


南京服务器地址：
user: {}
userdebug: {}
"""
    rootPath_os2x_sh = r"Z:\dailybuild\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop"
    rootPath_os2x_nj = r"V:\dailybuild\SH-ReleaseVersion\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop"
    day = date_today()
    daily_os2x_sh_user = trans_WXYZ_to_realPath(today_target(rootPath_os2x_sh, "user"))
    daily_os2x_sh_userdebug = trans_WXYZ_to_realPath(today_target(rootPath_os2x_sh))
    daily_os2x_nj_user = trans_WXYZ_to_realPath(today_target(rootPath_os2x_nj, "user"))
    daily_os2x_nj_userdebug = trans_WXYZ_to_realPath(today_target(rootPath_os2x_nj))
    # print("daily_path===", daily_os2x_sh_user)  # 12e nj daily path 完成
    # print("daily_path===", daily_os2x_sh_userdebug)  # 12e nj daily path 完成
    # print("daily_path===", daily_os2x_nj_user)  # 12e nj daily path 完成
    # print("daily_path===", daily_os2x_userdebug)  # 12e nj daily path 完成
    time.sleep(0.5)  # 休眠500ms
    text_format = text.format(day, daily_os2x_sh_user, daily_os2x_sh_userdebug, daily_os2x_nj_user,
                              daily_os2x_nj_userdebug)
    info = ""
    for line in text_format.split(sep='\n'):
        # print("line", not line.find("ERROR"), line)
        if line.find("ERROR") == -1:
            info += line
            info += '\n'
    print(info)


if "__main__" == __name__:
    send_12e = False
    if send_12e:
        send_text_12e()
    else:
        send_text_os2x()

    pass
