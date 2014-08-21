---
layout: post
title: Creating Suffix Array Based on Prefix Doubling and Counting Sort
categories: ds
tags: suffix array, prefix doubling, counting sort, radix sort
---

### Introduction

这篇笔记分 4 小节：

1. 开始简要介绍一下 suffix array，并定义一些后面用到的变量。

2. 然后介绍 suffix array 的一个特性，这一特性是 prefix doubling 算法的基础。

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

#### 变量定义

为了后续描述方便，这里定义一些变量。以下的例子都可以参考下面这个图。

<object data="/resource/SA/SA_variable_example.svg" type="image/svg+xml" class="blkcenter"></object>

* `str`

    表示要构建 suffix array 的 string。

    - `str[i:j]`

        表示从 i (inclusive) 到 j (exclusive) 的 substring。
        
        如：str = "science", str[1:3] = "ci"。

* `S`

    S = (str[0:n], str[1:n], ..., str[n-1:n]) 表示 str 的 suffix 序列。
    
    如：S = (science, cience, ience, ence, nce, ce, e), S[1] = "cience"。

    + <span class="code">S<sub>i:j</sub></span>

        S<sub>i:j</sub> = (S[0][i:j], S[1][i:j], ..., S[n-1][i:j]) 表示所有 suffix 的 [i:j] 子串序列

        str[i:j] = str[i:len(str)] if j > len(str)

        str[i:j] = NULL (空串) if i >= len(str)

        如：S<sub>2:4</sub> = (ie, en, nc, ce, e, NULL, NULL)

    + <span class="code">S<sub>l</sub></span>
  
        S<sub>l</sub> = S<sub>0:l</sub>，就是个缩写。

        如：S<sub>2</sub> = (sc, ci, ie, en, nc, ce, e)

* `SA`

    表示 suffix array，SA[r] 存储 S 的索引值，指向第 r 小 (从 0 开始记) 的 suffix。

    如：SA = (5, 1, 6, 3, 2, 4, 0)，SA[3] = 3 (表示第 3 小的后缀是 ence)

    + <span class="code">SA<sub>i:j</sub></span>

        表示 S<sub>i:j</sub> 对应的 suffix array

        如：SA<sub>2:4</sub> = (5, 6, 3, 4, 1, 0, 2)

    + <span class="code">SA<sub>l</sub></span>

        SA<sub>l</sub> = SA<sub>0:l</sub> 就是个缩写。

        如：SA<sub>2</sub> = (5, 1, 6, 3, 2, 4, 0)
        
* `R`
    
    表示 rank 数组，R[i] 存储 S[i] 的 rank 信息。

    如：R = (6, 1, 4, 3, 5, 0, 2)，注意到 SA[R[i]] = i

    同 SA 类似，也有<span class="code">R<sub>i:j</sub></span>和<span class="code">R<sub>l</sub></span>，注意到 S<sub>i:j</sub> 和 S<sub>l</sub> 可能有相同的元素，比如 S<sub>1</sub> 中就有两个 e，不同于 SA，对于相同的元素，<span class="code">R<sub>i:j</sub></span>和<span class="code">R<sub>l</sub></span> 值是相等的。

### 2. Prefix Doubling

观察 suffix 集合 S，很容易发现这么一个特点：S[i] 去掉第一个字符就成了 S[i+1]，去掉两个字符就成了 S[i+2]，去掉 n 个字符就成了 S[i+n]。

<object data="/resource/SA/prefix_equal.svg" type="image/svg+xml" class="blkcenter"></object>

因此，对于任意一个 l 都有 S[i][n:n+l] = S[i+n][0:l] 。而 S[i][n:n+l] 即为 S<sub>n:n+l</sub>[i]， S[i+n][0:l] 即为 S<sub>l</sub>[i+n]，当 n=l 时，就有：

<blockquote class="code">
S<sub>l</sub>[i+l] = S<sub>l:2l</sub>[i] 或者 S<sub>l</sub>[i] = S<sub>l:2l</sub>[i-l]
</blockquote>

这个性质就是 prefix doubling 算法的基础。

由这个性质也可以知道，S<sub>l:2l</sub> 中的非空元素全部都出现在 S<sub>l</sub> 中，空元素共 l 个，参考变量定义小节那幅图中的 S<sub>2</sub> 和 S<sub>2:4</sub>。

### 3. Counting Sort

* Input

    数组 I。为方便起见，后续均以整数输入为例。

* Output

    数组 K。K 中存 I 的序，K[r] = i 表示排在第 r 位的数为 I[i]。

例如，I = (234, 7890, 12, 5678)，则 K = (2, 0, 3, 1)

#### 简单 Counting Sort

最简单的 counting sort 可以用如下伪代码表示。

    for (i = 0; i < N; i++)
        count[I[i]] += 1
    for (i = 0; i < V; i++)
        count[i] += count[i - 1]
    for (i = 0; i < N; i++)
        K[--count[I[i]]] = i

