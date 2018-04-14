---
layout: post
title: "04.09到04.15.home"
author: "Spurs"
date: 2018-04-15 12:40:00
tags:
  - dinary
  - everyday
  - home
---

[TOC]

## 04-09

### 1.剑指Offer中的代码实现。

## 04-10

### 1.Bias && Variance

- ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/bias_variances.png)

- 左上角的示例是理想状况：偏差和方差都非常小。如果有无穷的训练数据，以及完美的模型算法，我们是有办法达成这样的情况的。然而，现实中的工程问题，通常数据量是有限的，而模型也是不完美的。因此，这只是一个理想状况。

  右上角的示例表示偏差小而方差大。靶纸上的落点都集中分布在红心周围，它们的期望落在红心之内，因此偏差较小。另一方面，落点虽然集中在红心周围，但是比较分散，这是方差大的表现。

  左下角的示例表示偏差大而方差小。显而易见，靶纸上的落点非常集中，说明方差小。但是落点集中的位置距离红心很远，这是偏差大的表现。

  右下角的示例则是最糟糕的情况，偏差和方差都非常大。这是我们最不希望看到的结果。

- 排除人为的失误，人们一般会遇到三种误差来源：随机误差、偏差和方差。

- **偏差（Bias）**描述的是通过学习拟合出来的结果的期望，与真实结果之间的差距，记作

  $Bias(X)=E[f^{'}(X)]−f(X)$

- **方差（Variance）**即为统计学中的定义，描述的是通过学习拟合出来的结果自身的不稳定性，记作

  $E[(f^{'}(X)−E[f^{'}(X)])]2$

- 如何Trade_off

  > 假设我们现在有一组训练数据，需要训练的一个模型（基于梯度的学习）。
  >
  > 在训练开始，Bias很大，因为我们的模型还没来得及开始学习，也就是与真实模型差距很大。然而Variance很小，因为训练数据集还没有来得及对模型产生影响，
  >
  > 随着训练的继续，Bias变得很小，输出值与真实值之间更加接近了。但是因为我们训练的很久了，Variance边的很大，因为我们除了学习到关于真实模型的信息，还学到了具体的只针对我们使用的模型的形象。而不同的可能的训练数据集（真实数据的子集）之间的某些特征和噪声不一致的。这就导致了我们再很多其他数据集上的就无法获得很好的效果。也就是所谓的Overfitting（过拟合）

  ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/tradeoff.png)

  若模型复杂度小于平衡点，则模型的偏差会偏高，模型倾向于欠拟合；若模型复杂度大于平衡点，则模型的方差会偏高，模型倾向于过拟合。

  在现实环境中，有时候我们很难计算模型的偏差与方差。因此，我们需要通过外在表现，判断模型的拟合状态：是欠拟合还是过拟合。

  所以，偏差较高（欠拟合）有以下两个特征：

  - 1）训练集误差很高
  - 2）验证集误差和训练集误差差不多大

  方差较高（过拟合）

  - 1）训练集误差较低
  - 2）非常高的验证集误差

- 如何处理欠拟合和过拟合

  ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/tradeoff1.png)

  当模型处于欠拟合状态时，根本的办法是增加模型的复杂度。我们一般有以下一些办法：

  - 1）增加模型迭代次数；
  - 2）训练一个复杂度更高的模型：比如在神经网络中增加神经网络层数、在SVM中用非线性SVM（核技术）代替线性SVM
  - 3）获取更多的特征以供训练使用：特征少，对模型信息的刻画就不足够了
  - 4）降低正则化权重：正则化正是为了限制模型的灵活度（复杂度）而设定的，降低其权值可以在模型训练中增加模型复杂度。

  当模型处于过拟合状态时，根本的办法是降低模型的复杂度。我们一般有以下一些办法：

  - 1）获取更多的数据：训练数据集和验证数据集是随机选取的，它们有不同的特征，以致在验证数据集上误差很高。更多的数据可以减小这种随机性的影响。
  - 2）减少特征数量
  - 3）增加正则化权重：方差很高时，模型对训练集的拟合很好。实际上，模型很有可能拟合了训练数据集的噪声，拿到验证集上拟合效果就不好了。我们可以增加正则化权重，减小模型的复杂度。

### 2.static和const进阶作用

static关键字至少有下列5个作用： 
（1）函数体内static变量的作用范围为该函数体，不同于auto变量，该变量的内存只被分配一次，因此其值在下次调用时仍维持上次的值； 
（2）在模块内的static全局变量可以被模块内所用函数访问，但不能被模块外其它函数访问； 
（3）在模块内的static函数只可被这一模块内的其它函数调用，这个函数的使用范围被限制在声明它的模块内； 
（4）在类中的static成员变量属于整个类所拥有，对类的所有对象只有一份拷贝，也就是派生类和父类中的static是公用空间的； 
（5）在类中的static成员函数属于整个类所拥有，这个函数不接收this指针，因而只能访问类的static成员变量。

const关键字至少有下列5个作用： 
（1）欲阻止一个变量被改变，可以使用const关键字。在定义该const变量时，通常需要对它进行初始化，因为以后就没有机会再去改变它了； 
（2）对指针来说，可以指定指针本身为const，也可以指定指针所指的数据为const，或二者同时指定为const； 
（3）在一个函数声明中，const可以修饰形参，表明它是一个输入参数，在函数内部不能改变其值； 
（4）对于类的成员函数，若指定其为const类型，则表明其是一个常函数，不能修改类的 成员变量； 
（5）对于类的成员函数，有时候必须指定其返回值为const类型，以使得其返回值不为“左值”。

