# -*- coding: utf-8 -*-
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:34:53 2018

@author: zhangch
"""

import os
import numpy as np
import shutil

def get_one_file(png_datas):
    path = os.listdir(png_datas)
    ind = np.random.randint(0,len(path),1)
    return path[int(ind)]

png_datas = '/home/zhangch/RSS/train_labelpng/'
balance_data = '/home/zhangch/RSS/validation_set/'
if __name__ == "__main__":
    countsum = 0
    count0 = count1 = count2 = 0
    while countsum < 30000:
        filename = get_one_file(png_datas)
        if filename.startswith("0"):
            if count0 <10000:
                count0 = count0 + 1
                countsum = countsum + 1
                shutil.copy(png_datas + filename,balance_data + filename)
                os.remove(png_datas + filename)
        if filename.startswith("1"):
            if count1 <10000:
                count1 = count1 + 1
                countsum = countsum + 1
                shutil.copy(png_datas + filename,balance_data + filename)
                os.remove(png_datas + filename)
        if filename.startswith("2"):
            if count2 <10000:
                count2 = count2 + 1
                countsum = countsum + 1
                shutil.copy(png_datas + filename,balance_data + filename)
                os.remove(png_datas + filename)
        print count0,count1,count2,countsum