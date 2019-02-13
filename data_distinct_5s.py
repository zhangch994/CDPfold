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

def distinct(list_dis,string):
    flag = False
    if string not in list_dis:
        flage = True
        for i in list_dis:
            if string in i:
                flage = False
        if flage == True:
            list_dis.append(string)
            flag = True
    return flag,list_dis

#path_dir = "/home/zhangch/RSS/stru_data/"
path_dir = "/home/zhangch/RSS/seq_data/"
save_dir = "/home/zhangch/RSS/train_seq_data/"
stru_path_dir = "/home/zhangch/RSS/stru_data/"
stru_save_dir = "/home/zhangch/RSS/train_stru_data/"
if __name__ == "__main__":
    path = os.listdir(path_dir)
    
    dict1 = {}
    for i in path:
        #if i.endswith(".csv"):
        data,filename = readfile(path_dir , i)
        dict1[filename] = len(data)
    dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)
    pathdir = []
    for i in range(len(dict2)):
        pathdir.append(dict2[i][0])
    #df = pd.DataFrame()
    #max_data = 0
    list_dis = []
    for i in pathdir:
        #filename1 = dict2[i][0]
        #if i.endswith(".csv"):
        data,filename = readfile(path_dir , i)
        string = ''
        for i in range(len(data)):
            string = string + data[i][0]
        flag,list_dis = distinct(list_dis,string)
        if flag == True:
            shutil.copyfile(path_dir + filename , save_dir + filename)
            filename2 = filename[:-8] + '.csv'
            shutil.copyfile(stru_path_dir + filename2 , stru_save_dir + filename2)
            #if len(data) >= 100 and len(data)<200:
            #if i.startswith("5s"):
                 #shutil.copyfile(path_dir + i , save_dir + i)