### 3.类的继承问题

- 什么是虚函数？什么是纯虚函数？基类为什么要用虚析构函数？

- 虚函数就是用于实现多态的，因为一个类函数的调用不是在编译时候确定的，而是在运行时候确定的。编写代码的时候根本不知道具体的被调用的是基类的函数还是派生类的函数。所以称“虚函数”实现了多态的效果。核心理念就是通过基类访问派生类定义的函数。

- 纯虚函数：在基类中声明的虚函数，他在基类中没有定义。但是要求任何派生类都要定义自己的实现方法

  ```c++
  virtual void f1() = 0
  ```

  除了上面的虚函数的派生作用意外，还因为许多基类对象本身没有任何意义的。所以干脆变成纯虚函数只用于继承，而且他们必须在继承类中重新声明。

- 上面说了由于派生的关系并不知道基类的指针调用了哪一个，所以析构函数应当是虚函数，他将调用相应对象类型的析构函数，因此，如果指针指向的是子类对象，将调用子类的析构函数，然后自动调用基类的析构函数。

- **继承时不能继承基类的构造函数和析构函数**，所以在创建派生类构造函数的时候可以**成员初始化列表**的方式调用基函数的构造函数。但是析构函数是默认调用的。

- **虚基类**

  虚基类使得多个类（基类相同）派生出的对象只继承一个基类对象

- 析构函数的执行顺序和构造函数的执行顺序也刚好相反

  - 创建派生类对象时，构造函数的执行顺序和继承顺序相同，即先执行基类构造函数，再执行派生类构造函数。
  - 销毁派生类对象时，析构函数的执行顺序和继承顺序相反，即先执行派生类析构函数，再执行基类析构函数。

- ```c++
  #include <iostream>
  using namespace std;
  //虚基类A
  class A{
  public:
      A(int a);
  protected:
      int m_a;
  };
  A::A(int a): m_a(a){ }
  //直接派生类B
  class B: virtual public A{
  public:
      B(int a, int b);
  public:
      void display();
  protected:
      int m_b;
  };
  B::B(int a, int b): A(a), m_b(b){ }
  void B::display(){
      cout<<"m_a="<<m_a<<", m_b="<<m_b<<endl;
  }
  //直接派生类C
  class C: virtual public A{
  public:
      C(int a, int c);
  public:
      void display();
  protected:
      int m_c;
  };
  C::C(int a, int c): A(a), m_c(c){ }
  void C::display(){
      cout<<"m_a="<<m_a<<", m_c="<<m_c<<endl;
  }
  //间接派生类D
  class D: public B, public C{
  public:
      D(int a, int b, int c, int d);
  public:
      void display();
  private:
      int m_d;
  };
  D::D(int a, int b, int c, int d): A(a), B(90, b), C(100, c), m_d(d){ }
  void D::display(){
      cout<<"m_a="<<m_a<<", m_b="<<m_b<<", m_c="<<m_c<<", m_d="<<m_d<<endl;
  }
  int main(){
      B b(10, 20);
      b.display();
     
      C c(30, 40);
      c.display();
      D d(50, 60, 70, 80);
      d.display();
      return 0;
  }
  ```

- 数据类型转换的前提是，编译器知道如何对数据进行取舍。例如：

  ```int a = 10.9;printf("%d\n", a);```

  输出结果为 10，编译器会将小数部分直接丢掉（不是四舍五入）。再如：

  ```float b = 10;printf("%f\n", b);```

  输出结果为 10.000000，编译器会自动添加小数部分。

  类其实也是一种数据类型，也可以发生数据类型转换，不过这种转换只有在基类和派生类之间才有意义，并且只能将派生类赋值给基类，包括将派生类对象赋值给基类对象、将派生类指针赋值给基类指针、将派生类引用赋值给基类引用，这在 C++ 中称为向上转型（Upcasting）。

  相应地，将基类赋值给派生类称为向下转型（Downcasting）。

- ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/cpp_copy.png)

  ```c++
  #include <iostream>
  using namespace std;
  //基类
  class A{
  public:
      A(int a);
  public:
      void display();
  public:
      int m_a;
  };
  A::A(int a): m_a(a){ }
  void A::display(){
      cout<<"Class A: m_a="<<m_a<<endl;
  }
  //派生类
  class B: public A{
  public:
      B(int a, int b);
  public:
      void display();
  public:
      int m_b;
  };
  B::B(int a, int b): A(a), m_b(b){ }
  void B::display(){
      cout<<"Class B: m_a="<<m_a<<", m_b="<<m_b<<endl;
  }
  int main(){
      A a(10);
      B b(66, 99);
      //赋值前
      a.display();
      b.display();
      cout<<"--------------"<<endl;
      //赋值后
      a = b;
      a.display();
      b.display();
      return 0;
  }
  ```

  赋值的本质是将现有的数据写入已分配好的内存中，对象的内存只包含了成员变量，所以对象之间的赋值是成员变量的赋值，成员函数不存在赋值问题。

  这种转换关系是不可逆的，只能用派生类对象给基类对象赋值，而不能用基类对象给派生类对象赋值。理由很简单，基类不包含派生类的成员变量，无法对派生类的成员变量赋值。同理，同一基类的不同派生类对象之间也不能赋值。

- 向上转型后通过基类的对象、指针、引用只能访问从基类继承过去的成员（包括成员变量和成员函数），不能访问派生类新增的成员。

