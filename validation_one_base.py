# -*- coding: utf-8 -*-

import tensorflow as tf
import input_data
import model


N_CLASSES = 3
IMG_W = 192
IMG_H = 19
BATCH_SIZE = 1
CAPACITY = 1000


def evaluate():
    with tf.Graph().as_default():
        logs_train_dir = '/home/zhangch/RSS/log/'
        verification_dir = "/home/zhangch/RSS/test/test_one_base/"
        n_test = 1
        train,train_label = input_data.get_files(verification_dir)
        train_batch,train_label_batch = input_data.get_batch(train,
                                                         train_label,
                                                         IMG_W,
                                                         IMG_H,
                                                         BATCH_SIZE,
                                                         CAPACITY)
        logit = model.inference(train_batch,BATCH_SIZE,N_CLASSES)
        softmax = tf.nn.softmax(logit,dim=-1,name=None)
        #top_k_op = tf.nn.in_top_k(logit,train_label_batch,1)       
        saver = tf.train.Saver(tf.global_variables())
        with tf.Session() as sess:
            
            print("Reading checkpoints...")
            ckpt = tf.train.get_checkpoint_state(logs_train_dir)
            if ckpt and ckpt.model_checkpoint_path:
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                saver.restore(sess,ckpt.model_checkpoint_path)
                print("Loading success,global_step is %s" % global_step)
            else:
                print("no checkpoint file found")
                
            coord = tf.train.Coordinator()
            threads = tf.train.start_queue_runners(sess=sess,coord = coord)
            
            try:
                num_iter = int(n_test/BATCH_SIZE)
                #true_count = 0
                #total_sample_count = num_iter * BATCH_SIZE
                step = 0
                
                while step < num_iter and not coord.should_stop():
                    prediction = sess.run([softmax])
                    step += 1
                    return prediction
            except Exception as e:
                coord.request_stop(e)
            finally:
                coord.request_stop()
                coord.join(threads)