该算法的时间空间复杂度均为 `O(V)`。V 表示所有可能的不同的输入的个数。如果你的输入为不限大小的 int，则 V = 2<sup>32</sup>, 如果你的输入为长度 <= 10 的 ascii string，则 V = 26<sup>10</sup>，类似的输入随处可见，因此，这个算法虽然简单，但实用性不高。下面给出改进的 counting sort。

#### 改进的 Counting Sort

假设 I[i] 是可以拆分的序列，所谓可拆分，比如 125 可以被拆成 1, 2, 5，"abc" 可以被拆成 "a", "b", "c"。并且序列中的每个元素有权重大小之分，如 125 = 1\*100 + 2\*10 + 5\*1，所以 1 的权重最高，2 次之，5 最低；对于字符串，权重从左到右依次递减。权重越高在排序中所起的作用也就越大，如 125, 211，虽然 25 > 11，但因为 1 < 2，所以 125 还是小于 211。

为了规避不必要的细节，对 I 做这么一个限制：I 中所有序列都是等长的 (长度不同可以补成相同，比如 125 和 2543，在 125 前面加个 0 就变成和 2543 等长了)。

改进的 counting sort 是一个迭代的过程，每次迭代在每个序列的某个局部做 count (局部指的是序列中连续的几个元素)，然后结合之前迭代得到的局部排序结果，推导出一个更大的局部的序，不断迭代直到得到全局的序，因为只在序列的局部做 count，所以时间和空间的使用都大大减少。这段话很抽象，看个例子吧。

令 I = (896706, 160243, 393894, 803201, 292963, 306785)，每次迭代的时候在 2 个元素上 count，改进的 counting sort 迭代如下：

1. 在最后 2 个元素做 counting sort，并将局部排序结果存于 K 中。

    <object data="/resource/SA/first_iter.svg" type="image/svg+xml"></object>

2. 在第 2, 3 个元素上做 counting sort，并 update K 数组。这步迭代完事后，K 中就包含了后 4 个元素的序 (相比于第 1 步迭代的一个更大的局部)。

    <object data="/resource/SA/second_iter.svg" type="image/svg+xml"></object>

    注意这个步骤的 counting sort 不同于上面的伪代码，区别在最后一个 for 循环，不能再简单得从第 0 个序列循环到第 N - 1 个，而是需要借助第一步中得到 K，代码如下 (其中`K2`是一个临时数组，用于暂时存放当前排序结果)：

        for (r = 0; r < N; r++)
            K2[--count[I[K[r]]]] = K[r]
        K = K2

    这里的 I[i] 不是完整的 I[i]，而是局部，如：I[0] = 67。

    如果按照标准的做法，你会发现 896706 和 306785 的序是反着的， **所以前一轮得到的 K 数组的作用就是在当前迭代中将相同的局部元素区分开**。

3. 重复与第 2 步相同的迭代，得到对应 6 个元素的 K，也就是最终的序 K = (1, 4, 5, 2, 3, 0)。

这个例子中，count 数组的大小只要 100 即可，每轮迭代耗时 O(N + 100) = O(N)，如果序列长度为 L，则总时间为 O(LN)。你也可以每轮迭代在 1 个元素上做 counting sort，也可以 3 个，都可以。

上述例子从权重低的局部开始迭代到权重高的局部，对于一般的 counting sort 并没有这个限制，下面的 suffix array 的构建就不是这么迭代的。但有一点是相同的，那就是**为了得到一个更大的局部的序，需要权重高的那个局部的 count 信息和权重低的那个局部的 K 数组**，这对于所有的 counting sort 都一样。

### 4. Suffix Array Construction

根据上一节给出的 counting sort 的原理，counting sort 是一个迭代的过程，在每一轮迭代得到权重高的局部的 count 信息和权重低的局部的排序信息，然后推导出一个更大的局部的排序结果。具体实现上共有 3 个部分需要明确：

1. 如何迭代
2. 如何 count
3. 如何推到出更大的局部的排序结果

结合前面提到的 suffix 集合 S 的性质，S<sub>l:2l</sub> 中的非空元素全部都出现在 S<sub>l</sub> 中，那如果我得到了 S<sub>l</sub> 的序，即 SA<sub>l</sub>，那我就可以想办法从 SA<sub>l</sub> 推导出 SA<sub>l:2l</sub>，结合 count<sub>l</sub> (count<sub>l</sub> 的定义与 SA<sub>l</sub> 类似) 就可以推出 SA<sub>2l</sub>，所以 suffix array 构建的迭代过程就是这样：

<blockquote class="code">
初始化 SA<sub>1</sub>, count<sub>1</sub><br/>
for (l = 1; l < len(str); l = 2 * l):<br/>
&nbsp;&nbsp;SA<sub>l</sub> &rarr; SA<sub>l:2l</sub><br/>
&nbsp;&nbsp;SA<sub>l:2l</sub> 结合 count<sub>l</sub> &rarr; SA<sub>2l</sub><br/>
&nbsp;&nbsp;得到 count<sub>2l</sub><br/>
</blockquote>

