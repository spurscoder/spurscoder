---
layout: post
title: "05.14到05.20.home"
author: "Spurs"
date: 2018-05-20 12:40:00
description:
photos:
links:
categories:
tags:
---

> 05.14到05.20.home
>

<!-- more -->

#### 05.13

##### mixing cout and wcout

```c++
// cout  << s  << std::endl;  // You shouldn't be able to
wcout << ws << std::endl;     // run these at the same time
```

When `cout` or `wcout` is called for the first time, the orientation for `stdout` becomes set. In the case of `cout`, `stdout` becomes a byte-oriented stream, and in the case of `wcout`, `stdout`becomes a wide-oriented stream. As per the C++ standard [27.4.1] and C standard [7.19.2], once the orientation of a stream is set, you should not call a function which is not compatible with the orientation of that stream.

##### size_t && ssize_t

----------------------------------size_t--------------------------------------

size_t是一些C/C++标准在stddef.h中定义的。这个类型足以用来表示对象的大小。

size_t的真实类型与操作系统有关，在32位架构中被普遍定义为：

typedef   unsigned int size_t;

而在64位架构中被定义为：

typedef  unsigned long size_t;

size_t在32位架构上是4字节，在64位架构上是8字节，在不同架构上进行编译时需要注意这个问题。

而int在不同架构下都是4字节，与size_t不同；且int为带符号数，size_t为无符号数。

