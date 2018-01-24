# -*- coding: utf-8 -*-
import xml.dom.minidom
import os
import subprocess


def diffCommitMsgNormal(oldPath, newlyPath, codeGm12eDir):
    """
    获取 diff 信息并存入 list中
    :param oldPath: 对比文件的 旧路径
    :param newlyPath: 对比文件的 新路径
    :param codeGm12eDir: 代码路径根目录
    :return: dict_list: [{"path01":[ci01,ci02]},{"path02":[ci01,ci02,..]},...]
    """
    ret_list = list()

    oldDom = xml.dom.minidom.parse(oldPath)
    newlyDom = xml.dom.minidom.parse(newlyPath)
    oldProjects = oldDom.getElementsByTagName("project")
    newlyProjects = newlyDom.getElementsByTagName("project")
    diffCount = 0
    equalCount = 0
    if (len(oldProjects) != len(newlyProjects)):
        print("len(oldProjects) != len(newlyProjects). exit")
        return
    # 如果不考虑两边顺序不一致的话：可以使用zip 然后操作
    two = zip(oldProjects, newlyProjects)
    for oldP, newlyP in two:
        oldName = oldP.getAttribute("name")
        newName = newlyP.getAttribute("name")
        oldRevision = oldP.getAttribute("revision")
        newlyRevision = newlyP.getAttribute("revision")
        if oldName == newName and oldRevision != newlyRevision:
            item = dict()
            diffCount += 1
            # print("diff:{}\t{}\tproject={}".format(oldRevision, newlyRevision, oldName))
            git_dir = os.path.join(codeGm12eDir, oldName)
            left = git_dir
            # print("git-dir={}".format(git_dir))
            os.chdir(git_dir)
            command = "git log {}..{}".format(oldRevision, newlyRevision)
            # print("#command=", command, "dir=", git_dir)
            # subprocess.Popen.encoding = 'utf-8'
            popen = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            origin_strB = popen.stdout.read()  # -- > 成为一个 bytes 字符串了
            origin_strs = str(origin_strB, encoding='utf-8')  # --> bytes 2 string
            # print(origin_strs)
            gitlogArr = origin_strs.splitlines()
            rights = list()
            for s in gitlogArr:
                # print(bs)  # 这个 s 是一个单行的string !
                # s = str(bs, encoding='utf-8')  # --> bytes 2 string
                # print(s)  # 这个 s 是一个单行的string !
                if s.startswith("commit "):
                    commitID = s[len("commit "):]  # 获取 commit id 成功
                    rights.append(commitID)
                    # print("git-dir={}".format(git_dir))
                    # print("--------------commit:", commitID)
            item[left] = rights
            ret_list.append(item)
        else:
            equalCount += 1
    print("all={}\tdiff={}\tequal={}".format((diffCount + equalCount), diffCount, equalCount))
    # print("ret====", ret_list)
    return ret_list


