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

### 04-22

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

2. [ROC曲线和AUC值](https://blog.csdn.net/dazhi_100/article/details/73469366)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/spurs/image/general/auc.png)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/spurs/image/general/auc_1.png)

   AUC分数是曲线下的面积（Area under curve），越大意味着分类器效果越好。

   ROC曲线适用于二分类问题，以假正率为横坐标，真正率为纵坐标的曲线图

   - 基本理解

     **TP**:正确的肯定数目

     **FN**:漏报，没有找到正确匹配的数目

     **FP**:误报，没有的匹配不正确

     **TN**:正确拒绝的非匹配数目

   - **AUC意味着什么**

     那么AUC值的含义是什么呢？根据(Fawcett, 2006)，AUC的值的含义是：

     The AUC value is equivalent to the probability that a randomly chosen positive example is ranked higher than a randomly chosen negative example.

     这句话有些绕，我尝试解释一下：首先AUC值是一个概率值，当你随机挑选一个正样本以及一个负样本，当前的分类算法根据计算得到的Score值将这个正样本排在负样本前面的概率就是AUC值。当然，AUC值越大，当前的分类算法越有可能将正样本排在负样本前面，即能够更好的分类。

   - **为什么使用ROC曲线**
     既然已经这么多评价标准，为什么还要使用ROC和AUC呢？因为ROC曲线有个很好的特性：当测试集中的正负样本的分布变化的时候，ROC曲线能够保持不变。在实际的数据集中经常会出现类不平衡（class imbalance）现象，即负样本比正样本多很多（或者相反），而且测试数据中的正负样本的分布也可能随着时间变化。下图是ROC曲线和Precision-Recall曲线5的对比：

   - sklearn中的计算方法

     ```python
         check_consistent_length(x, y)
         x = column_or_1d(x)
         y = column_or_1d(y)

         if x.shape[0] < 2:
             raise ValueError('At least 2 points are needed to compute'
                              ' area under curve, but x.shape = %s' % x.shape)

         direction = 1
         if reorder:
             # reorder the data points according to the x axis and using y to
             # break ties
             order = np.lexsort((y, x))
             x, y = x[order], y[order]
         else:
             dx = np.diff(x)
             if np.any(dx < 0):
                 if np.all(dx <= 0):
                     direction = -1
                 else:
                     raise ValueError("Reordering is not turned on, and "
                                      "the x array is not increasing: %s" % x)

         area = direction * np.trapz(y, x)
         if isinstance(area, np.memmap):
             # Reductions such as .sum used internally in np.trapz do not return a
             # scalar by default for numpy.memmap instances contrary to
             # regular numpy.ndarray instances.
             area = area.dtype.type(area)
         return area
     ```

   > 参考：
   >
   > [ROC和AUC介绍以及如何计算AUC](http://alexkong.net/2013/06/introduction-to-auc-and-roc/)
   >
   > [机器学习性能评估指标](http://charleshm.github.io/2016/03/Model-Performance/#)
   >
   > ​
   >
   > [AUC计算方法总结](https://blog.csdn.net/dazhi_100/article/details/73469366)
   >
   > [模型评价(一) AUC大法](https://segmentfault.com/a/1190000010410634)
   >
   > [精确率与召回率，RoC曲线与PR曲线](http://www.cnblogs.com/pinard/p/5993450.html)

3. 对数损失

   > 亦称逻辑回归损失，交叉熵损失

   对于二分类问题

   ​	$$L_{\rm log}(y,p)=-\log{\rm Pr}(y|p)=-(y\log(p)+(1-y)\log(1-p))$$

   对于多分类问题

   ​	$$L_{\log}(Y_i,P_i)=-\log{\rm Pr}(Y_i|P_i)=\sum\limits_{k=1}^{K}y_{i,k}\log p_{i,k}$$

4. Hinge loss, 铰链损失，边缘最大化

   铰链损失最开始出现在二分类问题中，假设正样本被标记为1，负样本被标记为-1，yy是真实值，ww是预测值，则铰链损失定义为：

   $$L_{\text{Hinge}}(w, y)=\max\{1-wy,0\}=|1-wy|_+$$

   然后被扩展到多分类问题，假设ywyw是对真实分类的预测值，ytyt是对非真实分类预测中的最大值，则铰链损失定义为：

   $$L_{\text{Hinge}}(y_w, y_t)=\max\{1+y_t-y_w,0\}$$

   注意，二分类情况下的定义并不是多分类情况下定义的特例。

5. 平均绝对误差MAE，L1范数损失

   $${\rm MAE}(y, \hat{y})=\frac{1}{n_{\rm samples}}\sum\limits_{i=1}^{n_{\rm samples}}|y_i-\hat{y}_i|$$

6. 平均平方误差MSE，l2范数损失

   $${\rm MSE}(y, \hat{y})=\frac{1}{n_{\rm samples}}\sum\limits_{i=1}^{n_{\rm samples}}(y_i-\hat{y}_i)^2$$

#### 好的博客，适合每天阅读的那种

1. https://swe.mirsking.com/
2. https://plushunter.github.io/
3. http://www.csuldw.com/
4. http://alexkong.net/index.html
5. http://charleshm.github.io/
6. http://www.cnblogs.com/pinard/

#### 判别模型和生成模型

1. https://blog.csdn.net/zouxy09/article/details/8195017
2. https://blog.csdn.net/qq_34896915/article/details/73771747

#### 数组随机打乱顺序

- 相当于从袋子里取球，每次随机的取一个球。
- [地址](https://www.zhihu.com/question/68330851/answer/266506621)

### 04-23

#### Leetcode 中的问题解题思路

1. 想清楚问题，理解清楚，至少花五分钟

2. 先处理特殊情况

3. ```c++
   istringstream in(str);
   // 可以有效了处理字符串split问题
   ```

#### 机器学习中概率分布

1. https://ayase.moe/2017/05/28/common-dist-in-ml/

2. 指数分布

   ```c++
   f(x)=λe**(-λx), x>0
   f(x)=0, x<=0

   其中 λ>0,叫做指数分布, X~E(λ)

   分布函数
   F(x) = 1-e**(-λx), x>0
   F(x) = 0, x<=0

   当一个时间发生了，那么，在此基础上在发生一个delta事件的概率是独立的。
   例如:
   交通事故发生的时间间隔服从指数分布，那么，过去的13个小时没有发生事故，再经过两个小时发生事故的概率是多少？
   无论前面是否发生事故，经过两个小时发生的事故的概率都是一样大的。
   P(X>13+2|X>13)=P(X>2)=1-F(2)
   ```

3. 时间独立性

   P(AB) = P(A)P(B)称作A和B是相互独立的事件。

   ```
       (1) P(AB) = P(A)P(B)
       (2) P(AC) = P(A)P(C)
       (3) P(BC) = P(B)P(C)
       (4) P(ABC) = P(A)P(B)P(C)

   其中: (1) (2) (3)成立，称作A B C两两独立；而 (1) (2) (3) (4)成立,都成立才称作相互独立。

   P(A∪B) = P(A) + P(B) - P(AB) = P(A) + P(B) - P(A)P(B)
   ```

4. 协方差

   计算公式: Cov(X,Y)=E(XY)-E(X)E(Y)

   ρ的理解很关键，表示两个随机变量的相关性。如果二者线性相关，那么使用1个随机变量就可以了，没有必要使用两个随机变量。

5. $$D(x) = E(x^2) - [E(x)]^2$$

| 分布名称             | 期望             | 方差               |
| ---------------- | -------------- | ---------------- |
| 泊松分布 X~π(λ)      | E(X)=λ         | D(X)=λ           |
| 正态分布 X~N(μ,σ**2) | E(X) = μ       | D(X)=σ**2        |
| 指数分布 X~E(λ)      | E(X) = 1/λ     | D(X)=1/λ**2      |
| 二项分布 X~B(n,p)    | E(X) = np      | D(x)=np(1-p)     |
| 几何分布 X~G(p)      | E(X) = 1/p     |                  |
| 均匀分布 X~U(a,b)    | E(X) = (a+b)/2 | D(X)=(b-a)**2/12 |

6. http://www.csuldw.com/2016/08/19/2016-08-19-probability-distributions/#more


### 04-24

#### KNN

1. KNN中，当训练集、距离度量、k、分类决策规则确定之后，对于任何一个新的输入实例，他所属的类唯一确定。

2. 距离度量有：欧氏距离、曼哈顿距离、切比雪夫距离、闵可夫斯基距离、标准化欧式距离、余弦夹角

3. K值较小时候，就相当于用较小的领域中的训练实例进行预测，K值减小意味着模型变复杂了，容易发生过拟合

   K值较大时候，减少了学习的估计误差。

4. 分类决策规则：主要是多数表决

5. 简单、易于理解、易于实现、无需训练、无需估计参数、

6. 懒惰学习，只有当需要分类测试样例时再进行，lazy learner

   积极学习，一旦训练集可用，就开始学习从输入属性到类标号的映射模型。

   > https://plushunter.github.io/2017/01/05/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97%EF%BC%881%EF%BC%89%EF%BC%9AK%E8%BF%91%E9%82%BB/

####  线性回归

1. http://www.cnblogs.com/jerrylead/archive/2011/03/05/1971867.html
2. https://plushunter.github.io/2017/01/08/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97%EF%BC%882%EF%BC%89%EF%BC%9A%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92/
3. 最小二乘法或者梯度下降法或者牛顿法（海森矩阵）

#### 逻辑回归

1. https://plushunter.github.io/2017/01/12/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97%EF%BC%883%EF%BC%89%EF%BC%9A%E9%80%BB%E8%BE%91%E6%96%AF%E8%B0%9B%E5%9B%9E%E5%BD%92/
2. 推导过程，从极大似然估计，到最小对数似然估计

#### 决策树

1. https://plushunter.github.io/2017/01/15/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97%EF%BC%884%EF%BC%89%EF%BC%9A%E5%86%B3%E7%AD%96%E6%A0%91/

#### 随机森林

1. https://plushunter.github.io/2017/01/16/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97%EF%BC%885%EF%BC%89%EF%BC%9A%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97/

#### Adaboost

1. https://plushunter.github.io/2017/01/18/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97%EF%BC%886%EF%BC%89%EF%BC%9AAdaBoost/




### 04-25

#### #include <cassert>, <algorithm>, 

[link_cassert](http://www.cplusplus.com/reference/cassert/assert/) [link_algorithm](http://www.cplusplus.com/reference/algorithm/)

```c++
#include <cassert>
assert(int expression)
```

#### string toupper(), tolower(), strupr(), strlwr()

```c++
#include<iostream>  
#include<string>  
  
using namespace std;  
  
int main(int argc, char* argv[])  
{  
    //声明字符数组  
    char str[80],*p;  
    int i;  
  
    //转换字符串中的小写为大写  
    cout<<"将字符串中的小写字母转换为大写"<<endl;  
    cout<<"请输入原字符串："<<endl;  
    cin>>str;  
    p=strupr(str);  
    cout<<"p:"<<p<<endl;  
    cout<<"string:"<<str<<endl;  
    cout<<"___________________"<<endl;  
  
    //转换字符串中的大写为小写  
    cout<<"将字符串中的大写字母转换为小写"<<endl;  
    cout<<"请输入原字符串："<<endl;  
    cin>>str;  
    p=strlwr(str);  
    cout<<"p:"<<p<<endl;  
    cout<<"string:"<<str<<endl;  
    cout<<"___________________"<<endl;  
  
    system("pause");  
    return 0;  
}  
```

```c++
#include <iostream>  
  
using namespace std;  
  
int main()  
{  
    cout<<(char)toupper(97)<<'\n';  
    cout<<(char)toupper('a')<<'\n';  
    cout<<(char)tolower(66)<<'\n';  
    cout<<(char)tolower('B')<<'\n';  
  
    return 0;  
}  
```

#### ubuntu 16 释放显卡内存

```sudo kill -9 PID```















































#### 办公软件不止office，还有xmind思维导图

