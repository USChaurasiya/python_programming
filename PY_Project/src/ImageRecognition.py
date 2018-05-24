import os
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from scipy.misc import imread
import pylab

import tensorflow as tf


seed = 128
rng = np.random.RandomState(seed)

root_dir = os.path.abspath('/home/uma/Desktop/ML-AI')
data_dir = os.path.join(root_dir, 'Data Set')
sub_dir = os.path.join(root_dir, '')

train = pd.read_csv(os.path.join(root_dir, data_dir, 'data.csv'))
test = pd.read_csv(os.path.join(root_dir, data_dir, 'test.csv'))

img_name = rng.choice(train.InputImage)
filepath = os.path.join(root_dir, data_dir, img_name)


img = imread(filepath, flatten=True)

temp = []
for img_name in train.InputImage:
    image_path = os.path.join(root_dir, data_dir, img_name)
    img = imread(image_path, flatten=True)
    img = img.astype('float32')
    temp.append(img)
pylab.imshow(img, cmap='gray')
pylab.axis('off')
pylab.show()
train_x = np.stack(temp)

temp = []

for img_name in test.InputImage:
    print(img_name)
    image_path = os.path.join(root_dir, data_dir, img_name)
    img = imread(image_path, flatten=True)
    img = img.astype('float32')
    temp.append(img)
pylab.imshow(img, cmap='gray')
pylab.axis()
pylab.show()
test_x = np.stack(temp)


split_size = int(train_x.shape[0]*0.7)
train_x, val_x = train_x[:split_size], train_x[split_size:]
train_y, val_y = train.label.values[:split_size], train.label.values[split_size:]



# #1143*220
# input_num_units = 1016*99
# hidden_num_units = 500
# output_num_units = 10
#
# # define placeholders
# x = tf.placeholder(tf.float32, [None, input_num_units])
# y = tf.placeholder(tf.float32, [None, output_num_units])
#
# # set remaining variables
# epochs = 5
# batch_size = 128
# learning_rate = 0.01
#
#
# weights = {
#     'hidden': tf.Variable(tf.random_normal([input_num_units, hidden_num_units], seed=seed)),
#     'output': tf.Variable(tf.random_normal([hidden_num_units, output_num_units], seed=seed))
# }
#
# biases = {
#     'hidden': tf.Variable(tf.random_normal([hidden_num_units], seed=seed)),
#     'output': tf.Variable(tf.random_normal([output_num_units], seed=seed))
# }
#
# hidden_layer = tf.add(tf.matmul(x, weights['hidden']), biases['hidden'])
# hidden_layer = tf.nn.relu(hidden_layer)
#
# output_layer = tf.matmul(hidden_layer, weights['output']) + biases['output']
#
#
# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=output_layer, labels=y))
# optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
# init = tf.initialize_all_variables()
#
#
#
#
#
# def dense_to_one_hot(labels_dense, num_classes=10):
#     """Convert class labels from scalars to one-hot vectors"""
#     num_labels = labels_dense.shape[0]
#     index_offset = np.arange(num_labels) * num_classes
#     labels_one_hot = np.zeros((num_labels, num_classes))
#
#     return labels_one_hot
#
#
# def preproc(unclean_batch_x):
#     """Convert values to range 0-1"""
#     temp_batch = unclean_batch_x / unclean_batch_x.max()
#     return temp_batch
#
# def batch_creator(batch_size, dataset_length, dataset_name):
#     """Create batch with random samples and return appropriate format"""
#     batch_mask = rng.choice(dataset_length, batch_size)
#
#     batch_x = eval(dataset_name + '_x')[[batch_mask]].reshape(-1, input_num_units)
#     batch_x = preproc(batch_x)
#
#     if dataset_name == 'train':
#         batch_y = eval(dataset_name).ix[batch_mask, 'label'].values
#         batch_y = dense_to_one_hot(batch_y)
#
#     return batch_x, batch_y
#
# with tf.Session() as sess:
#     # create initialized variables
#     sess.run(init)
#
#     for epoch in range(epochs):
#         avg_cost = 0
#         total_batch = int(train.shape[0] / batch_size)
#         for i in range(total_batch):
#             batch_x, batch_y = batch_creator(batch_size, train_x.shape[0], 'train')
#             _, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})
#
#             avg_cost += c / total_batch
#
#         print("Epoch:", (epoch + 1), "cost =", "{:.5f}".format(avg_cost))


