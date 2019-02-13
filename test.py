# -*- coding: utf-8 -*-

import os
import train_to_labelpng
import numpy as np
import scipy.misc
from PIL import Image
import validation_one_base
import shutil
import pandas as pd

seq_path = '/home/zhangch/RSS/test/test_seq_data/'
png_path = '/home/zhangch/RSS/test/test_labelpng/'
testset_path = '/home/zhangch/RSS/test/test_set/'
test_one_path = '/home/zhangch/RSS/test/test_one_base/'

seqDir =  os.listdir(seq_path)


prediction_list = []
seq_data,seqfilename = train_to_labelpng.readfile(seq_path,seqDir[0])
im = np.zeros([len(seq_data)+19,len(seq_data),3])
mat = train_to_labelpng.creatmat(seq_data)
im[9:len(seq_data)+9,0:len(seq_data),0] = im[9:len(seq_data)+9,0:len(seq_data),0] + mat 
for j in range(len(seq_data)):
    pic = im[j:j+19]
    new_filename = png_path + seqfilename[:-4] +'_'+train_to_labelpng.complete(j) + '.png'
    scipy.misc.imsave(new_filename, pic)
pngDir = os.listdir(png_path)
for k in pngDir:
    image = Image.open(png_path+k)
    image = image.resize((128,19))
    scipy.misc.imsave(testset_path+k, image)
testDir = os.listdir(testset_path)
testDir.sort()
for l in testDir:
    shutil.copyfile(testset_path + l , test_one_path + l)
    prediction = validation_one_base.evaluate()
    prediction_new = [prediction[0][0][0],prediction[0][0][1],prediction[0][0][2]]
    prediction_list.append(prediction_new)
    os.remove(test_one_path + l)
name = ['left','right','point']
test = pd.DataFrame(columns=name,data=prediction_list)
test.to_csv('test.csv')
test2 = pd.read_csv('test.csv')
