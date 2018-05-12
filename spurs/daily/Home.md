---
layout: post
title: "05.07到05.13.home"
author: "Spurs"
date: 2018-05-13 12:40:00
description:
photos:
links:
categories:
tags:
---

> 05.07到05.13.home
>
> 做自己认为正确的事情，避免从众，做一个有主见的人。寻找自己追求的事情。
>
> Do what you think is right.

<!-- more -->

#### 05.08

##### lru_cache

> https://docs.python.org/3/library/functools.html
>
> http://kuanghy.github.io/2016/04/20/python-cache

缓存是一种将定量数据加以保存以备迎合后续请求的处理方式，旨在加快数据的检索速度。

通过用键值对的防止将数据放到字典中，如果下次需要取值时可以直接到字典中获取。

#### 05-10

##### gc模块

> Python作为一种动态类型的语言，其对象和引用分离。这与曾经的面向过程语言有很大的区别。为了有效的释放内存，Python内置了垃圾回收的支持。Python采取了一种相对简单的垃圾回收机制，即引用计数，并因此需要解决孤立引用环的问题

python话说会自己管理内存，实际上，对于占用很大内存的对象，并不会马上释放。举例，a=range(10000*10000)，会发现内存飙升一个多G，del a 或者a=[]都不能将内存降下来。
del 可以删除多个变量，del a,b,c,d
办法：

```
gc.enable() 打开自动回收garbage
gc.disable() 关闭自动回收垃圾
gc.isenabled 返回自动回收垃圾是否打开
gc.collect() 开始回收垃圾，然有三个参数0,1,2 分别代表不同级别的回收
gc.set_debug(flags) debug的结果会写入sys.stderr
gc.set_debug() 返回debug的结果
gc.get_objects 返回被删除的东西的名称
```

##### psutil模块

1. psutil是一个跨平台库（http://code.google.com/p/psutil/），能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。它主要应用于系统监控，分析和限制系统资源及进程的管理。它实现了同等命令行工具提供的功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。目前支持32位和64位的Linux、Windows、OS X、FreeBSD和Sun Solaris等操作系统，

2. ```
   import psutil
   mem = psutil.virtual_memory()
   mem
   系统内存的所有信息
   svmem(total=1040662528, available=175054848, percent=83.2, used=965718016, free=74944512, active=566755328, inactive=59457536, buffers=9342976, cached=90767360
   ```

3. ```
   import Psutil
   查看cpu所有信息
   >>> psutil.cpu_times()
   scputimes(user=11677.09, nice=57.93, system=148675.58, idle=2167147.79, iowait=260828.48, irq=7876.28, softirq=0.0, steal=3694.59, guest=0.0, guest_nice=0.0)
   ```

##### Numpy中stack()，hstack()，vstack()函数详解

https://blog.csdn.net/csdn15698845876/article/details/73380803

##### sklearn.preprocessing.MinMaxScaler

> http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html

对矩阵中的数字进行归一化，按列归一。

```
>>> from sklearn.preprocessing import MinMaxScaler
>>>
>>> data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
>>> scaler = MinMaxScaler()
>>> print(scaler.fit(data))
MinMaxScaler(copy=True, feature_range=(0, 1))
>>> print(scaler.data_max_)
[  1.  18.]
>>> print(scaler.transform(data))
[[ 0.    0.  ]
 [ 0.25  0.25]
 [ 0.5   0.5 ]
 [ 1.    1.  ]]
>>> print(scaler.transform([[2, 2]]))
[[ 1.5  0. ]]
```

##### from scipy.sparse import csr_matrix

>  https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html

Compressed Sparse Row matrix

```
>>> import numpy as np
>>> from scipy.sparse import csr_matrix
>>> csr_matrix((3, 4), dtype=np.int8).toarray()
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]], dtype=int8)
>>> row = np.array([0, 0, 1, 2, 2, 2])
>>> col = np.array([0, 2, 2, 0, 1, 2])
>>> data = np.array([1, 2, 3, 4, 5, 6])
>>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
array([[1, 0, 2],
       [0, 0, 3],
       [4, 5, 6]])
```

```
>>> from scipy.sparse import coo_matrix, hstack
>>> A = coo_matrix([[1, 2], [3, 4]])
>>> B = coo_matrix([[5], [6]])
>>> hstack([A,B]).toarray()
array([[1, 2, 5],
       [3, 4, 6]])
```

#### 05-12

##### TextBlob: Simplified Text Processing

> http://textblob.readthedocs.io/en/dev/

*TextBlob* is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

#####  github all kinds of text classificaiton models and more with deep learning

> https://github.com/brightmart/text_classification

the purpose of this repository is to explore text classification methods in NLP with deep learning.