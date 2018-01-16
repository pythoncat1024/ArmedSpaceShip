# -*- coding: utf-8 -*-
import xml.dom.minidom
import os
import subprocess


def diffCommitMsg(oldPath, newlyPath):
    oldDom = xml.dom.minidom.parse(oldPath)
    newlyDom = xml.dom.minidom.parse(newlyPath)
    oldProjects = oldDom.getElementsByTagName("project")
    newlyProjects = newlyDom.getElementsByTagName("project")
    diffCount = 0
    equalCount = 0
    if (len(oldProjects) != len(newlyProjects)):
        print("len(oldProjects) != len(newlyProjects). exit")
        return
    two = zip(oldProjects, newlyProjects)
    for oldP, newlyP in two:
        # for newlyP in newlyProjects:
        # oldP = oldProjects
        # newlyP = newlyProjects
        oldName = oldP.getAttribute("name")
        newName = newlyP.getAttribute("name")
        oldRevision = oldP.getAttribute("revision")
        newlyRevision = newlyP.getAttribute("revision")
        if oldName == newName and oldRevision != newlyRevision:
            diffCount += 1
            # print("diff:{}\t{}\tproject={}".format(oldRevision, newlyRevision, oldName))
            codeGm12eDir = r'X:\codes\gm12e'
            git_dir = os.path.join(codeGm12eDir, oldName)
            # print("git-dir={}".format(git_dir))
            os.chdir(git_dir)
            command = "git log {}..{}".format(oldRevision, newlyRevision)
            print("#command=", command, "dir=", git_dir)
            # subprocess.Popen.encoding = 'utf-8'
            popen = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

            # popen._stream.
            # print("------------1---111---")

            origin_strs = popen.stdout.read()  # -- > 成为一个 bytes 字符串了
            # print(origin_strs)
            # print("------------2---222---")
            gitlogArr = origin_strs.splitlines()
            for bs in gitlogArr:
                # print(bs)  # 这个 s 是一个单行的string !
                s = str(bs, encoding='utf-8')  # --> bytes 2 string
                # print(s)  # 这个 s 是一个单行的string !
                if s.startswith("commit "):
                    commitID = s[len("commit "):]  # 获取 commit id 成功
                    # print("git-dir={}".format(git_dir))
                    print("--------------commit:", commitID)
        else:
            equalCount += 1
    print("all={}\tdiff={}\tequal={}".format((diffCount + equalCount), diffCount, equalCount))


if "__main__" == __name__:
    print("xxxx")
    gm12e = r'Z:\dailybuild\aus6797_6m_n\GM12E_7.1_mtk6797_dev_171016'
    oldPath = r"2018-01-11-06-36-50_userdebug\2018-01-11-05-15-01.xml"  # 20180114
    newlyPath = r"2018-01-15-06-37-59_userdebug\2018-01-15-05-15-01.xml"  # 20180115
    oldPath = os.path.join(gm12e, oldPath)
    newlyPath = os.path.join(gm12e, newlyPath)

    print("oldPath={}\nnewlyPath={}\n".format(oldPath, newlyPath))
    if os.path.isfile(oldPath) and os.path.isfile(newlyPath):
        diffCommitMsg(oldPath=oldPath, newlyPath=newlyPath)
    else:
        print("file not exists...")
        print(oldPath, newlyPath, sep="\n")