- 概括起来说就是：编译器通过指针、对象、引用来访问成员变量，指针、对象、引用指向哪个对象就使用哪个对象的数据；编译器通过指针、对象、引用的类型来访问成员函数，指针属于哪个类的类型就使用哪个类的函数。

### 3.虚函数

- **通过基类指针只能访问派生类的成员变量，但是不能访问派生类的成员函数。**


- **有了虚函数，基类指针指向基类对象时就使用基类的成员（包括成员函数和成员变量），指向派生类对象时就使用派生类的成员。**换句话说，基类指针可以按照基类的方式来做事，也可以按照派生类的方式来做事，它有多种形态，或者说有多种表现方式，我们将这种现象称为多态（Polymorphism）。

- 多态是面向对象编程的主要特征之一，C++中虚函数的唯一用处就是构成多态。

  C++提供多态的目的是：可以通过基类指针对所有派生类（包括直接派生和间接派生）的成员变量和成员函数进行“全方位”的访问，尤其是成员函数。如果没有多态，我们只能访问成员变量。

- ```c++
  #include <iostream>
  using namespace std;
  //基类People
  class People{
  public:
      People(char *name, int age);
      virtual void display();  //声明为虚函数
  protected:
      char *m_name;
      int m_age;
  };
  People::People(char *name, int age): m_name(name), m_age(age){}
  void People::display(){
      cout<<m_name<<"今年"<<m_age<<"岁了，是个无业游民。"<<endl;
  }
  //派生类Teacher
  class Teacher: public People{
  public:
      Teacher(char *name, int age, int salary);
      virtual void display();  //声明为虚函数
  private:
      int m_salary;
  };
  Teacher::Teacher(char *name, int age, int salary): People(name, age), m_salary(salary){}
  void Teacher::display(){
      cout<<m_name<<"今年"<<m_age<<"岁了，是一名教师，每月有"<<m_salary<<"元的收入。"<<endl;
  }
  int main(){
      People *p = new People("王志刚", 23);
      p -> display();
      p = new Teacher("赵宏佳", 45, 8200);
      p -> display();
      return 0;
  }
  ```

- ```c++
  int main(){
      People p("王志刚", 23);
      Teacher t("赵宏佳", 45, 8200);
     
      People &rp = p;
      People &rt = t;
     
      rp.display();
      rt.display();
      return 0;
  }
  ```

- 不过引用不像指针灵活，指针可以随时改变指向，而引用只能指代固定的对象，在多态性方面缺乏表现力，所以以后我们再谈及多态时一般是说指针

- 读者可能还未发现多态的用途，不过确实也是，多态在小项目中鲜有有用武之地。对于具有复杂继承关系的大中型程序，多态可以增加其灵活性，让代码更具有表现力。

- 注意事项：

  虚函数对于多态具有决定性的作用，有虚函数才能构成多态，这节我们来重点说一下虚函数的注意事项。

  1) 只需要在虚函数的声明处加上 virtual 关键字，函数定义处可以加也可以不加。

  2) 为了方便，你可以只将基类中的函数声明为虚函数，这样所有派生类中具有遮蔽（覆盖）关系的同名函数都将自动成为虚函数。关于名字遮蔽已在《[C++继承时的名字遮蔽](http://c.biancheng.net/cpp/biancheng/view/2985.html)》一节中进行了讲解。

  3) 当在基类中定义了虚函数时，如果派生类没有定义新的函数来遮蔽此函数，那么将使用基类的虚函数。

  4) 只有派生类的虚函数遮蔽基类的虚函数（函数原型相同）才能构成多态（通过基类指针访问派生类函数）。例如基类虚函数的原型为`virtual void func();`，派生类虚函数的原型为`virtual void func(int);`，那么当基类指针 p 指向派生类对象时，语句`p -> func(100);`将会出错，而语句`p -> func();`将调用基类的函数。

  5) 构造函数不能是虚函数。对于基类的构造函数，它仅仅是在派生类构造函数中被调用，这种机制不同于继承。也就是说，派生类不继承基类的构造函数，将构造函数声明为虚函数没有什么意义。

  6) 析构函数可以声明为虚函数，而且有时候必须要声明为虚函数，这点我们将在下节中讲解。

- 下面是构成多态的条件：

  - 必须存在继承关系；
  - 继承关系中必须有同名的虚函数，并且它们是遮蔽（覆盖）关系。
  - 存在基类的指针，通过该指针调用虚函数。

- ```c++
  #include <iostream>
  using namespace std;
  //基类Base
  class Base{
  public:
      virtual void func();
      virtual void func(int);
  };
  void Base::func(){
      cout<<"void Base::func()"<<endl;
  }
  void Base::func(int n){
      cout<<"void Base::func(int)"<<endl;
  }
  //派生类Derived
  class Derived: public Base{
  public:
      void func();
      void func(char *);
  };
  void Derived::func(){
      cout<<"void Derived::func()"<<endl;
  }
  void Derived::func(char *str){
      cout<<"void Derived::func(char *)"<<endl;
  }
  int main(){
      Base *p = new Derived();
      p -> func();  //输出void Derived::func()
      p -> func(10);  //输出void Base::func(int)
      p -> func("http://c.biancheng.net");  //compile error
      return 0;
  }
  ```

