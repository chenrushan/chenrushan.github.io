---
layout: post
title: 基于 Prefix Double 及 Counting Sort 构建 Suffix Array
categories: ds
tags: suffix array, prefix doubling, counting sort, radix sort
---

### Counting Sort

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

2. 在第 2, 3 个元素上做 counting sort，并 update S 数组。

   <object data="/resource/SA/second_iter.svg" type="image/svg+xml"></object>

   注意这个步骤的 counting sort 不同于上面的伪代码，区别在最后一个 for 循环，不能再简单得从第 0 个序列循环到第 N - 1 个，而是需要借助第一步中得到 S，代码如下：

        for (r = 0; r < N; r++)
            S2[--count[I[S[r]]]] = S[r]

   这里的 I[i] 不是完整的 I[i]，而是局部，如：I[0] = 67。

   如果按照标准的做法，你会发现 896706 和 306785 的序是反着的，**所以前一轮得到的 S 数组的作用就是在当前迭代中将相同的局部元素区分开**。

