#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:13:20 2018

@author: zhangch
"""
import tensorflow as tf
import numpy as np
import os
"""
image_widht = 135/201
image_height = 13/201

train_dir = "/home/zhangch994/RNA/test_data/"
"""
def get_files(file_dir):
    """
    Args:
        file_dir:file directtory
    Returns:
        list of images and labels
    """
    left_bracket = []
    label_left_bracket = []
    right_bracket = []
    label_right_bracket = []
    point = []
    label_point = []
    for file in os.listdir(file_dir):
        name = file.split('.')
        if name[0] == '0':
            left_bracket.append(file_dir + file)
            label_left_bracket.append(0)
        elif name[0] == '1':
            right_bracket.append(file_dir + file)
            label_right_bracket.append(1)
        else:
            point.append(file_dir + file)
            label_point.append(2)
    print("There are %d left bracket\nThere are %d right bracket\nThere are %d point"  %(len(left_bracket),len(right_bracket),len(point)))
    
    image_list = np.hstack((left_bracket,right_bracket,point))
    label_list = np.hstack((label_left_bracket,label_right_bracket,label_point))
    
    temp = np.array([image_list,label_list])
    temp = temp.transpose()
    np.random.shuffle(temp)
    
    image_list = list(temp[:,0])
    label_list = list(temp[:,1])
    label_list = [int(float(i)) for i in label_list]
    
    return image_list, label_list


def get_batch(image,label,image_W,image_H,batch_size,capacity):
    """
    Args:
        image:list type
        label:list type
        image_W:image width
        image_H:image height
        batch_size:batch size
        capacity:the maximum elements in quene
    Returns:
        image_batch:4D tensor [batch_size,width,height,3],dtype = tf.float32
        label_batch:1D tensor [batch_size],dtype = tf.int32
    """
    image = tf.cast(image,tf.string)
    label = tf.cast(label,tf.int32)
    
    input_queue = tf.train.slice_input_producer([image,label])
    
    label = input_queue[1]
    image_contents = tf.read_file(input_queue[0])
    image = tf.image.decode_png(image_contents,channels = 3)
    
    #image = tf.image.resize_image_with_crop_or_pad(image,image_W,image_H)
    image.set_shape([19,128,3])#([13,135,3])
    image = tf.image.per_image_standardization(image)
    image_batch,label_batch = tf.train.batch([image,label],
                                             batch_size = batch_size,
                                             num_threads = 8,
                                             capacity = capacity)
    label_batch = tf.reshape(label_batch,[batch_size])
    return image_batch,label_batch


"""
import matplotlib.pyplot as plt

BATCH_SIZE = 2
CAPACITY = 256
IMG_W = 135
IMG_H = 13

train_dir = "/home/zhangch/RNA/png_data/"
image_list,label_list = get_files(train_dir)
image_batch,label_batch = get_batch(image_list,label_list,IMG_W,IMG_H,BATCH_SIZE,CAPACITY)

with tf.Session() as sess:
    i = 0
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord = coord)
    try:
        while not coord.should_stop() and i<1:
            img,label = sess.run([image_batch,label_batch])
            
            for j in np.arange(BATCH_SIZE):
                print("label:%d" %label[j])
                plt.imshow(img[j,:,:,:])
                plt.show()
            i+=1
    except tf.errors.OutOfRangeError:
        print('Done')
    finally:
        coord.request_stop()
    coord.join(threads)
"""    