- 在基类 Base 中我们将void func()声明为虚函数，这样派生类 Derived 中的void func()就会自动成为虚函数。p 是基类 Base 的指针，但是指向了派生类 Derived 的对象。

  语句p -> func();调用的是派生类的虚函数，构成了多态。

  语句p -> func(10);调用的是基类的虚函数，因为派生类中没有函数遮蔽它。

  语句p -> func("http://c.biancheng.net");出现编译错误，因为通过基类的指针只能访问从基类继承过去的成员，不能访问派生类新增的成员。

- 什么时候声明虚函数

  首先看成员函数所在的类是否会作为基类。然后看成员函数在类的继承后有无可能被更改功能，如果希望更改其功能的，一般应该将它声明为虚函数。如果成员函数在类被继承后功能不需修改，或派生类用不到该函数，则不要把它声明为虚函数。

### 4.纯虚函数

- 在C++中，可以将虚函数声明为纯虚函数，

  ```语法格式为：virtual 返回值类型 函数名 (函数参数) = 0;```

- 纯虚函数没有函数体，只有函数声明，在虚函数声明的结尾加上`=0`，表明此函数为纯虚函数。最后的`=0`并不表示函数返回值为0，它只起形式上的作用，告诉编译系统“这是纯虚函数”。

- 包含纯虚函数的类称为抽象类（Abstract Class）。之所以说它抽象，是因为它无法实例化，也就是无法创建对象。原因很明显，纯虚函数没有函数体，不是完整的函数，无法调用，也无法为其分配内存空间。

  **抽象类通常是作为基类，让派生类去实现纯虚函数。派生类必须实现纯虚函数才能被实例化。**


- 关于纯虚函数的几点说明

  1) 一个纯虚函数就可以使类成为抽象基类，但是抽象基类中除了包含纯虚函数外，还可以包含其它的成员函数（虚函数或普通函数）和成员变量。

  2) 只有类中的虚函数才能被声明为纯虚函数，普通成员函数和顶层函数均不能声明为纯虚函数。

- 在实际开发中，你可以定义一个抽象基类，只完成部分功能，未完成的功能交给派生类去实现（谁派生谁实现）。这部分未完成的功能，往往是基类不需要的，或者在基类中无法实现的。虽然抽象基类没有完成，但是却强制要求派生类完成，这就是抽象基类的“霸王条款”。



## 04-11

## 04-12

### 1.Python [fire](https://github.com/google/python-fire) 用于自动生成命令行界面的内容库

```python
pip install fire
#--------------------------------------
import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)
#--------------------------------------
python calculator.py double 10  # 20
python calculator.py double --number=15  # 30
```

### 2.[Logistic Regression](https://blog.csdn.net/ligang_csdn/article/details/53838743)

梯度下降算法是一个很基本的算法，在机器学习和优化中有着非常重要的作用，本文首先介绍了梯度下降的基本概念，然后使用python实现了一个基本的梯度下降算法。梯度下降有很多的变种，本文只介绍最基础的梯度下降，也就是批梯度下降。

Logistic Regression虽然名字里带“回归”，但是它实际上是一种分类方法，用于两分类问题（即输出只有两种）。

- **具体过程**

1. 随机初始化权重

2. 构造预测函数

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/logistic_1.jpeg)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/logistic_2.jpeg)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/logistic_3.jpeg)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/logistic_4.jpeg)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/logistic_5.jpeg)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/logistic_6.jpeg)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/logistic_7.jpeg)

3. 构造Cost函数

4. 梯度下降法求$J(\theta)$的最小值(Cost)函数

5. 不断优化求权重

### 3.神经网络基础问题

1. Backpropagation

   后向传播是在求解损失函数L对参数W时候用到的方法，目的是通过链式法则对参数进行一层一层的求导，这里重点强调：要将参数进行随机初始化而不是全部置0，否则所有隐层的数值都会与输入相关，这称为对称失效

   大致过程是：

   - 首先前向传导计算出所有节点的激活值和输出值

     $z^{l+1} = W^{l}a^{l} + b^{l}$

     $a^{l+1} = f(z^{l+1})$

     ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/bp_1.png)

   - 计算整体损失函数

     $J(W, b) = [1/m \sum_{i=1}^{m}J(W,b;x^{i},y^{i})] + \lambda/2\sum_{l=1}^{n_l - 1}\sum_{i=1}^{s_l}\sum_{j=1}^{s_{l+1}}(W_{ji}^{l})^2$

     =$[1/m \sum_{i=1}^{m}(1/2||h_{W,b}(x^{i}) - y^{i}||^2)] + \lambda/2\sum_{l=1}^{n_l - 1}\sum_{i=1}^{s_l}\sum_{j=1}^{s_{l+1}}(W_{ji}^{l})^2$

     ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/bp_2.png)


   - 然后针对第L层的每个节点计算出残差（这里是因为UFLDL中说的残差，**本质就是整体损失函数对每一层激活值Z的导数**），所以要对W求导，只要再乘上激活函数对W的导数即可

     ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/bp_4.png)

     ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/bp_3.png)


1. 梯度消失、梯度爆炸

   梯度消失：这本质上是由于激活函数的选择导致的，最简单的sigmoid函数为例，在函数的两端梯度求导结果非常小（饱和区），导致后向传播过程中由于多次用到激活函数的导数值，使得整体的乘积梯度结果变得越来越小，也就出现了梯度消失的现象

   梯度爆炸：同理，出现在激活函数的激活区，而且权重W过大的情况下。但是梯度爆炸不如梯度消失出现的机会多。

2. ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/activation_1.png)

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/activation_2.png)

3. 参数更新的方法

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/act_3.png)

