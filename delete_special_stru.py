# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:15:31 2018

@author: zhangch
"""

from __future__ import division
import os
import pandas as pd
import csv
import shutil

def readfile(path_dir,file):
    filename = path_dir + file
    csvFile = open(filename,"r")
    reader = csv.reader(csvFile)
    data = []
    for item in reader:
        data.append(item)
    return data,file

path_dir = "/home/zhangch/RSS/srp/train_seq_data/"
path_dir2 = "/home/zhangch/RSS/srp/train_stru_data/"
save_dir = "/home/zhangch/RSS/special_data/"
if __name__ == "__main__":
    path = pathDir =  os.listdir(path_dir)
    df = pd.DataFrame()
    for i in pathDir:
        j = i[:-8] + '.csv'
        if i.endswith(".csv"):
            if '10' in i:
                os.remove(path_dir + i)
                os.remove(path_dir2 + j)
            if '11' in i:
                os.remove(path_dir + i)
                os.remove(path_dir2 + j)
            if '12' in i:
                os.remove(path_dir + i)
                os.remove(path_dir2 + j)
            if '13' in i:
                os.remove(path_dir + i)
                os.remove(path_dir2 + j)
            if '14' in i:
                os.remove(path_dir + i)
                os.remove(path_dir2 + j)
            if '15' in i:
                os.remove(path_dir + i)
                os.remove(path_dir2 + j)
            if '16' in i:
                os.remove(path_dir + i)
                os.remove(path_dir2 + j)
            if '17' in i:
                os.remove(path_dir + i)
                os.remove(path_dir2 + j)