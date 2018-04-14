---
layout: post
title: "using svd for recommendation"
author: "Spurs"
date: 2018-01-25 12:00:00
tags:
---

> using svd for recommendation

<!-- more -->

​	本笔记将介绍SVD的概念及其能够进行数据约简的原因。然后，可以通过python的SVD实现将数据映射到低维空间从而进行简化。再接下来，我们就将学习推荐引擎的概念和他们的实际运行过程。最后可以利用SVD实现一个简单的推荐系统。

- SVD矩阵分解
- 推荐引擎
- 利用SVD提升推荐引擎的性能

### SVD的应用

​	奇异值分解：

- 优点：简化数据，去除噪声，提高算法的结果。
- 缺点：数据转换可能难以理解。
    - 适用数据类型：数值型数据。

#### 隐形语义检索

​	通过SVD分解得到的对角矩阵的奇异值，对应于文档中的概念或主题，通过概念或主题可以加快检索文档的速度。

#### 推荐系统

​	假如有个矩阵，用户及菜品评价表，就可以实现一个推荐系统。简单版本的推荐系统能够计算项或者人之间的相似度。更先进版本的方法则是利用SVD从数据中构建一个主题空间，然后从该空间下计算其相似度。

### 矩阵分解

​	奇异值分解的公式：
$$
Data_{mn} = U_{mm} \Sigma_{mn} V^T_{nn}
$$

#### 利用python实现SVD

```python
>>> from numpy import *
>>> U,Sigma,VT = linalg.svd([[1,1], [7,7]])
```

​	这个时候得到的奇异值可能有很多，我只需要保留其中的90%左右的能量即可。为了计算所以的能量：

> 1.求奇异值的平方和直到90%为止
>
> 2.可以预估性质的保留前几个或者几千个奇异值

#### 基于协同过滤的推荐引擎

​	Amazon根据用户的购物历史推荐物品，Netflix会向用户推荐电影，新闻网站向用户推荐新闻报道。有很多方法实现推荐功能，今天就介绍一下协同过滤的方法。

​	协同过滤（collaborative filtering）是通过对比用户和其他用户的数据进行对比来实现推荐的。这其中就需要数学方法来来进行相似度计算，如果发现用户对某个菜品没有评价，然而我们又不清楚用户喜不喜欢某个东西，这个时候我们就只能通过计算菜品与其他菜品之间的相似度来判断用户是否喜欢某个菜品。

#### 相似度计算

​	   在数据矩阵中进行相似度计算，就是进行向量之间的运算，

- 相似度=1/(1+距离)：当距离为0时，相似度为1.0。距离越大相似度越小
- 皮尔逊相关系数(Pearson correlation): 它避免来对用户评级的量级的敏感度。可以通过Numpy中的corrcoef()函数来计算。其取值范围在-1到+1之间，
    - 余弦相似度(cosine similarity)：其计算的是两个向量夹角的余弦值，在Numpy中的`linalg.norm()`

```python
from numpy import *
from numpy import linalg as la

def eclidSim(inA, inB):
  return 1.0/(1.0 + la.norm(inA - inB))

def pearsonSim(inA, inB):
  if len(inA) < 3 : return 1.0
  return 0.5 + 0.5*corrcoef(inA, inB, rowvar = 0)[0][1]

def cosSim(inA, inB):
  num = float(inA.T * inB)
  denom = la.norm(inA) * la.norm(inB)
  return 0.5 + 0.5*(num/denom)
```

### 示例

-   基于物品相似度还是用户相似度

    > 一般是基于物品相似度，因为一般物品的数量少于用户的数量，在计算的时候会简便点。

-   推荐系统的评价

    > 我们可以将某些一直的评分值去掉，然后对他们进行预测，最后计算预测值与真实值之间的差值。
    >
    > 指标就是**最小均方根误差（Root Mean Squared Error，RMSE）

#### 餐馆菜肴推荐引擎。

​	工作流程：给定一个用户，系统会为此用户返回N个最好的推荐菜。为了实现这一点。

   	1. 找到用户没有评级的菜，即矩阵中的0值
   	2. 对每个没有评级的菜，预测一个可能的评级分数。
      3. 对菜品的评级排序，找到最好的N的物品

