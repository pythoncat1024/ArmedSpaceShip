#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess


def find_target(target_path="./", key='.git'):
    """
    查找目标目录所在的目录 ： 如 /aa/bb/.git --> return /aa/bb/
    :param target_path:
    :param key: target
    :return:
    """
    walk = os.walk(target_path)
    for super_dir, dir_names, file_names in walk:
        for dir_name in dir_names:
            if dir_name == key:
                dir_full_path = os.path.join(super_dir, dir_name)
                # print(dir_full_path, super_dir, dir_name, sep=" ## ")
                yield super_dir


def match_reversion():
    sum_of_path = 0
    target = find_target("./")
    for path in target:
        sum_of_path += 1
        if path.startswith("./"):
            print("-----path:", path[2:])
        else:
            print("-----path:", path)
        command = "git -C {} log -1".format(path)
        # print("command:", command)
        popen = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        blog = popen.stdout.read()  # -- > 成为一个 bytes 字符串了
        log = str(blog, encoding='utf-8')  # --> bytes 2 string
        reversion = log.split("\n")[0][len("commit "):]
        print("reversion={}".format(reversion))
    print("total .git dir==", sum_of_path)


if __name__ == "__main__":
    match_reversion()
