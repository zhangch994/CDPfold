# -*- coding: utf-8 -*-

import os
import random
import shutil

if __name__ == "__main__":
    pathDir = '/home/zhangch/RSS/5s/train_labelpng/'
    pathDir2 = '/home/zhangch/RSS/5s/train_labelpng2/'
    filelist = os.listdir(pathDir)
    filepointlist = []
    fileleftlist = []
    filerightlist = []
    label_0_num = 0
    label_2_num = 0
    label_1_num = 0
    for i in filelist:
        if i.split('.')[0] == '0':
            label_0_num = label_0_num + 1
            fileleftlist.append(i)
        elif i.split('.')[0] == '1':
            label_1_num = label_1_num + 1
            filerightlist.append(i)
        else:
            label_2_num = label_2_num + 1
            filepointlist.append(i)
    y = list(range(len(fileleftlist)))
    slicey = random.sample(y,18991)
    for i in range(18991):
        shutil.copyfile(pathDir + fileleftlist[slicey[i]] , pathDir2 + fileleftlist[slicey[i]])
    z = list(range(len(filerightlist)))
    slicez = random.sample(z,18991)
    for i in range(18991):
        shutil.copyfile(pathDir + filerightlist[slicez[i]] , pathDir2 + filerightlist[slicez[i]])
        