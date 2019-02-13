#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:15:50 2018

@author: zhangch
"""

import tensorflow as tf

def inference(images,batch_size,n_classes):
    """Build the model
    Args:
        image:image batch ,4D tensor, tf.float32,[batch_size,width,height,channels]
    Return:
        output tensor with the computed logits,float,[batch_size,n_classes]
    """
    #conv1
    with tf.variable_scope('conv1') as scope:
        weights = tf.get_variable('weights',
                                 shape = [3,3,3,16],
                                 dtype = tf.float32,
                                 initializer = tf.truncated_normal_initializer(stddev = 0.1,dtype = tf.float32))
        biases = tf.get_variable('biases',
                                 shape = [16],
                                 dtype = tf.float32,
                                 initializer = tf.constant_initializer(0.1))
        conv = tf.nn.conv2d(images,weights,strides = [1,1,1,1],padding = 'SAME')
        pre_activation = tf.nn.bias_add(conv,biases)
        conv1 = tf.nn.relu(pre_activation,name = scope.name)
        
    with tf.variable_scope('pooling1_lrn') as scope:
        pool1 = tf.nn.avg_pool(conv1,ksize = [1,3,3,1],strides = [1,1,1,1],
                               padding = 'SAME',name = 'pooling1')
        norm1 = tf.nn.local_response_normalization(pool1,depth_radius=4,bias = 1.0,alpha = 0.001/9.0,
                                                   beta = 0.75,name = 'norm1')
        
    #conv2
    with tf.variable_scope('conv2') as scope:
        weights = tf.get_variable('weights',
                                 shape = [3,3,16,16],
                                 dtype = tf.float32,
                                 initializer = tf.truncated_normal_initializer(stddev = 0.1,dtype = tf.float32))
        biases = tf.get_variable('biases',
                                 shape = [16],
                                 dtype = tf.float32,
                                 initializer = tf.constant_initializer(0.1))
        conv = tf.nn.conv2d(norm1,weights,strides = [1,1,1,1],padding = 'SAME')
        pre_activation = tf.nn.bias_add(conv,biases)
        conv2 = tf.nn.relu(pre_activation,name = scope.name)
        
    with tf.variable_scope('pooling2_lrn') as scope:
        norm2 = tf.nn.local_response_normalization(conv2,depth_radius=4,bias = 1.0,alpha = 0.001/9.0,
                                                   beta = 0.75,name = 'norm2')
        pool2 = tf.nn.avg_pool(norm2,ksize = [1,3,3,1],strides = [1,1,1,1],
                               padding = 'SAME',name = 'pooling2')
    #conv3
    """
    with tf.variable_scope('conv3') as scope:
        weights = tf.get_variable('weights',
                                 shape = [3,3,16,16],
                                 dtype = tf.float32,
                                 initializer = tf.truncated_normal_initializer(stddev = 0.1,dtype = tf.float32))
        biases = tf.get_variable('biases',
                                 shape = [16],
                                 dtype = tf.float32,
                                 initializer = tf.constant_initializer(0.1))
        conv = tf.nn.conv2d(pool2,weights,strides = [1,1,1,1],padding = 'SAME')
        pre_activation = tf.nn.bias_add(conv,biases)
        conv3 = tf.nn.relu(pre_activation,name = scope.name)
        
    with tf.variable_scope('pooling3_lrn') as scope:
        norm3 = tf.nn.local_response_normalization(conv3,depth_radius=4,bias = 1.0,alpha = 0.001/9.0,
                                                   beta = 0.75,name = 'norm3')
        pool3 = tf.nn.avg_pool(norm3,ksize = [1,3,3,1],strides = [1,1,1,1],
                               padding = 'SAME',name = 'pooling3')
    #conv4
    
    with tf.variable_scope('conv4') as scope:
        weights = tf.get_variable('weights',
                                 shape = [3,3,16,16],
                                 dtype = tf.float32,
                                 initializer = tf.truncated_normal_initializer(stddev = 0.1,dtype = tf.float32))
        biases = tf.get_variable('biases',
                                 shape = [16],
                                 dtype = tf.float32,
                                 initializer = tf.constant_initializer(0.1))
        conv = tf.nn.conv2d(pool3,weights,strides = [1,1,1,1],padding = 'SAME')
        pre_activation = tf.nn.bias_add(conv,biases)
        conv4 = tf.nn.relu(pre_activation,name = scope.name)
        
    with tf.variable_scope('pooling4_lrn') as scope:
        norm4 = tf.nn.local_response_normalization(conv4,depth_radius=4,bias = 1.0,alpha = 0.001/9.0,
                                                   beta = 0.75,name = 'norm3')
        pool4 = tf.nn.avg_pool(norm4,ksize = [1,3,3,1],strides = [1,1,1,1],
                               padding = 'SAME',name = 'pooling4')
    """
    #conv5
    """
    with tf.variable_scope('conv5') as scope:
        weights = tf.get_variable('weights',
                                 shape = [3,3,16,16],
                                 dtype = tf.float32,
                                 initializer = tf.truncated_normal_initializer(stddev = 0.1,dtype = tf.float32))
        biases = tf.get_variable('biases',
                                 shape = [16],
                                 dtype = tf.float32,
                                 initializer = tf.constant_initializer(0.1))
        conv = tf.nn.conv2d(pool4,weights,strides = [1,1,1,1],padding = 'SAME')
        pre_activation = tf.nn.bias_add(conv,biases)
        conv5 = tf.nn.relu(pre_activation,name = scope.name)
        
    with tf.variable_scope('pooling5_lrn') as scope:
        norm5 = tf.nn.local_response_normalization(conv5,depth_radius=4,bias = 1.0,alpha = 0.001/9.0,
                                                   beta = 0.75,name = 'norm3')
        pool5 = tf.nn.avg_pool(norm5,ksize = [1,3,3,1],strides = [1,1,1,1],
                               padding = 'SAME',name = 'pooling5')
    """    
    with tf.variable_scope("local3") as scope:
        reshape = tf.reshape(pool2,shape = [batch_size, -1])
        dim = reshape.get_shape()[1].value
        weights = tf.get_variable("weights",
                                  shape = [dim,32],
                                  dtype = tf.float32,
                                  initializer = tf.truncated_normal_initializer(stddev = 0.005,dtype = tf.float32))
        biases = tf.get_variable('biases',
                                 shape = [32],
                                 dtype = tf.float32,
                                 initializer = tf.constant_initializer(0.1))
        local3 = tf.nn.relu(tf.matmul(reshape,weights) + biases,name = scope.name)
        
    with tf.variable_scope("local4") as scope:
        weights = tf.get_variable("weights",
                                  shape = [32,32],
                                  dtype = tf.float32,
                                  initializer = tf.truncated_normal_initializer(stddev = 0.005,dtype = tf.float32))
        biases = tf.get_variable('biases',
                                 shape = [32],
                                 dtype = tf.float32,
                                 initializer = tf.constant_initializer(0.1))
        local4 = tf.nn.relu(tf.matmul(local3,weights) + biases,name = 'local4')
        
    with tf.variable_scope('softmax_linear') as scope:
        weights = tf.get_variable('softmax_linear',
                                  shape = [32,n_classes],
                                  dtype = tf.float32,
                                  initializer = tf.truncated_normal_initializer(stddev = 0.005,dtype = tf.float32))
        biases = tf.get_variable('biases',
                                 shape = [n_classes],
                                 dtype = tf.float32,
                                 initializer = tf.constant_initializer(0.1))
        softmax_linear = tf.add(tf.matmul(local4,weights),biases,name = 'softmax_linear')
        
    return softmax_linear

def losses(logits,labels):
    with tf.variable_scope('loss') as scope:
        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits = logits,labels = labels,name = 'xentropy_per_example')
        loss = tf.reduce_mean(cross_entropy,name = 'loss')
        tf.summary.scalar(scope.name + '/loss',loss)
    return loss

def trainning(loss,learning_rate):
    with tf.name_scope('optimizer'):
        optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate)
        global_step = tf.Variable(0,name = 'global_step',trainable = False)
        train_op = optimizer.minimize(loss,global_step = global_step)
    return train_op

def evalution(logits,labels):
    with tf.variable_scope('accuracy') as scope:
        correct = tf.nn.in_top_k(logits,labels,1)
        correct= tf.cast(correct,tf.float32)
        accuracy = tf.reduce_mean(correct)
        tf.summary.scalar(scope.name + '/accuracy',accuracy)
    return accuracy
