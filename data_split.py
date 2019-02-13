import os
import random
import shutil

stru_dir = '/home/zhangch/Desktop/tRNA/train_stru_data/'
seq_dir = '/home/zhangch/Desktop/tRNA/train_seq_data/'

t_stru_dir = '/home/zhangch/Desktop/tRNA/test_stru_data/'
t_seq_dir = '/home/zhangch/Desktop/tRNA/test_seq_data/'

if __name__ == '__main__':
    pathDir = os.listdir(stru_dir)
    pathDir.sort()
    pathDir2 = os.listdir(seq_dir)
    pathDir2.sort()
    y = list(range(len(pathDir)))
    slice1 = random.sample(y,48)
    for i in range(48):
        shutil.copyfile(stru_dir + pathDir[slice1[i]] , t_stru_dir + pathDir[slice1[i]])
        shutil.copyfile(seq_dir + pathDir2[slice1[i]] , t_seq_dir + pathDir2[slice1[i]])
        os.remove(stru_dir + pathDir[slice1[i]])
        os.remove(seq_dir + pathDir2[slice1[i]])

