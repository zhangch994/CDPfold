# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def paired(x,y):
    if x == 'A' and y == 'U':
        return True
    elif x == 'G' and y == 'C':
        return True
    elif x == "G"and y == 'U':
        return True
    elif x == 'U' and y == 'A':
        return True
    elif x == 'C' and y == 'G':
        return True
    elif x == "U"and y == 'G':
        return True
    else:
        return False

def main(seq_path,seqfilename):
    seqfile = pd.read_csv(seq_path + seqfilename,names=['label'])
    probability = pd.read_csv('test.csv')
    result = pd.concat([seqfile,probability[['left','right','point']]],axis=1)
    row = result.iloc[:,0].size
    array1 = np.zeros([row,row])
    array = [None]*(row)*(row)
    array2 = np.array(array)
    array2.resize(row,row)
    for j in range(0,row):
        array2[j,j] = '.'
    for j in range(1,row):
        array2[j,j-1] = ''
    for add in range(1,row):# zengliang
        for i in range(0,row - add):
            maxset = 0
            maxpoint = 0
            if add > 1:
                for k in range(i+1,i+add):
                    if array1[i,k]+array1[k+1,i+add] > maxset:
                        maxset = array1[i,k]+array1[k+1,i+add]
                        maxpoint = k
            kind1 = array1[i+1,i+add]+result['point'][i]
            kind2 = array1[i,i+add-1]+result['point'][i+add]
            pair = 0
            if paired(result['label'][i],result['label'][i+add]):
                kind3 = array1[i+1,i+add-1]+result['left'][i]+result['right'][i+add]
                pair = 1
            else:
                kind3 = array1[i+1,i+add-1]+result['point'][i]+result['point'][i+add]
            kind4 = maxset
            array1[i,i+add] = max(kind1,kind2,kind3,kind4)
            if array1[i,i+add] == kind1:
                array2[i,i+add] = '.'+ array2[i+1,i+add]
            elif array1[i,i+add] == kind2:
                array2[i,i+add] = array2[i,i+add-1] + '.'
            elif array1[i,i+add] == kind3 and pair == 1:
                array2[i,i+add] = '(' + array2[i+1,i+add-1] + ')'
            elif array1[i,i+add] == kind3 and pair == 0:
                array2[i,i+add] = '.' + array2[i+1,i+add-1] + '.'
            else:
                array2[i,i+add] = array2[i,maxpoint]+array2[maxpoint+1,i+add]
    
    deal = []
    for i in array2[0,row-1]:
        if i is not '0':
            deal.append(i)
    return deal