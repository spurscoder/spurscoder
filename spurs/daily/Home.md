---
layout: post
title: "05.21到05.27.home"
author: "Spurs"
date: 2018-05-27 12:40:00
description:
photos:
links:
categories:
tags:
---

> 05.21到05.27.home
>

<!-- more -->

#### 05.23

##### tensorflow 中模型的保存与加载

我们在上线使用一个算法模型的时候，首先必须将已经训练好的模型保存下来。tensorflow保存模型的方式与sklearn不太一样，sklearn很直接，一个sklearn.externals.joblib的dump与load方法就可以保存与载入使用。而tensorflow由于有graph, operation 这些概念，保存与载入模型稍显麻烦。

一、基本方法

网上搜索tensorflow模型保存，搜到的大多是基本的方法。即

保存

1. 定义变量
2. 使用saver.save()方法保存

载入

1. 定义变量
2. 使用saver.restore()方法载入

如 **保存** 代码如下

```
import tensorflow as tf  
import numpy as np  

W = tf.Variable([[1,1,1],[2,2,2]],dtype = tf.float32,name='w')  
b = tf.Variable([[0,1,2]],dtype = tf.float32,name='b')  

init = tf.initialize_all_variables()  
saver = tf.train.Saver()  
with tf.Session() as sess:  
        sess.run(init)  
        save_path = saver.save(sess,"save/model.ckpt")
```

**载入**代码如下

```
import tensorflow as tf  
import numpy as np  

W = tf.Variable(tf.truncated_normal(shape=(2,3)),dtype = tf.float32,name='w')  
b = tf.Variable(tf.truncated_normal(shape=(1,3)),dtype = tf.float32,name='b')  

saver = tf.train.Saver()  
with tf.Session() as sess:  
        saver.restore(sess,"save/model.ckpt")
```

这种方法不方便的在于，在使用模型的时候，必须把模型的结构重新定义一遍，然后载入对应名字的变量的值。但是很多时候我们都更希望能够读取一个文件然后就直接使用模型，而不是还要把模型重新定义一遍。所以就需要使用另一种方法。

二、不需重新定义网络结构的方法

tf.train.import_meta_graph

```
import_meta_graph(
    meta_graph_or_file,
    clear_devices=False,
    import_scope=None,
    **kwargs
)
```

这个方法可以从文件中将保存的graph的所有节点加载到当前的default graph中，并返回一个saver。也就是说，我们在保存的时候，除了将变量的值保存下来，其实还有将对应graph中的各种节点保存下来，所以模型的结构也同样被保存下来了。

比如我们想要保存计算最后预测结果的`y`，则应该在训练阶段将它添加到collection中。具体代码如下

保存

```
### 定义模型
input_x = tf.placeholder(tf.float32, shape=(None, in_dim), name='input_x')
input_y = tf.placeholder(tf.float32, shape=(None, out_dim), name='input_y')

w1 = tf.Variable(tf.truncated_normal([in_dim, h1_dim], stddev=0.1), name='w1')
b1 = tf.Variable(tf.zeros([h1_dim]), name='b1')
w2 = tf.Variable(tf.zeros([h1_dim, out_dim]), name='w2')
b2 = tf.Variable(tf.zeros([out_dim]), name='b2')
keep_prob = tf.placeholder(tf.float32, name='keep_prob')
hidden1 = tf.nn.relu(tf.matmul(self.input_x, w1) + b1)
hidden1_drop = tf.nn.dropout(hidden1, self.keep_prob)
### 定义预测目标
y = tf.nn.softmax(tf.matmul(hidden1_drop, w2) + b2)
# 创建saver
saver = tf.train.Saver(...variables...)
# 假如需要保存y，以便在预测时使用
tf.add_to_collection('pred_network', y)
sess = tf.Session()
for step in xrange(1000000):
    sess.run(train_op)
    if step % 1000 == 0:
        # 保存checkpoint, 同时也默认导出一个meta_graph
        # graph名为'my-model-{global_step}.meta'.
        saver.save(sess, 'my-model', global_step=step)
```

载入

```
with tf.Session() as sess:
  new_saver = tf.train.import_meta_graph('my-save-dir/my-model-10000.meta')
  new_saver.restore(sess, 'my-save-dir/my-model-10000')
  # tf.get_collection() 返回一个list. 但是这里只要第一个参数即可
  y = tf.get_collection('pred_network')[0]

  graph = tf.get_default_graph()

  # 因为y中有placeholder，所以sess.run(y)的时候还需要用实际待预测的样本以及相应的参数来填充这些placeholder，而这些需要通过graph的get_operation_by_name方法来获取。
  input_x = graph.get_operation_by_name('input_x').outputs[0]
  keep_prob = graph.get_operation_by_name('keep_prob').outputs[0]

  # 使用y进行预测  
  sess.run(y, feed_dict={input_x:....,  keep_prob:1.0})
```

**这里有两点需要注意的：** 
一、 saver.restore()时填的文件名，因为在saver.save的时候，每个checkpoint会保存三个文件，如 
`my-model-10000.meta`, `my-model-10000.index`, `my-model-10000.data-00000-of-00001` 
在`import_meta_graph`时填的就是meta文件名，我们知道权值都保存在`my-model-10000.data-00000-of-00001`这个文件中，但是如果在restore方法中填这个文件名，就会报错，应该填的是**前缀**，这个前缀可以使用`tf.train.latest_checkpoint(checkpoint_dir)`这个方法获取。

二、模型的y中有用到placeholder，在sess.run()的时候肯定要feed对应的数据，因此还要根据具体placeholder的名字，从graph中使用`get_operation_by_name`方法获取。

##### pip freeze 用途

Output installed packages in requirements format.

packages are listed in a case-insensitive sorted order.

```
$ env1/bin/pip freeze > requirements.txt
$ env2/bin/pip install -r requirements.txt
```

> .freeze显示的只有17个，而pip list 和 pip freeze --all显示了20个，
> freeze 显示 少了 pip , wheel, setuptools.






#### end

