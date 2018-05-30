---
layout: post
title: "05.28到06.03.home"
author: "Spurs"
date: 2018-06-03 12:40:00
description:
photos:
links:
categories:
tags:
---

> 05.28到06.03.home
>

<!-- more -->

#### 06.03

#### 2018腾讯社交广告大赛

>腾讯社交广告Lookalike相似人群拓展，原理是基于目标人群，从海量其他人群中寻找相似人群，并拓展人群规模。
>
>实际业务中，Lookalike能给予广告主已有的消费者，找出与已有消费者相似的潜在消费者，以帮助广告主挖掘新客，拓展业务

1. 特征工程：

   用户特征： interest五个，kw三个，topic三个，教育年龄，性别，有无房子，婚姻状态等用户特征

   广告特征：广告主id，广告推广计划，创建时间，产品id，产品类型等特征。

   训练集中：其中正例有42万，而反例有800万左右。

   用户：有userfeature.data 1100万，其中800万的训练集，200万的测试集合

   评价标准是所有待评估的m个种子包的平均AUC值。

   1. 首先处理缺失值，对计算缺失率，考虑将缺失率较大的特征直接删除，发现删除之后模型效果更好了，

      全部是类别型特征，用的OntHotEncoder()，以及CountVectorizer()

   2. 其中有一个特征直接是26万中取值，特征维数大约为40万。

      剔除掉缺失率过高的特征: interest3, interest4, kw3, appIdInstall, topic3；去除特征维数比较大的特征之后，效果提升

   3. 通过绘制柱状图，查看每个特征与目标之间的关系，查看特征之间的关系

   4. 联网类型可能会影响广告转化率，推广计划转化率特征，用户所在位置的历史点击率特征

   5. 广告转化率，发出的广告且别发送给种子用户的数量

   6. 对特征进行了归一化

   7. 点击某广告的用户平均年龄；用户的广告点击次数，广告点击率；分析广告投放以及地理位置的关系

   8. 用户的兴趣和广告的兴趣有多少相符合；用户的兴趣总数；特征年龄分布

   9. clf.feature_importances；模型调参数，重点调节estimators，learning_rate, grid_search

   10. 尝试使用embedding来进行降维interest kw topic

   11. 16G内存

   12. 随机下采样负样例，训练多个LGB之后，模型融合，现实加权融合，之后bagging，

       因为下采样会丢失信息，如何减少信息的损失呢？第一种方法叫做EasyEnsemble，利用模型融合的方法（Ensemble）：多次下采样（放回采样，这样产生的训练集才相互独立）产生多个不同的训练集，进而训练多个不同的分类器，通过组合多个分类器的结果得到最终的结果。第二种方法叫做BalanceCascade，利用增量训练的思想（Boosting）：先通过一次下采样产生训练集，训练一个分类器，对于那些分类正确的大众样本不放回，然后对这个更小的大众样本下采样产生训练集，训练第二个分类器，以此类推，最终组合所有分类器的结果得到最终结果。

       上采样容易过拟合

2. 1、**Bagging**：使用训练数据的不同随机子集来训练每个 Base Model，最后进行每个 Base Model 权重相同的 Vote。也即 Random Forest 的原理。  2、**Boosting**：迭代地训练 Base Model，每次根据上一个迭代中预测错误的情况修改训练样本的权重。也即 Gradient Boosting，Adaboost 的原理。比 Bagging 效果好，但更容易 Overfit。  3、**Blending**：用不相交的数据训练不同的 Base Model，将它们的输出取（加权）平均。实现简单，但对训练数据利用少了。  4、**Stacking**：接下来会详细介绍。 

3. https://blog.csdn.net/u012969412/article/details/76636336

   stacking是不重复的，而blending是不重复的。

   stacking就是训练出一个权重来，你和多个level1模型的结果，最终得到真正的结果。

   bagging：使用训练集的不同随机子集来训练每个Base model，最后进行每个basemodel权重相同的Vote，也即Random Forest的原理。

   可以使用stacking的第一层的方式训练模型。分为n

   在实际比赛中往往不能单纯的使用某一种模型融合方法。






#### end

