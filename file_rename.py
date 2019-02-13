# -*- coding: utf-8 -*-

import os

file_dir = '/home/zhangch/RSS/5s/train_labelpng2/'

filelist = os.listdir(file_dir)
for i in filelist:
    new_name = i[:-4] + 'copy1' + '.png'
    os.rename(file_dir + i,file_dir + new_name)
    