def diffCommitMsgMixed(oldPath, newlyPath, codeGm12eDir):
    """
    获取 diff 信息并存入 list中
    :param oldPath: 对比文件的 旧路径
    :param newlyPath: 对比文件的 新路径
    :param codeGm12eDir: 代码路径根目录
    :return: dict_list: [{"path01":[ci01,ci02]},{"path02":[ci01,ci02,..]},...]
    """
    ret_list = list()

    oldDom = xml.dom.minidom.parse(oldPath)
    newlyDom = xml.dom.minidom.parse(newlyPath)
    oldProjects = oldDom.getElementsByTagName("project")
    newlyProjects = newlyDom.getElementsByTagName("project")
    diffCount = 0
    equalCount = 0
    if (len(oldProjects) != len(newlyProjects)):
        print("len(oldProjects) != len(newlyProjects). exit")
        return
    # 如果考虑两边顺序不一致的话：就只能使用原始的双层循环处理了
    # two = zip(oldProjects, newlyProjects)
    # for oldP, newlyP in two:
    for oldP in oldProjects:
        for newlyP in newlyProjects:
            oldName = oldP.getAttribute("name")
            newName = newlyP.getAttribute("name")
            oldRevision = oldP.getAttribute("revision")
            newlyRevision = newlyP.getAttribute("revision")
            if oldName == newName and oldRevision != newlyRevision:
                item = dict()
                diffCount += 1
                print("diff:{}\t{}\tproject={}".format(oldRevision, newlyRevision, oldName))
                git_dir = os.path.join(codeGm12eDir, oldName)
                left = git_dir
                # print("git-dir={}".format(git_dir))
                os.chdir(git_dir)
                command = "git log {}..{}".format(oldRevision, newlyRevision)
                # print("#command=", command, "dir=", git_dir)
                # subprocess.Popen.encoding = 'utf-8'
                popen = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                origin_strB = popen.stdout.read()  # -- > 成为一个 bytes 字符串了
                origin_strs = str(origin_strB, encoding='utf-8')  # --> bytes 2 string
                # print(origin_strs)
                gitlogArr = origin_strs.splitlines()
                rights = list()
                for s in gitlogArr:
                    # print(bs)  # 这个 s 是一个单行的string !
                    # s = str(bs, encoding='utf-8')  # --> bytes 2 string
                    # print(s)  # 这个 s 是一个单行的string !
                    if s.startswith("commit "):
                        commitID = s[len("commit "):]  # 获取 commit id 成功
                        rights.append(commitID)
                        # print("git-dir={}".format(git_dir))
                        # print("--------------commit:", commitID)
                item[left] = rights
                ret_list.append(item)
            elif oldName == newName and oldRevision == newlyRevision:
                equalCount += 1
    print("all={}\tdiff={}\tequal={}".format((diffCount + equalCount), diffCount, equalCount))
    # print("ret====", ret_list)
    return ret_list


def show_diff(dict_list):
    """
    显示diff 信息
    :param dict_list: [{"path01":[ci01,ci02]},{"path02":[ci01,ci02,..]},...]
    :return: void
    """
    for dict_item in dict_list:
        # ss = set()
        # ss.pop()
        git_dir = list(dict_item.keys())[0]
        commits = dict_item.get(git_dir, [])
        print("git-dir={}".format(git_dir))
        for ci in commits:
            print("-------commit:{}".format(ci))
        else:
            print()


if "__main__" == __name__:
    local = False
    gm12e = r'Z:\dailybuild\aus6797_6m_n\GM12E_7.1_mtk6797_dev_171016'
    oldPath = r'2018-01-11-05-15-01.xml'
    newlyPath = r'2018-01-15-05-15-01.xml'
    if not local:
        oldPath = r"2018-01-11-06-36-50_userdebug\2018-01-11-05-15-01.xml"  # 20180114
        newlyPath = r"2018-01-15-06-37-59_userdebug\2018-01-15-05-15-01.xml"  # 20180115
        oldPath = os.path.join(gm12e, oldPath)
        newlyPath = os.path.join(gm12e, newlyPath)

    # oldPath=r'2018-01-11-05-15-01.xml'
    # newlyPath=r'2018-01-15-05-15-01.xml'
    print("oldPath=\t{}\nnewlyPath=\t{}\n".format(oldPath, newlyPath))
    if os.path.isfile(oldPath) and os.path.isfile(newlyPath):
        # codeGm12eDir = r'X:\codes\gm12e'  # todo: git 根目录如何解决？
        commit_msg = diffCommitMsgMixed(oldPath=oldPath, newlyPath=newlyPath, codeGm12eDir=r'X:\codes\gm12e')
        # show_diff(commit_msg)
    else:
        print("file not exists...?",os.path.isfile(oldPath),"#",os.path.isfile(newlyPath))
        print(oldPath, newlyPath, sep="\n")
