# -*- coding: utf-8 -*-

import os
import random
import shutil

if __name__ == "__main__":
    pathDir = '/home/zhangch/RSS/5s/train_labelpng/'
    #pathDir2 = '/home/zhangch/Desktop/tmRNA/train_labelpng2/'
    filelist = os.listdir(pathDir)
    filepointlist = []
    label_0_num = 0
    label_2_num = 0
    label_1_num = 0
    for i in filelist:
        if i.split('.')[0] == '0':
            label_0_num = label_0_num + 1
        elif i.split('.')[0] == '1':
            label_1_num = label_1_num + 1
        else:
            label_2_num = label_2_num + 1
            filepointlist.append(i)
    """
    y = list(range(len(filepointlist)))
    slice = random.sample(y,label_2_num - label_0_num)
    for i in range(label_2_num - label_0_num):
        shutil.copyfile(pathDir + filepointlist[slice[i]] , pathDir2 + filepointlist[slice[i]])
        os.remove(pathDir + filepointlist[slice[i]])
    """
    
            