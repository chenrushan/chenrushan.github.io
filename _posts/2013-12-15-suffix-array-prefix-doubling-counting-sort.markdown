---
layout: post
title: 基于 Prefix Doubling 及 Counting Sort 构建 Suffix Array
categories: ds
tags: suffix array, prefix doubling, counting sort, radix sort
---

### Introduction

这篇笔记分 4 小节：

1. 开始简要介绍一下 suffix array。

2. 然后介绍 suffix array 的一个特性，即 prefix doubling。

3. 之后介绍 counting sort，这是我对一些特定的 counting sort (如 radix sort) 共性的一些总结。

4. 最后给出基于 prefix doubling 和 counting sort 的 suffix array 构建过程。

### 1. Suffix Array

给定一个 string，它的 suffix 就是从 string 的某一位置开始到结尾的一个 substring。如，对于 "science"，"ence" 就是其中一个 suffix，其所有的 suffix 包括：

> science, cience, ience, ence, nce, ce, e

对 suffix 集合排个序就得到了 suffix array，由于每个 suffix 的结尾都是相同的，所以只需要一个开始位置即可表示一个 suffix。如 "ence" 可以用 3 表示，因此 suffix array 可以表示为一个整形数组，上面的 suffix 集合对应的 suffix array 是 (5, 1, 6, 3, 2, 4, 0)。

<object data="/resource/SA/science_SA.svg" type="image/svg+xml" class="blkcenter"></object>

Suffix array 的构建方法有很多，最快的貌似是线性的，这篇笔记给出基于 prefix doubling 及 counting sort 的构建方法并不是最快的，之所以搞这个算法，原因主要是，一来**它很有意思**，二来在实现它的过程感觉受益匪浅，主要收获包括：

* 任何时候都要明确一个数组的索引的含义，及数组中包含的元素的含义。这无论对你写代码还是理解别人代码都非常重要，尤其是当：

  * 遇到嵌套数组时，如：`arr3[arr2[arr1[i]]]`
  * 当程序中使用多个数组时
  * 在处理与数组有关的循环时

* 数组的索引不要一味得以 i, j 命名，当数组多的时候你就乱了。如果索引表示 rank 就用 r 表示，如果表示 length 就用 l，总之不要一味用 i, j。

### 2. Prefix Doubling


### 3. Counting Sort

* Input

  数组 I。为方便起见，后续均以整数输入为例。

* Output

  数组 S。S 中存 I 的序，S[r] = i 表示排在第 r 位的数为 I[i]。

例如，I = (234, 7890, 12, 5678)，则 S = (2, 0, 3, 1)

#### 简单 Counting Sort

最简单的 counting sort 可以用如下伪代码表示。

    for (i = 0; i < N; i++)
        count[I[i]] += 1
    for (i = 0; i < V; i++)
        count[i] += count[i - 1]
    for (i = 0; i < N; i++)
        S[--count[I[i]]] = i

该算法的时间空间复杂度均为 `O(V)`。V 表示所有可能的不同的输入的个数。如果你的输入为不限大小的 int，则 V = 2<sup>32</sup>, 如果你的输入为长度 <= 10 的 ascii string，则 V = 26<sup>10</sup>，类似的输入随处可见，因此，这个算法虽然简单，但实用性不高。下面给出改进的 counting sort。

#### 改进的 Counting Sort

假设 I[i] 是可以拆分的序列，所谓可拆分，比如 125 可以被拆成 1, 2, 5，"abc" 可以被拆成 "a", "b", "c"。并且序列中的每个元素有权重大小之分，如 125 = 1\*100 + 2\*10 + 5\*1，所以 1 的权重最高，2 次之，5 最低；对于字符串，权重从左到右依次递减。权重越高在排序中所起的作用也就越大，如 125, 211，虽然 25 > 11，但因为 1 < 2，所以 125 还是小于 211。

为了规避不必要的细节，对 I 做这么一个限制：I 中所有序列都是等长的 (长度不同可以补成相同，比如 125 和 2543，在 125 前面加个 0 就变成和 2543 等长了)。

改进的 counting sort 是一个迭代的过程，每次迭代在每个序列的某个局部做 count (局部指的是序列中连续的几个元素)，然后结合之前迭代得到的局部排序结果，推导出一个更大的局部的序，不断迭代直到得到全局的序，因为只在序列的局部做 count，所以时间和空间的使用都大大减少。这段话很抽象，看个例子吧。

令 I = (896706, 160243, 393894, 803201, 292963, 306785)，每次迭代的时候在 2 个元素上 count，改进的 counting sort 迭代如下：

1. 在最后 2 个元素做 counting sort，并将局部排序结果存于 S 中。

   <object data="/resource/SA/first_iter.svg" type="image/svg+xml"></object>

2. 在第 2, 3 个元素上做 counting sort，并 update S 数组。这步迭代完事后，S 中就包含了后 4 个元素的序 (相比于第 1 步迭代的一个更大的局部)。

   <object data="/resource/SA/second_iter.svg" type="image/svg+xml"></object>

   注意这个步骤的 counting sort 不同于上面的伪代码，区别在最后一个 for 循环，不能再简单得从第 0 个序列循环到第 N - 1 个，而是需要借助第一步中得到 S，代码如下：

        for (r = 0; r < N; r++)
            S2[--count[I[S[r]]]] = S[r]
        S = S2

   这里的 I[i] 不是完整的 I[i]，而是局部，如：I[0] = 67。

   如果按照标准的做法，你会发现 896706 和 306785 的序是反着的，**所以前一轮得到的 S 数组的作用就是在当前迭代中将相同的局部元素区分开**。

3. 重复与第 2 步相同的迭代，得到对应 6 个元素的 S，也就是最终的序 S = (1, 4, 5, 2, 3, 0)。

这个例子中，count 数组的大小只要 100 即可，每轮迭代耗时 O(N + 100) = O(N)，如果序列长度为 L，则总时间为 O(LN)。你也可以每轮迭代在 1 个元素上做 counting sort，也可以 3 个都可以。

上述例子从权重低的局部开始迭代到权重高的局部，对于一般的 counting sort 并没有这个要求，下面的 suffix array 的构建就不是这么迭代的。但有一点是相同的，那就是**为了得到一个更大的局部的序，需要权重高的那个局部的 count 信息和权重低的那个局部的 S 数组**，这对于所有的 counting sort 都一样。


