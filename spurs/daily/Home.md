---
layout: post
title: "04.16到04.22.home"
author: "Spurs"
date: 2018-04-22 12:40:00
description:
photos:
links:
categories:
tags:
---

> 04.16到04.22.home

<!-- more -->

### 04-15 整理个人简历

### 04-16 阅读看山杯比赛的代码 - 前七名选手的代码

#### 第一名的代码

- 代码有很强的可扩展性

- 通过类继承basicmodel，每个新的model都继承了basicmodel，从而提高代码可用性。

- 有一个统一的配置文件，每个模型的配置都可以在config.py中进行配置

- ```python
  # 这个包可以有效的提高从外部输入 参数的情况。
  import fire
  fire.Fire() 
  ```

- ```python
  import tpdm
  # 可以很好的查看进度	
  ```

### 04-18

#### Python-Filter()

> 顾名思义，Filter起过滤的作用。自动提取列表中满足条件的元素。

```python
# examples
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
```

#### Python-Reduce()

> 不断作用于列表中的每个元素，从头到尾

```python
from functools import reduce
product = reduce((lambda x,y: x*y), [1,2,3,4])
# output: 24
```

#### torch可视化工具-visdom

> facebook AI Lab 的一个工具，用于可视化模型和numpy

A flexible tool for creating, organizing, and sharing visualizations of live, rich data. Supports Torch and Numpy. [link](https://github.com/facebookresearch/visdom)

#### [np.savez_compressed](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.savez_compressed.html)

> np.savez_compressed(file, *args, **kwds)
>
> Save several arrays into a single file in compressed `.npz` format
>
> `np.save` Save a single array to a binary file in numpy format
>
> `np.savetxt` Save an array to a file as plain txt
>
> `np.savez` Save several arrays into an *uncompressed* `.npz` file format
>
> `np.load` Load the files created by savez_compressed.

#### ipdb调试Python代码

> [链接](https://pypi.org/project/ipdb/)
>
> ipdb exports functions to access the [IPython](http://ipython.org/) debugger, which features tab completion, syntax highlighting, better tracebacks, better introspection with the same interface as the pdb module.

#### tf.keras.preprocessing.sequence.[pad_sequences()](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/sequence/pad_sequences)

```python
tf.keras.preprocessing.sequence.pad_sequences(
    sequences,
    maxlen=None,
    dtype='int32',
    padding='pre',
    truncating='pre',
    value=0.0
)
```

Arguments:

- **sequences**: list of lists where each element is a sequence
- **maxlen**: int, maximum length
- **dtype**: type to cast the resulting sequence.
- **padding**: 'pre' or 'post', pad either before or after each sequence.
- **truncating**: 'pre' or 'post', remove values from sequences larger than maxlen either in the beginning or in the end of the sequence
- **value**: float, value to pad the sequences to the desired value.

Returns:

- **x**: numpy array with dimensions (number_of_sequences, maxlen)

Raises:

- **ValueError**: in case of invalid values for `truncating` or `padding`, or in case of invalid shape for a `sequences` entry.

#### Python工具包-[hyperopt](https://github.com/hyperopt/hyperopt)

> Hyperopt is a Python library for serial and parallel optimization over awkward search spaces, which may include real-valued, discrete, and conditional dimensions.

#### Torch-[torch.nn.Linear(in_features, out_features, bias=True)](http://pytorch.org/docs/master/nn.html?highlight=class%20sequential#linear)

>  Applies a linear transformation to the incoming data: y=Ax+b

### 04-19

#### `nvidia-smi` 错误修改过程

- 发现linux内核版本对其有很大影响，通过`uname -r` 查看内核版本，禁止内核upgrade
- 按照官网指导，不需要单独安装显卡驱动，直接在安装cuda时候一同安装driver
- 通过各种官网提供的测试方法之后
- 安装cudnn
- 安装tensorflow-gpu

固定内核版本:

```
echo "linux-image-4.10.0-27-generic hold" | dpkg --set-selections
# dpkg --get-selections linux-image-4.10.0-27-generic
注意：设置为hold状态的软件包，对于apt upgrade命令，不会升级，但是依然可以通过apt install命令将其升级并将状态切回install。因此，从安全性角度来看，这样做其实效果不大，仅仅只是避免了偶然的操作失误。本人还是推荐执行apt install来进行“定点升级”
```

- 重启之后，可能会报错，找不到lib....so.9.0，这时候可以copy文件到/usr/local/lib中，错误就消失了。

  此时需要从`/usr/local/cuda-9.0/lib64/`copy到`/usr/local/lib/`，所有的都copy。

####  pexpect ssh自动登录

代码[位置](https://github.com/spurscoder/spurscoder.github.io/tree/master/spurs/code/ssh.py)

#### Terminator 终端切屏

#### 多GPU，资源分配

> - `"/cpu:0"`: The CPU of your machine.
> - `"/device:GPU:0"`: The GPU of your machine, if you have one.
> - `"/device:GPU:1"`: The second GPU of your machine, etc.

```python
with tf.device('/cpu:0'):
with tf.device('/device:GPU:2'):
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
```

[参考位置](https://blog.csdn.net/u014381600/article/details/72911262)

#### 查找进程以及kill进程,查看GPU及进程

- `ps -ef | grep python3`
- `kill -9 pid`
- `watch -n 1 -d nvidia-smi`
- `top -u spurs`

#### 1

#### 1





