#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 可以加一个用时多久
# 还有打包备份的功能
# F:\studyFolder\React\rnDemo\android\app\build\outputs\apk可以删除这个

import os,shutil,datetime
hitname = "node_modules"    # 比较的名字
curdir = os.getcwd()    # 绝对路径
def getListFiles(path):
    # ret = [] 
    for root, dirs, files in os.walk(path):  
        for filespath in dirs: 
            if filespath == hitname:

                # ret.append(os.path.join(root,filespath)) 

                removeDir(os.path.join(root,filespath))
                # 可以优化
            else:
                pass
    # return ret

def removeDir(path):
    shutil.rmtree(path)
    print('*删除了： %s*' % path)

if __name__ == '__main__':
    print("******************警告！！！******************")
    print("当前文件夹： 【%s】" % curdir)

    ipt = input("*****************确认删除？[y]*****************\n")
    if ipt == 'y' or ipt == '':
        print("开始删除： %s 下的所有 %s 文件夹！" % (curdir, hitname))
        starttime=datetime.datetime.now()
        getListFiles(curdir)

        endtime=datetime.datetime.now()
        print("用时： %s 秒" % (endtime - starttime))
    else:
        print("用户取消: %s" % str(ipt))

    ipt = input("*****************按任意键退出！*****************\n")
    # getListFiles(curdir)
 
