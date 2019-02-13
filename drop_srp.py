# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:15:31 2018

@author: zhangch
"""


import os

path_dir = "/media/disk/zhangch/RSS/train_set_up/"

if __name__ == "__main__":
    pathDir =  os.listdir(path_dir)
    for i in pathDir:
        if 'srp' in i:
            os.remove(path_dir + i)
               