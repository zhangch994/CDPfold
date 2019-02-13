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


def readfile(path_dir,file):
    filename = path_dir + file
    csvFile = open(filename,"r")
    reader = csv.reader(csvFile)
    data = []
    for item in reader:
        data.append(item)
    return data,file

path_dir = "/home/zhangch/Desktop/tRNA/train_seq_data/"
save_dir = "/home/zhangch/RSS/special_data/"
if __name__ == "__main__":
    pathDir =  os.listdir(path_dir)
    df = pd.DataFrame()
    for i in pathDir:
        if i.endswith(".csv"):
            data,filename = readfile(path_dir , i)
            if len(data) <= 74 or len(data)>=78:
               os.remove(path_dir + i)
               