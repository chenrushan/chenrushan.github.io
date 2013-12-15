---
layout: post
title: 基于 Prefix Double 及 Counting Sort 构建 Suffix Array
categories: arch
tags: suffix array, prefix doubling, counting sort, radix sort
---

### Counting Sort

* Input

  数组 I。为方便起见，后续均以整数输入为例。

* Output

  数组 S。S 中存 I 的序，S[r] = i 表示排在第 r 位的数为 I[i]。

例如，I = (234, 7890, 12, 5678)，则 S = (2, 0, 3, 1)


最简单的 counting sort 可以用如下伪代码表示。

    for (i = 0; i < N; i++)
        count[I[i]] += 1
    for (i = 0; i < V; i++)
        count[i] += count[i - 1]
    for (i = 0; i < N; i++)
        S[--count[I[i]]] = i