4. 解决Overfitting的方法

   Dropout, regularization, batch normalization, 但是要注意dropout只在训练中使用，让一部分神经炎随机失活

   Batch Normalization是为了让输出都是单位高斯激活，方法是在链接和激活函数之间加入BatchNorm层，计算每个特征的均值和方差进行规则化。

### 4.CNN问题

1. 思想

   改变全链接为局部连接，这是由于图片的特殊性造成的（图像的一部分的统计特性与其他部分是一样的），通过局部连接和参数共享大范围的减少参数值。可以通过使用多个filter来提取图片的不同特征（多卷积核）。

2. filter尺寸的选择

   通常尺寸多为奇数（1，3，5，7）

3. 输出尺寸计算公式
   **输出尺寸=（N-F+padding*2）/ stride + 1**

   步长可以自由选择通过补零的方式来实现连接。

4. poolling池化的作用

   虽然通过卷积的方式可以大范围的减少输出尺寸（特征树），但是依然很难计算而且容易过拟合，所以依然利用图片的静态特性通过池化的方式进一步减少尺寸。

5. 常见的几个模型

   图像领域的深层神经网络

### 5.RNN问题

1. RNN原理

   **在普通的全链接网络或CNN中，每层神经元的信号只能向上一层传播，样本的处理在各个时刻独立，因此又被称为前向神经网络（Feed-forword + neural + networks）。而在RNN中，神经元的输出可以在下一个时间戳直接作用于自身，即第i层神经元在m时刻的输入，除了（i-1）层神经元在该时刻的输出外，还包括其自身在（m-1）时刻的输出。所以叫循环神经网络。**

2. RNN、LSTM、GRU区别

   - RNN引入了循环的概念，但是在实际过程中却出现了初始信息随时间消失的问题，即长期依赖（Long-Term Dependencies）问题，所以引入了LSTM。

   - LSTM：因为LSTM有进有出且当前的cell information是通过input gate控制之后叠加的，RNN是叠乘，因此LSTM可以防止梯度消失和爆炸的情况。

     ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/lstm_11.png)

   - GRU是LSTM的变体，将忘记门和输入门合成为一个单一的更新门。

     ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/gru_11.png)

3. LSTM防止梯度弥散和爆炸

   LSTM用加和的方式取代了乘积，使得很难出现梯度弥散。但是相应的更大的机率会出现梯度爆炸，但是可以通过给梯度假门限解决这一问题。

4. 引入word2vec

   这个也就是word embedding，是一种高效的从原始语料中学习字词空间向量的预测模型。分为CBOW（continous Bag of Words）和Skip-Gram形式。其中CBOW是从原始语句推测目标词汇，而Skip-Gram相反。CBOW可以用于小语料库，SKip-Gram用于大语料库。

### 6.GAN问题（不是很懂）

1. GAN的思想

   GAN结合了生成模型和判别模型，相当于矛与盾的撞击。生成模型负责生成最好的数据骗过判别模型，而判别模型负责识别那些是真的那些是生成模型生成的。但是这些只是在了解了GAN之后才体会到的，但是为什么这样会有效呢？

2. GAN的表达式

3. GAN的实际计算方法

### 7.决策树相关问题

1. 各种熵的计算

   熵、联合熵、条件熵、交叉熵、KL散度（相对熵）

   熵用于衡量不确定性，所以均分的时候熵最大

2. 常用的搭建树的方法：ID3、C4.5、CART

   **上述几种树分别利用信息增益、信息增益率、Gini指数作为数据分割标准**

   其中**信息增益衡量按照某个特征分割前后熵的减少程度为依据**

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/rf_1.png)

   用上述信息增益会出现优先选择具有较多属性的特征，毕竟分的越细的属性确定性越高。所以提出了信息增益率的概念，让含有较多属性的特征的作用降低。

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/rf_2.png)

   CART树在分类过程中使用的是基尼指数Gini，只能用于切分二叉树，而且和ID3、C4.5树不同，CART树不会在每一个步骤删除所用的特征。

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/rf_3.png)

3. 防止过拟合

   剪枝分为前剪枝和后剪枝，前剪枝本质上是早停止，后剪枝通常是通过衡量剪枝后损失函数变化来决定是否剪枝。后剪枝有：错误率降低剪枝、悲观剪枝、代价复杂度剪枝。

4. 剪枝的几个停止条件 **不懂

   节点中样本同一类

   特征不足返回多类

   如果某个分支没有值则返回父节点中的多类

   样本个数小于阈值返回多类

### 8.逻辑回归相关的问题

1. 公式推导

2. 逻辑回归的基本概念

3. L1-norm和L2-norm

   其实稀疏的根本还是在于L0-norm也就是直接统计参数不为0的个数作为规则项，但实际上却不好执行于是引入了L1-norm；而L1norm本质上是假设参数先验是服从Laplace分布的，而L2-norm是假设参数先验为Gaussian分布，我们在网上看到的通常用图像来解答这个问题的原理就在这。 
   　　但是L1-norm的求解比较困难，可以用坐标轴下降法或是最小角回归法求解。

