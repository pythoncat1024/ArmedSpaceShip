# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     merge_mtk
   Description :
   Author :       cat
   date：          2018/2/1
-------------------------------------------------
   Change Activity:
                   2018/2/1:
-------------------------------------------------
"""


def unzip_file(zipPath):
    """
    解压缩 ，并输出解压后的全部文件的路径
    :param zipPath: 压缩包路径
    :return: path list
    """
    import subprocess
    command = "tar  -zxvf {}".format(zipPath)
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    origin_strB = popen.stdout.read()  # -- > 成为一个 bytes 字符串了
    origin_strs = str(origin_strB, encoding='utf-8')  # --> bytes 2 string
    # print("origin_str=======", origin_strs.split('\n'))
    lines = [line for line in origin_strs.split('\n') if line]  # 移除空字符串
    for line in lines:
        print("line-->", line)
    return lines


def find_target(target_path="./", key='.git'):
    """
    这个方式太慢了 <--- 已废弃
    查找目标目录所在的目录 ： 如 ／aa/bb/.git --> return /aa/bb/
    :param target_path:
    :param key: target
    :return:
    """
    import os
    walk = os.walk(target_path)
    for super_dir, dir_names, file_names in walk:
        for dir_name in dir_names:
            if dir_name == key:
                dir_full_path = os.path.join(super_dir, dir_name)
                # print(dir_full_path, super_dir, dir_name, sep=" ## ")
                yield super_dir


def find_target2(target_path="./"):
    """
    查找一个项目的所有 project
    查找目标目录所在的目录 ： 如 ／aa/bb/.git --> return /aa/bb/
    :param target_path:
    :param key: target
    :return:
    """
    import os
    repo_dir_name = '.repo'
    project_list_name = 'project.list'
    repo_path = os.path.join(target_path, repo_dir_name)
    print("repo-path--->", repo_path)
    for subName in os.listdir(repo_path):
        if subName == project_list_name:
            break
    else:
        raise Exception("target path:[{}]不对，没有找到对应的{}".format(target_path, project_list_name))
    project_list_Path = os.path.join(repo_path, project_list_name)

    print("project_list---> ", project_list_Path)
    for line in open(project_list_Path):
        if line:
            yield line.strip()  # 移除空格以及尾部的换行符


def status(target_path, project_list):
    clean1 = "Not currently on any branch"
    clean2 = "nothing to commit, working directory clean"
    change = []
    import os
    import subprocess
    for path in project_list:
        tpath = os.path.join(target_path, path)
        if not os.path.exists(tpath):
            tpath = path
        if not os.path.exists(tpath):
            raise Exception('No such file or directory {}'.format(tpath))
        command = "git -C {} status".format(tpath)
        print("command--==", command)
        popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        popen.wait()
        # print("####popen$$$$ ", popen, popen.returncode)
        # logging.error("popen.returncode-->{}".format(popen.returncode))
        if popen and popen.returncode == 0:
            origin_strB = popen.stdout.read()  # -- > 成为一个 bytes 字符串了
            origin_strs = str(origin_strB, encoding='utf-8')  # --> bytes 2 string
            if not (clean1 in origin_strs) and not (clean2 in origin_strs):
                "说明是本地有未提交的..."
                change.append(tpath)
                print(tpath)
                print(origin_strs)

    print("status() 结束了###.........")
    if len(change):
        print("当前分支有未提交的修改！！！")
    return change


"""
line--> alps/
line--> alps/device/
line--> alps/device/ausshine/
line--> alps/device/ausshine/aus6797_6m_n/
line--> alps/device/ausshine/aus6797_6m_n/ProjectConfig.mk
line--> alps/vendor/
line--> alps/vendor/ausshine/
line--> alps/vendor/ausshine/libs/
line--> alps/vendor/ausshine/libs/libClearMotionFW/
line--> alps/vendor/ausshine/libs/libClearMotionFW/arm/
line--> alps/vendor/ausshine/libs/libClearMotionFW/arm/libClearMotionFW.so
line--> patch_list.txt
"""

if "__main__" == __name__:
    import sys
    import os

    if len(sys.argv) == 1:
        # 没有进行任何的传参
        changes = status(os.getcwd(), find_target2(os.getcwd()))
        print("未提交的修改为:\n", changes)
    else:
        changes = status(sys.argv[2], find_target2(sys.argv[2]))
    print("未提交的修改为:\n", changes)
