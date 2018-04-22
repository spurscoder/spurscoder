---
layout: post
title: "04.23到04.29.home"
author: "Spurs"
date: 2018-04-29 12:40:00
description:
photos:
links:
categories:
tags:
---

> 04.23到04.29.home

<!-- more -->

### 04-23

#### 二分类性能评价指标

> [链接](http://www.cnblogs.com/zhaokui/p/ml-metric.html)

1. 精确率和召回率

   精确率precision指的是模型判为正的所有样本中有多少是真正的正样本。 - 查准率

   召回率recall指的是所有正样本有多少被模型判为了正样本。 - 查全率

   为了再precision和recall之间权衡，

   有一种选择是准确率-召回率曲线(P-R curve)，曲线下面积为AP分数（average precision score）

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/spurs/image/general/P_R_curve.png)

   另一种选择是\\( $F_{\beta}$ \\)分数：

   ​	$$F_{\beta}=(1+\beta^2)\cdot\frac{\text{precision}\cdot\text{recall}}{\beta^2\cdot\text{precision}+\text{recall}} $$

   当\\( $\beta$ = 1 \\)时候，称为F1分数，是分类和信息检索中最常用的指标之一

2. ROC曲线和AUC值

   ​

#### 1

