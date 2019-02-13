#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:36:01 2018

@author: zhangch
"""
import os
import pandas as pd
import csv

 # 遍历指定目录，显示目录下的所有文件名

def readfile(fileDir,filename):
    fopen = open(fileDir+filename,'r')
    rnafile = fopen.readlines()
    del rnafile[0]
    with open("test.txt",'w') as f:
        for i in range(len(rnafile)):
            s = rnafile[i]
            result = '\t'.join(s.split())
            result = result +"\n"
            f.write(result)
    data = pd.read_csv("test.txt", sep='\t', header=None)
    return data,filename

def transform(data,filename):
    rnadata1 = data.loc[:,0]
    rnadata2 = data.loc[:,4]
    flag = False
    for i in range(len(rnadata2)):
        for j in range(len(rnadata2)):
            if (rnadata1[i] < rnadata1[j] < rnadata2[i] < rnadata2[j]):
                flag = True
                break
    return flag

list_Dir = '/home/zhangch/Desktop/test1/' 

if __name__ == '__main__':
    pathDir =  os.listdir(list_Dir)
    for i in pathDir:
        data,filename=readfile(list_Dir , i)
        flag = transform(data,filename)
        if flag:
            os.remove(list_Dir + i)
    