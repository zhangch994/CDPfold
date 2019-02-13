#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:51:06 2018

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

path_dir = "/home/zhangch/RSS/stru_data/"
save_dir = "/home/zhangch/RSS/5s_stru_data/"
if __name__ == "__main__":
    path = pathDir =  os.listdir(path_dir)
    df = pd.DataFrame()
    max_data = 0
    for i in pathDir:
        if i.endswith(".csv"):
            #data,filename = readfile(path_dir , i)
            #if len(data) >= 100 and len(data)<200:
            if i.startswith("srp"):
                 shutil.copyfile(path_dir + i , save_dir + i)