```python
def standEst(dataMat, user, simMeas, item):
  n = shape(dataMat)[1]
  simTotal = 0.0; ratSimTotal = 0.0
  for j in range(n):
    userRating = dataMat[user, j]
    if userRating == 0 : continue
    overLap = nonzero(logical_and(dataMat[:, item].A > 0, \
                                 dataMat[:, j].A > 0))[0]
    if len(overLap) == 0 similarity = 0
    else:similarity = simMeas(dataMat[overLap, item], \
                             dataMat[overLap, j])
    # pring 'the %d and %d similarity is : %f' % (item, j, similarity)
    simTotal += similarity
    ratSimTotal += similarity * userRating
  if simTotal == 0: return 0
  else: return ratSimTotal / simTotal
  
def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
  unratedItems = nonzero(dataMat[user,:].A==0)[1]
  itemScores = []
  for item in unratedItems:
    estimatedScore = standEst(dataMat, user, simMeas, item)
    itemScores.append((item, estimatedScore))
  return sorted(itemScores, \
               key=lambda jj:jj[1], reverse=True)[:N]
```

通过上述两个函数就可以将菜品中相对较好的N的推荐给用户。

#### 推荐的效果

> 实际生产环境中，矩阵是非常稀疏的！
>
> 这个时候就用到了SVD，提取并简化矩阵中的特征

要想用到SVD，只需要修改一下函数`svdEst`即可

```python
def svdEst(dataMat, user, simMeas, item):
  n = shape(dataMat)[1]
  simTotal = 0.0; ratSimTotal = 0.0
  U, Sigma, VT = la.svd(dataMat)
  Sig4 = mat(eye(4)*Sigma[:4])
  xformedItems = dataMat.T * U[:,:4] * Sig4.I
  for j in range(n):
    userRating = dataMat[user, j]
    if userRating == 0: continue
    similarity = simMeas(xformedItems[item, :].T, \
                        xformedItems[j, :].T)
    print 'the %d and %d similarity is: %f' % (item, j, similarity)
    simTotal += similarity
    ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal / simTotal
```

> 其中为何只取前四列，是根据能量来获得的。
>
> 因为前四列就已经包含了全部能量的90%

#### 挑战

- SVD分解特别耗费时间，会降低程序的运行速度。特别是对特别大的矩阵。

  > SVD分解可以在**开始**运行时候运行一次，在大型系统中，SVD每天运行一次或者其频率更低，并且还要离线运行。

- 矩阵的表示问题，在实际系统运行时候，矩阵中存在大量的0，从而导致浪费大量的内存。

- 相似度计算问题。每次推荐一个物品时候，都要计算物品间的相似度。一个解决办法就是*离线计算并保存相似度得分*

#### Big Problem

如何在缺乏实际的时候给出一个好的推荐。即冷启动(cold-start)。

> 用户不喜欢一个无效的物品，而用户不喜欢的物品又无效

**也就是说，在协同过滤场景下，由于新物品到来时由于缺乏所有用户对其的喜好信息，因此无法判断每个用户对其的喜好。而无法判断某个用户对其的喜好，就无法利用该商品**

*解决方法：*

​	冷启动的解决方案就是把推荐问题当成是搜索问题。这就需要推荐物品的**属性**，比如素食、美式BBQ、价格很贵等。这可以被称为*基于内容(content_based)*的推荐。这可能比协同过滤的推荐效果差，但这是一个良好的开始。

### 总结

​	SVD是一个强大的降维工具，可以利用它从来逼近矩阵、提取重要特征。通过保留80%-90%的能量，就可以得到重要的特征、去除噪声。SVD的应用中最成功的就是推荐系统。

​	协同过滤的核心是相似度计算方法，有很多相似度计算方法(cos, pearson, 距离)，通过在低维空间中计算相似度，提高推荐效果。

​	在大规模数据集上，SVD的计算和推荐可能是一个很困难的工程问题。为了减少冗余计算和推荐所需要的时间，可以离线计算。

### others

1. 基于内容的推荐系统

   重点物品的属性建模，寻找属性相关的物品，推荐给用户。

2. 基于协同过滤的推荐系统

   需要用户的偏好数据，根据用户的偏好来计算用户的相似度，或者物品的相似度计算来判断用户是否喜欢某些物品。

3. 基于规则的推荐系统

   关联规则

4. 混合或者其他的推荐系统

   为了有效避免各自的缺点和优点，为了效果好即可。实现混合模型。

















