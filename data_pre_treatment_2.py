#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:41:57 2018

@author: zhangch
"""

import os
import pandas as pd
import csv


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
    rnaseq = data.loc[:,1]
    rnadata1 = data.loc[:,0]
    rnadata2 = data.loc[:,4]
    rnastructure = []
    for i in range(len(rnadata2)):
        if rnadata2[i] == 0:
            rnastructure.append(".")
        else:
            if rnadata1[i] > rnadata2[i]:
                rnastructure.append(")")
            else:
                rnastructure.append("(")
    return rnaseq,rnastructure,filename

def savefile(rnaseq,rnastructure,filename):
    rnafile = filename[:-3]
    rnafile = rnafile+".csv"
    rnafile = csv_Dir + rnafile
    rnacsv = open(rnafile,'wb')
    writer = csv.writer(rnacsv)
    m = len(rnastructure)
    for i in range(m):
        writer.writerow(rnastructure[i])
    os.remove("test.txt")
    rnaseqfile = seq_Dir + filename[:-3] + "_seq.csv"
    rnaseqcsv = open(rnaseqfile,'wb')
    seqwriter = csv.writer(rnaseqcsv)
    m = len(rnastructure)
    for i in range(m):
        seqwriter.writerow(rnaseq[i])
    
list_Dir = '/home/zhangch/RNASecondStructure/source_data_2/' 
csv_Dir = '/home/zhangch/RNASecondStructure/stru_data/' 
seq_Dir = '/home/zhangch/RNASecondStructure/seq_data/' 
   
if __name__ == '__main__':
    pathDir =  os.listdir(list_Dir)
    for i in pathDir:
        data,filename=readfile(list_Dir , i)
        rnaseq,rnastructure,filename=transform(data,filename)
        savefile(rnaseq,rnastructure,filename)
    