4. LR和SVM对比

   首先，LR和SVM最大的区别在于损失函数的选择，LR的损失函数为Log损失（或者说是逻辑损失都可以）、而SVM的损失函数为hinge loss。 

   ![](https://github.com/spurscoder/spurscoder.github.io/raw/master/img/home/svm_1.png)

   其次，两者都是线性模型。 
   最后，SVM只考虑支持向量（也就是和分类相关的少数点） 　

5. LR和随机森林区别

   随机森林等树算法都是非线性的，而LR是线性的。LR更侧重全局优化，而树模型主要是局部的优化。

6. 常见的优化方法

   逻辑回归本身是可以用公式求解的，但是因为需要求逆的复杂度太高，所以才引入了梯度下降算法。 
   　　一阶方法：梯度下降、随机梯度下降、mini 随机梯度下降降法。随机梯度下降不但速度上比原始梯度下降要快，局部最优化问题时可以一定程度上抑制局部最优解的发生。 
   　　二阶方法：牛顿法、拟牛顿法： 
   　　这里详细说一下牛顿法的基本原理和牛顿法的应用方式。牛顿法其实就是通过切线与x轴的交点不断更新切线的位置，直到达到曲线与x轴的交点得到方程解。在实际应用中我们因为常常要求解凸优化问题，也就是要求解函数一阶导数为0的位置，而牛顿法恰好可以给这种问题提供解决方法。实际应用中牛顿法首先选择一个点作为起始点，并进行一次二阶泰勒展开得到导数为0的点进行一个更新，直到达到要求，这时牛顿法也就成了二阶求解问题，比一阶方法更快。我们常常看到的x通常为一个多维向量，这也就引出了Hessian矩阵的概念（就是x的二阶导数矩阵）。缺点：牛顿法是定长迭代，没有步长因子，所以不能保证函数值稳定的下降，严重时甚至会失败。还有就是牛顿法要求函数一定是二阶可导的。而且计算Hessian矩阵的逆复杂度很大。 
   拟牛顿法： 不用二阶偏导而是构造出Hessian矩阵的近似正定对称矩阵的方法称为拟牛顿法。拟牛顿法的思路就是用一个特别的表达形式来模拟Hessian矩阵或者是他的逆使得表达式满足拟牛顿条件。主要有DFP法（逼近Hession的逆）、BFGS（直接逼近Hession矩阵）、 L-BFGS（可以减少BFGS所需的存储空间）。

### 9.SVM相关问题

1. 带核的SVM为什么能分类非线性问题

   核函数的本质是两个函数的內积，而这个函数在SVM中可以表示成对于输入值的高维映射。注意核并不是直接对应映射，核只不过是一个內积 

2. RBF核一定是线性可分的吗

   不一定，RBF核比较难调参而且容易出现维度灾难，要知道无穷维的概念是从泰勒展开得出的。

3. 常见的核函数及核函数的条件

   核函数选择的时候应该从线性核开始，而且在特征很多的情况下没有必要选择高斯核，应该从简单到难的选择模型。我们通常说的核函数指的是正定和函数，其充要条件是对于任意的x属于X，要求K对应的Gram矩阵要是半正定矩阵。

   - RBF核径向基，这类函数取值依赖于特定点间的距离，所以拉普拉斯核其实也是径向基核。
   - 线性核：主要用于线性可分的情况
   - 多项式核

4. SVM的基本思想

   间隔最大化来得到最优分离超平面。方法是将这个问题形式化为一个凸二次规划问题，还可以等价位一个正则化的合页损失最小化问题。SVM又有硬间隔最大化和软间隔SVM两种。这时首先要考虑的是如何定义间隔，这就引出了函数间隔和几何间隔的概念（这里只说思路），我们选择了几何间隔作为距离评定标准（为什么要这样，怎么求出来的要知道），我们希望能够最大化与超平面之间的几何间隔x，同时要求所有点都大于这个值，通过一些变化就得到了我们常见的SVM表达式。接着我们发现定义出的x只是由个别几个支持向量决定的。对于原始问题（primal problem）而言，可以利用凸函数的函数包来进行求解，但是发现如果用对偶问题（dual ）求解会变得更简单，而且可以引入核函数。而原始问题转为对偶问题需要满足KKT条件（这个条件应该细细思考一下）到这里还都是比较好求解的。因为我们前面说过可以变成软间隔问题，引入了惩罚系数，这样还可以引出hinge损失的等价形式（这样可以用梯度下降的思想求解SVM了）。我个人认为难的地方在于求解参数的SMO算法。

5. 是否所有的优化问题可以转化为对偶问题

   这个问题我感觉非常好，有了强对偶和弱对偶的概念。用[知乎大神的解释吧](https://www.zhihu.com/question/43830699) 

6. 处理数据偏斜

   可以对数量多的类使得惩罚系数C越小表示越不重视，相反另数量少的类惩罚系数变大。

### 10.Boosting和Bagging

1. 随机森林

   随机森林改变了决策树容易过拟合的问题，这主要是由两个操作所优化的：

   1、Boostrap从袋内有放回的抽取样本值 

   2、每次随机抽取一定数量的特征（通常为sqr(n)）。 
   　　分类问题：采用Bagging投票的方式选择类别频次最高的 
   　　回归问题：直接取每颗树结果的平均值。

   | 常见参数                                                     | 误差分析                                                     | 优点                                                         | 缺点                     |
   | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------ |
   | 1、树最大深度2、树的个数 3、节点上的最小样本数4、特征数(sqr(n)) | oob(out-of-bag)将各个树的未采样样本作为预测样本统计误差作为误分率 | 可以并行计算不需要特征选择可以总结出特征重要性可以处理缺失数据不需要额外设计测试集 | 在回归上不能输出连续结果 |

2. Boosting之Adaboost

   Boosting的本质实际上是一个加法模型，通过改变训练样本权重学习多个分类器并进行一些线性组合。而Adaboost就是加法模型+指数损失函数+前项分布算法。Adaboost就是从弱分类器出发反复训练，在其中不断调整数据权重或者是概率分布，同时提高前一轮被弱分类器误分的样本的权值。最后用分类器进行投票表决（但是分类器的重要性不同）。 

3. Boosting之GBDT

   将基分类器变成二叉树，回归用二叉回归树，分类用二叉分类树。和上面的Adaboost相比，回归树的损失函数为平方损失，同样可以用指数损失函数定义分类问题。但是对于一般损失函数怎么计算呢？GBDT（梯度提升决策树）是为了解决一般损失函数的优化问题，方法是用损失函数的负梯度在当前模型的值来模拟回归问题中残差的近似值。 
   　　**注：**由于GBDT很容易出现过拟合的问题，所以推荐的GBDT深度不要超过6，而随机森林可以在15以上。

4. GBDT和RF的区别

5. Xgboost

   这个工具主要有以下几个特点：

   - 支持线性分类器
   - 可以自定义损失函数，并且可以用二阶偏导
   - 加入了正则化项：叶节点数、每个叶节点输出score的L2-norm
   - 支持特征抽样
   - 在一定情况下支持并行，只有在建树的阶段才会用到，每个节点可以并行的寻找分裂特征。

### 11.KNN和Kmeans

1. KNN和Kmeans缺点

   都属于惰性学习机制，需要大量的计算距离过程，速度慢的可以（但是都有相应的优化方法）。

2. KNN

   KNN不需要进行训练，只要对于一个陌生的点利用离其最近的K个点的标签判断其结果。KNN相当于多数表决，也就等价于经验最小化。而KNN的优化方式就是用Kd树来实现。

3. Kmean

   要求自定义K个聚类中心，然后人为的初始化聚类中心，通过不断增加新点变换中心位置得到最终结果。Kmean的缺点可以用Kmean++方法进行一些解决（思想是使得初始聚类中心之间的距离最大化）

### 12.EM算法、HMM、CRF

1. EM算法

   　　EM算法用于含有隐变量模型的极大似然估计或者极大后验估计，有两步组成：E步，求期望（expectation）；M步，求极大（maxmization）。本质上EM算法还是一个迭代算法，通过不断用上一代参数对隐变量的估计来对当前变量进行计算，直到收敛。 
      　　注意：EM算法是对初值敏感的，而且EM是不断求解下界的极大化逼近求解对数似然函数的极大化的算法，也就是说**EM算法不能保证找到全局最优值**。对于EM的导出方法也应该掌握。 

2. HMM算法

   　　隐马尔可夫模型是用于标注问题的生成模型。有几个参数（π，A，B）：初始**状态**概率向量π，状态转移矩阵A，观测概率矩阵B。称为马尔科夫模型的三要素。 
      马尔科夫三个基本问题：

   - 概率计算问题：给定模型和观测序列，计算模型下观测序列输出的概率。$\to$ 前向后向算法
   - 学习问题：已知观测序列，估计模型参数，即用极大似然估计来估计参数。$\to$ Baum-Welch(也就是EM算法)和极大似然估计。
   - 预测问题：已知模型和观测序列，求解对应的状态序列。$\to$ 近似算法（贪心算法）和维比特算法（动态规划求最优路径）

3. CRF算法

   　　给定一组输入随机变量的条件下另一组输出随机变量的条件概率分布密度。条件随机场假设输出变量构成马尔科夫随机场，而我们平时看到的大多是线性链条随机场，也就是由输入对输出进行预测的判别模型。求解方法为极大似然估计或正则化的极大似然估计。 
      　　之所以总把HMM和CRF进行比较，主要是因为CRF和HMM都利用了图的知识，但是CRF利用的是马尔科夫随机场（无向图），而HMM的基础是贝叶斯网络（有向图）。而且CRF也有：概率计算问题、学习问题和预测问题。大致计算方法和HMM类似，只不过不需要EM算法进行学习问题。

4. HMM和CRF对比

   其根本还是在于基本的理念不同，一个是生成模型，一个是判别模型，这也就导致了求解方式的不同。

### 13.常见的其他ML基础问题

1. 数据归一化（或者标准化、注意归一化和标准化的不同）的原因

   　　要强调：**能不归一化最好不归一化**，之所以进行数据归一化是因为各维度的量纲不相同。而且需要看情况进行归一化。

   - 有些模型在各维度进行了不均匀的伸缩后，最优解与原来不等价（如SVM）需要归一化。
   - 有些模型伸缩有与原来等价，如：LR则不用归一化，**但是**实际中往往通过迭代求解模型参数，如果目标函数**太扁**（想象一下很扁的高斯模型）迭代算法会发生不收敛的情况，所以最坏进行数据归一化。

   补充：其实本质是由于loss函数不同造成的，SVM用了欧拉距离，如果一个特征很大就会把其他的维度dominated。而LR可以通过权重调整使得损失函数不变。

2. 衡量跟分类器的好坏

   　　这里首先要知道TP、FN（真的判成假的）、FP（假的判成真）、TN四种（可以画一个表格）。 
      几种常用的指标：

   - 精度precision = TP/(TP+FP) = TP/~P （~p为预测为真的数量）
   - 召回率 recall = TP/(TP+FN) = TP/ P
   - F1值： 2/F1 = 1/recall + 1/precision
   - ROC曲线：ROC空间是一个以伪阳性率（FPR，false positive rate）为X轴，真阳性率（TPR, true positive rate）为Y轴的二维坐标系所代表的平面。其中真阳率TPR = TP / P = recall， 伪阳率FPR = FP / N

3. SVD和PCA

   　　PCA的理念是使得数据投影后的方差最大，找到这样一个投影向量，满足方差最大的条件即可。而经过了去除均值的操作之后，就可以用SVD分解来求解这样一个投影向量，选择特征值最大的方向。

4. 防止过拟合的方法

   　　过拟合的原因是算法的学习能力过强；一些假设条件（如样本独立同分布）可能是不成立的；训练样本过少不能对整个空间进行分布估计。 
      　　处理方法：

   - 早停止：如在训练中多次迭代后发现模型性能没有显著提高就停止训练
   - 数据集扩增：原有数据增加、原有数据加随机噪声、重采样
   - 正则化
   - 交叉验证
   - 特征选择/特征降维

5. 数据不平衡问题

   　　这主要是由于数据分布不平衡造成的。解决方法如下：

   - 采样，对小样本加噪声采样，对大样本进行下采样
   - 进行特殊的加权，如在Adaboost中或者SVM中
   - 采用对不平衡数据集不敏感的算法
   - 改变评价标准：用AUC/ROC来进行评价
   - 采用Bagging/Boosting/ensemble等方法
   - 考虑数据的先验分布

### 14.常见算法最好的讲解[地址](https://blog.csdn.net/woaidapaopao/article/details/63690692)

## 04-13

## 04-14 各种回归问题终结

### 15.线性回归

> 线性回归才是真正的回归，而不像逻辑回归用于分类，其基本思想是用梯度下降法对最小二乘法形式的误差函数进行优化。单变量线性回归的基本形式是$y = ax + b$，用来拟合数据，比如房屋的面积和价格的关系

[***线性回归博客***](https://blog.csdn.net/xbinworld/article/details/43919445)

###16.ridge regression && Lasso regression

- ridge regression是在线性回归的基础上加了L2-norm

  $$J_R(w)=\frac{1}{2}\|y-Xw\|^2+\frac{\lambda}{2}\|w\|^2$$

  $$\min_{w} \frac{1}{2}\|y-Xw\|^2, \quad s.t. \|w\|_2<\theta$$

- Lasso regression是在线性回归的基础上加了L1-norm

  $$J_L(w)=\frac{1}{2}\|y-Xw\|^2+\lambda\sum_{i}|w_i|$$

  $$\min_{w} \frac{1}{2}\|y-Xw\|^2, \quad s.t. \|w\|_1<\theta$$

  [讲解地址](https://blog.csdn.net/xbinworld/article/details/44276389)

### 17. Logistic regression && Softmax regression

$$\min_{w} \quad L(w) = -\log \prod_{i=1}^{N}h(x_i)^{y_i}（1 - h(x_i))^{1-y_i}\\$$
$$= -\sum_{i=1}^{N}[y_i\log h(x_i) +(1-y_i)\log (1-h(x_i))]\\$$

$$\nabla L(w) = \frac{\partial L}{\partial w} = \frac{1}{N}\sum_{i=1}^{N}(h(x_i) - y_i)x_i \\$$
$$w = w - \alpha\cdot \nabla L(w)$$

**[LR是广义线性回归模型](https://blog.csdn.net/cdd2xd/article/details/75635688)**

[讲解地址1](https://blog.csdn.net/danieljianfeng/article/details/41901063)

[讲解地址2](https://blog.csdn.net/xbinworld/article/details/45291009)

[美团技术团队的讲解](https://tech.meituan.com/intro_to_logistic_regression.html)

$$p(y^{(i)}=j|x^{(i)};w) = \frac{e^{w_j^Tx^{(i)}}}{\sum_{l=1}^{k}e^{w_l^Tx^{(i)}}}$$

$$\min_{w} \quad J(w) = -\frac{1}{N}\sum_{i=1}^{N}\sum_{j=1}^{k}\left[{\textbf{1}\{y^{(i)}=1\}}\log\frac{e^{w_j^Tx^{(i)}}}{\sum_{l=1}^{k}e^{w_l^Tx^{(i)}}}\right] + \frac{\lambda}{2}\sum_{j=1}^{k}\sum_{v=1}^{m}w_{jv}^2$$

### 18.

### 19.

### 20.正态**分布**

> （英语：normal distribution）又名**高斯分布**（英语：**Gaussian** distribution), 是一个非常常见的连续概率**分布**。 正态**分布**在统计学上十分重要，经常用在自然和社会科学来代表一个不明的随机变量。

### 21.伯努利分布

> 亦称“零一分布”、“两点分布”。称随机变量X有伯努利分布, 参数为p(0<p<1),如果它分别以概率p和1-p取1和0为值。EX= p,DX=p(1-p)。伯努利试验成功的次数服从伯努利分布,参数p是试验成功的概率。伯努利分布是一个离散型机率分布，是N=1时[二项分布](https://baike.baidu.com/item/%E4%BA%8C%E9%A1%B9%E5%88%86%E5%B8%83)的特殊情况，为纪念[瑞士](https://baike.baidu.com/item/%E7%91%9E%E5%A3%AB)科学家詹姆斯·[伯努利](https://baike.baidu.com/item/%E4%BC%AF%E5%8A%AA%E5%88%A9)(Jacob Bernoulli 或James Bernoulli)而命名。

### 22.

### 23.

### 24.



## 04-15

