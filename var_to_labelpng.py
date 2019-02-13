# -*- coding: utf-8 -*-
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:20:23 2018

@author: zhangch
"""

from __future__ import division
import os
import numpy as np
import csv
import math
import scipy.misc


def Gaussian(x):
    return math.exp(-0.5*(x*x))

def paired(x,y):
    if x == ['A'] and y == ['U']:
        return 2
    elif x == ['G'] and y == ['C']:
        return 3
    elif x == ["G"]and y == ['U']:
        return 0.8
    elif x == ['U'] and y == ['A']:
        return 2
    elif x == ['C'] and y == ['G']:
        return 3
    elif x == ["U"]and y == ['G']:
        return 0.8
    else:
        return 0

def readfile(path_dir,file):
    filename = path_dir + file
    csvFile = open(filename,"r")
    reader = csv.reader(csvFile)
    data = []
    for item in reader:
        data.append(item)
    return data,file

def creatmat(data):
    mat = np.zeros([len(data),len(data)])
    for i in range(len(data)):
        for j in range(len(data)):
            coefficient = 0
            for add in range(30):
                if i - add >= 0 and j + add <len(data):
                    score = paired(data[i - add],data[j + add])
                    if score == 0:
                        break
                    else:
                        coefficient = coefficient + score * Gaussian(add)
                else:
                    break
            if coefficient > 0:
                for add in range(1,30):
                    if i + add < len(data) and j - add >= 0:
                        score = paired(data[i + add],data[j - add])
                        if score == 0:
                            break
                        else:
                            coefficient = coefficient + score * Gaussian(add)
                    else:
                        break
            mat[[i],[j]] = coefficient
    return mat

def complete(i):
    if i < 10:
        str1 = '00' + str(i)
    elif i <100:
        str1 = '0' + str(i)
    else:
        str1 = str(i)
    return str1

def change(x):
    if x == ['(']:
        return 0
    elif x == [')']:
        return 1
    else:
        return 2

def jiaoyan(data):
    num_0 = num_1 =num_2 = 0
    for i in range(len(data)):
        if data[i][0] == '(':
            num_0 = num_0 + 1
        elif data[i][0] == ')':
            num_1 = num_1 + 1
        else:
            num_2 = num_2 + 1
        if num_1 == num_0:
            return True
        else:
            return False
    

seq_dir = '/home/zhangch/RSS/ver_seq_data/'
str_dir = '/home/zhangch/RSS/ver_stru_data/'
png_dir = '/home/zhangch/RSS/ver_labelpng/' 
                   
if __name__ == "__main__":
    pathDir =  os.listdir(seq_dir)
    pathDir.sort()
    length = len(pathDir)
    for i in range(length):
        filename = pathDir[i]
        filename2 = filename[:-8] + '.csv'
        data,file = readfile(seq_dir , filename)
        data2,file2 = readfile(str_dir,filename2)
        if jiaoyan(data):
            im = np.zeros([len(data)+19,len(data),3])
            mat = creatmat(data)
            im[9:len(data)+9,0:len(data),0] = im[9:len(data)+9,0:len(data),0] + mat 
            for j in range(len(data)):
                pic = im[j:j+19]
                new_filename=png_dir+str(change(data2[j]))+'.'+file[:-4] +'_'+complete(j) + '.png'
                scipy.misc.imsave(new_filename, pic)
        else:
            print file