注意到这里的 count 不同于上一节例子中 count 每次都在一个固定大小的局部上做，这里每次 count 的局部大小都翻一翻。假设 str 只包含 ascii 字符且长度为 100，那是不是 count 的大小就要是 26<sup>100</sup> 呢？其实不用，可以借助 rank 数组 R，在变量定义小节中提到，相同的元素对应相同的 rank，不同的元素对应不同的 rank，因此 rank 可以当成每个元素的唯一 ID，count 就在 R 上做。这样迭代就变成：

<blockquote class="code">
初始化 SA<sub>1</sub>, count<sub>1</sub>, R<sub>1</sub><br/>
for (l = 1; l < len(str); l = 2 * l):<br/>
&nbsp;&nbsp;SA<sub>l</sub> &rarr; SA<sub>l:2l</sub><br/>
&nbsp;&nbsp;SA<sub>l:2l</sub> 结合 count<sub>l</sub> &rarr; SA<sub>2l</sub><br/>
&nbsp;&nbsp;R<sub>l</sub> &rarr; R<sub>l:2l</sub><br/>
&nbsp;&nbsp;R<sub>l</sub> 结合 R<sub>l:2l</sub> &rarr; R<sub>2l</sub><br/>
&nbsp;&nbsp;在 R<sub>2l</sub> 的基础上得到 count<sub>2l</sub><br/>
</blockquote>

对应的 C 代码如下所示，这里空间的使用并不是最优的，有些数组可以合并使用，但这样会使逻辑不清晰，不利于这里说明。

里面的变量和上面定义的变量的对应关系是这样：

* rank 对应 R<sub>l</sub>，rank2 对应 R<sub>l:2l</sub>，rank\_ 是一个临时数组
* SA 对应 SA<sub>l</sub>，SA2 对应 SA<sub>l:2l</sub>
* count 对应 count<sub>l</sub>

代码：

{% highlight c %}
/*
 * initialize SA_1, R_1, count_1
 */
for (i = 0; i < len; ++i) {
    rank[i] = str[i];
    count[rank[i]] += 1;
}
for (r = 1; r < sa->vcb_size; ++r) {
    count[r] += count[r - 1];
}
for (i = 0; i < len; ++i) {
    SA[--count[rank[i]]] = i;
}
/* reset count */
memset(count, 0, sizeof(int) * sa->size);
for (i = 0; i < len; ++i) {
    count[rank[i]] += 1;
}
for (r = 1; r < sa->vcb_size; ++r) {
    count[r] += count[r - 1];
}

/*
 * prefix doubling loop
 */
for (l = 1; l < len; l <<= 1) {
    int r_ = 0;

    /*
     * SA_l ==> SA_l:2l
     */
    for (r = 0, i = len - 1; i >= len - l; --i) {
        SA2[r++] = i;
    }
    for (r_ = 0; r_ < len; ++r_) {
        if (SA[r_] >= l) {
            SA2[r++] = SA[r_] - l;
        }
    }

    /*
     * count_l + SA_l:2l ==> SA_2l
     */
    for (r = len - 1; r >= 0; --r) {
        SA[--count[rank[SA2[r]]]] = SA2[r];
    }

    /*
     * rank_l ==> rank_l:2l
     */
    for (r_ = 0; r_ < l; ++r_) {
        rank2[SA2[r_]] = 0;
    }
    r = 1;
    rank2[SA2[l]] = r;
    for (r_ = l + 1; r_ < len; ++r_) {
        int i_cur = SA2[r_];
        int i_pre = SA2[r_ - 1];
        if (rank[i_cur + l] != rank[i_pre + l]) {
            r += 1;
        }
        rank2[i_cur] = r;
    }

    /*
     * rank_l + rank_l:2l ==> rank_2l
     */
    r = 0;
    rank_[SA[0]] = 0;
    for (r_ = 1; r_ < len; ++r_) {
        int i_cur = SA[r_];
        int i_pre = SA[r_ - 1];
        if (rank[i_cur] != rank[i_pre] || rank2[i_cur] != rank2[i_pre]) {
            r += 1;
        }
        rank_[i_cur] = r;
    }
    swap_pointer(&rank, &rank_);

    /*
     * get count_2l
     */
    memset(count, 0, len * sizeof(int));
    for (i = 0; i < len; ++i) {
        count[rank[i]] += 1;
    }
    for (r = 1; r < len; ++r) {
        count[r] += count[r - 1];
    }
}
{% endhighlight %}

完整的可执行代码参考 [uva 10526 的解题代码](https://github.com/juscodit/uva/blob/master/10526_intellectual_property_SA.c)。