参考：[size_t在WikiPedia上的词条](http://en.wikipedia.org/wiki/Size_t)

size_t是无符号的，并且是平台无关的，表示0-MAXINT的范围；

int是有符号的；

具体可参考：http://123.125.115.53/view/3236587.htm

---------------------------------------ssize_t------------------------------------------------------------

ssize_t是有符号整型，在32位机器上等同与int，在64位机器上等同与long int，有没有注意到，它和long数据类型有啥区别？其实就是一样的。size_t 就是无符号型的ssize_t，也就是unsigned long/ unsigned int (在32位下），不同的编译器或系统可能会有区别，主要是因为在32位机器上int和long是一样的。

  typedef  long  ssize_t;//ssize_t就是long类型

-----------------------------------size_t和ssize_t----------------------------------------------

size_t是什么类型的？

解释一：为了增强程序的可移植性，便有了size_t，它是为了方便系统之间的移植而定义的，不同的系统上，定义size_t可能不一样。

     在32位系统上 定义为 unsigned int 也就是说在32位系统上是32位无符号整形。在64位系统上定义为 unsigned long 也就是说在64位系统上是64位无符号整形。size_t一般用来表示一种计数，比如有多少东西被拷贝等。例如：sizeof操作符的结果类型是size_t，该类型保证能容纳实现所建立的最大对象的字节大小。 它的意义大致是“适于计量内存中可容纳的数据项目个数的无符号整数类型”。所以，它在数组下标和内存管理函数之类的地方广泛使用。而ssize_t这个数据类型用来表示可以被执行读写操作的数据块的大小.它和size_t类似,但必需是signed.意即：它表示的是signed size_t类型的。

typedef unsigned long size_t

解释二：ssize_t是signed size_t。

size_t是标准C库中定义的，应为unsigned int。定义为typedef int ssize_t。

而ssize_t:这个数据类型用来表示可以被执行读写操作的数据块的大小.它和size_t类似,但必需是signed.意即：它表示的是sign size_t类型的。

《Unix 高级环境编程》里面是这么说的：

原始系统数据类型
前面所示的getpid函数的原型定义了其返回值为pid_t类型，这也是POSIX中的新规定。
UNIX的早期版本规定此函数返回一整型。与此类似， read和write返回类型为ssize_t的值，并
要求第三个参数的类型是size_t。
以_ t结尾的这些数据类型被称为原始系统数据类型。它们通常在头文件<sys/types.h>中定
义(头文件<unistd.h>应已包括该头文件)。它们通常以C typedef说明加以定义。typedef说明在C
语言中已超过1 5年了(所以这并不要求ANSI C)，它们的目的是阻止程序使用专门的数据类型
(例如int , short或long) 来允许对于一种特定系统的每个实现选择所要求的数据类型。在需要存储
进程I D的地方，分配类型为pid_t的一个变量(注意，程序1 - 5已对名为pid的变量这样做了)。在
各种不同的实现中，这种数据类型的定义可能是不同的，但是这种差别现在只出现在一个头文
件中。我们只需在另一个系统上重新编辑应用程序。

转：http://blog.csdn.net/wypblog/article/details/6818761

=============================================================

C语言中size_t的陷阱

今天写了一个类似这样的程序：

> ```
> #include <stdio.h>
> #include <string.h>
> int main()
> {
>     int i = -1;
>     if(i > strlen("Demon"))
>         printf("Hello World");
>     else
>         printf("Hello Demon");
>     return 0;
> }
> ```

输出的竟然是Hello World！-1 > 5？！

仔细想想，原来问题出在strlen上，strlen返回的类型是size_t，size_t的定义为：

> ```
> typedef unsigned int size_t;
> ```

即无符号的整型，而i的类型是int，即有符号的整型。当有符号整型和无符号整型进行运算时，有符号整型会先自动转化成无符号。-1转化成无符号数为4294967295，远远大于5。

今后遇到有符号数和无符号数之间的运算时要千万小心。

##### 基本的内置类型

C++ 为程序员提供了种类丰富的内置数据类型和用户自定义的数据类型。下表列出了七种基本的 C++ 数据类型：

| 类型   | 关键字     |
| ---- | ------- |
| 布尔型  | bool    |
| 字符型  | char    |
| 整型   | int     |
| 浮点型  | float   |
| 双浮点型 | double  |
| 无类型  | void    |
| 宽字符型 | wchar_t |

| 类型                 | 位         | 范围                                       |
| ------------------ | --------- | ---------------------------------------- |
| char               | 1 个字节     | -128 到 127 或者 0 到 255                    |
| unsigned char      | 1 个字节     | 0 到 255                                  |
| signed char        | 1 个字节     | -128 到 127                               |
| int                | 4 个字节     | -2147483648 到 2147483647                 |
| unsigned int       | 4 个字节     | 0 到 4294967295                           |
| signed int         | 4 个字节     | -2147483648 到 2147483647                 |
| short int          | 2 个字节     | -32768 到 32767                           |
| unsigned short int | 2 个字节     | 0 到 65,535                               |
| signed short int   | 2 个字节     | -32768 到 32767                           |
| long int           | 8 个字节     | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807 |
| signed long int    | 8 个字节     | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807 |
| unsigned long int  | 8 个字节     | 0 to 18,446,744,073,709,551,615          |
| float              | 4 个字节     | +/- 3.4e +/- 38 (~7 个数字)                 |
| double             | 8 个字节     | +/- 1.7e +/- 308 (~15 个数字)               |
| long double        | 16 个字节    | +/- 1.7e +/- 308 (~15 个数字)               |
| wchar_t            | 2 或 4 个字节 | 1 个宽字符                                   |

从上表可得知，变量的大小会根据编译器和所使用的电脑而有所不同。

##### wstring, wiftream, wostream, wcin, wout 宽字符

##### ifstream 最后一行读取两次的问题

- 解决办法一

  ```c++
  ifstream m_fileConfig;
  string str;
  m_fileConfig.open(FILE_OPERATORS);
  while(!m_fileConfig.eof()){
    m_fileConfig >> str;
    if(m_fileConfig.fail()) {
      break;
    }
    // if (!m_fileConfig) break;
    cout << str << endl;
  }
  ```

- 最好的办法

  ```
  while (input >> str) {
   std::cout << str;
  }
  ```

##### 文件重定向 C/C++

```c++
在C++中
直接用ifstream读取文件即可，
直接用ofstream输出到文件即可。
```

##### C++中的中文输出输入问题

```c++
// Ubuntu 单独设置wcout，wcin不管用
#include <locale>
locale::global(locale("zh_CN.UTF-8"));

// windows 
// 好像可以单独设置各个编码格式
#include <locale>
wcin.imbue(locale("chs"));
wcout.imbue(locale("chs"));

// macos 只能单独设置
#include <locale>
wcin.imbue(locale("zh_CN.UTF-8"));
wcout.imbue(locale("zh_CN.UTF-8"));
```

> 整体来看，不同的操作系统对应的locale差异不同
>
> 但是可以通过实现自己的转换API来实现对中文的支持。

```c++
std::wstring StringToWString(const std::string& str)
{
    setlocale(LC_ALL, "chs");
    const char* point_to_source = str.c_str();
    size_t new_size = str.size() + 1;
    wchar_t *point_to_destination = new wchar_t[new_size];
    wmemset(point_to_destination, 0, new_size);
    mbstowcs(point_to_destination, point_to_source, new_size);
    std::wstring result = point_to_destination;
    delete[]point_to_destination;
    setlocale(LC_ALL, "C");
    return result;
}
```

```c++
#include <iostream>  
#include <string>  
int main() {  
    std::string s = "Chelse";  
    const char *str = s.c_str();  
    std::cout << str << std::endl;  
    s[1] = 'm';  
    std::cout << str << std::endl;  

    return 0;  
} 
/*
第一个输出 当然是 Chelse；
第二个输出呢: Chelse还是Cmelse呢？
答案是Cmelse。
*/
```