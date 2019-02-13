#!'/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:18:17 2018

@author: zhangch
"""

import os
import numpy as np
import tensorflow as tf
import input_data
import model
    
N_CLASSES = 3
IMG_W = 128
IMG_H = 19
BATCH_SIZE = 256
CAPACITY = 1000
MAX_STEP = 20001
learning_rate = 0.01

def run_training():
    train_dir = '/home/zhangch/RSS/train_set/'
    logs_train_dir = '/home/zhangch/RSS/log/'
    
    train,train_label = input_data.get_files(train_dir)
    
    train_batch,train_label_batch = input_data.get_batch(train,
                                                         train_label,
                                                         IMG_W,
                                                         IMG_H,
                                                         BATCH_SIZE,
                                                         CAPACITY)
    train_logits = model.inference(train_batch,BATCH_SIZE,N_CLASSES)
    train_loss = model.losses(train_logits,train_label_batch)
    train_op = model.trainning(train_loss,learning_rate)
    train_acc = model.evalution(train_logits,train_label_batch)
    
    summary_op = tf.summary.merge_all()
    sess = tf.Session()
    train_writer = tf.summary.FileWriter(logs_train_dir,sess.graph)
    saver = tf.train.Saver(max_to_keep=2100)
    
    sess.run(tf.global_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess,coord = coord)
    
    try:
        for step in np.arange(MAX_STEP):
            if coord.should_stop():
                break
            _,tra_loss,tra_acc = sess.run([train_op,train_loss,train_acc])
            
            if step % 100 == 0:
                print("Step %d,train loss = %.2f,train accuracy = %.2f" %(step,tra_loss,tra_acc))
                summary_str = sess.run(summary_op)
                train_writer.add_summary(summary_str,step)
                
            if step % 200 == 0 or (step + 1) == MAX_STEP:
                checkpoin_path = os.path.join(logs_train_dir,'model.ckpt')
                saver.save(sess,checkpoin_path,global_step = step)
                
    except tf.errors.OutOfRangeError:
        print('Done train')
    finally:
        coord.request_stop()
        
    coord.join(threads)
    sess.close()

run_training()
