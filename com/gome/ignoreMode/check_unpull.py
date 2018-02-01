# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     check_unpull
   Description :
   Author :       cat
   date：          2018/2/1
-------------------------------------------------
   Change Activity:
                   2018/2/1:
-------------------------------------------------
"""


def find_target2(target_path="./", key='.git'):
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


if "__main__" == __name__:
    import sys
    import os

    if len(sys.argv) == 1:
        # 没有进行任何的传参
        changes = status(os.getcwd(), find_target2(os.getcwd()))
    else:
        changes = status(sys.argv[1], find_target2(sys.argv[1]))

    print("未提交的修改为:\n", changes)
    pass
