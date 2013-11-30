---
layout: post
title: Suffix Array
categories: ds
---

### 变量定义

* `str`

  表示一个字符串

  以下所有例子均针对 str = "mississippi"

* `T`

  表示 str 的长度

  T = 11

* `str[i:j]`

  表示从 str[i] 到 str[j-1] 的子串

  str[2:5] = "ssi"

* `S`

  `S = (str[0:n], str[1:n], ..., str[n-1:n])` 表示 str 的 suffix 序列

  S = (mississippi, ississippi, ssissippi, sissippi, issippi, ssippi, sippi, ippi, ppi, pi, i)

* <span class="code">S<sub>i:j</sub></span>

  <span class="code">S<sub>i:j</sub> = (S[0][i:j], S[1][i:j], ..., S[n-1][i:j])</span> 表示所有 suffix 的 [i:j] 子串序列

  s[i:j] = s[i:len(s)] if j > len(s)

  s[i:j] = \<NULL\> (空串) if i >= len(s)

  S<sub>1:3</sub> = (is, ss, si, is, ss, si, ip, pp, pi, i, \<NULL\>)

* <span class="code">S<sub>l</sub></span>

  S<sub>l</sub> = S<sub>0:l</sub>

* `SA`

  表示 suffix array，SA[i] 存储 str 的索引值，指向第 i 小后缀

  SA[2] = 4 (表示第 2 小的后缀是 issippi)

### Prefix-doubling Algorithm

#### 基本思想

构建一个 SA 最简单的方法就是调用 qsort 对所有的后缀进行排序，qsort 的 compare 比较两两后缀的大小。这种方法的时间复杂度就是 O(T<sup>2</sup>logT)，因为 qsort 中每次 compare 的代价为 O(T)。这种方法虽然简单，但效率不高，因为它没有在排序的过程中利用 SA 的一些特有的性质。

首先很容易意识到

> 任一后缀的后缀依然是 str 的一个后缀

举个例子，考虑后缀 "ssippi"，"ippi" 是这一后缀的后缀，同时也是原始字符串的后缀。

根据这一性质，我们可以得到如下推论

> 任一后缀的任一子串必然是某一后缀的前缀

看着有点绕，一看例子就明白了，"sip" 是 "ssippi" 的一个子串，也是 "sippi" 这个后缀的前缀。

根据上面的推论，假设我们有了 S<sub>l</sub> 的序，那就等价于有了 S<sub>i:i+l</sub> 的序，当 i = l 时，S<sub>i:i+l</sub> = S<sub>l:2l</sub>，这样我们就同时有了 S<sub>l</sub> 和 S<sub>l:2l</sub> 的序，由此很容易可以推出 S<sub>2l</sub> 的序。具体的实现细节见下一小节。

既然从 S<sub>l</sub> 的序推出 S<sub>2l</sub> 的序很简单，我们就可以设计这么一个算法，一开始 SA 包含 S<sub>1</sub> 的序，然后推出 S<sub>2</sub> 的序，然后推出 S<sub>4</sub> 的序，直到 S<sub>T</sub> 的序，S<sub>T</sub> 就等于 S，这就完成了对所有后缀的排序。这就是所谓的 prefix-doubling algorithm。这里共进行了 logT 次排序，如果每次排序用 qsort，由于每个 compare 的时间为 O(1)，所以每次 qsort 的时间为 O(TlogT)，则总时间为 O(Tlog<sup>2</sup>T)。

#### 部分实现细节

对于这个算法，如何快速的从 S<sub>l</sub> 的序推出 S<sub>2l</sub> 的序是核心。为了方便，我们添加一个额外的数组 rank，rank[i] 表示 S<sub>l</sub>[i] 在 S<sub>l</sub> 序列中的 rank，如果 S<sub>l</sub>[i] == S<sub>l</sub>[j]，那 rank[i] = rank[j]，如果 S<sub>l</sub> 中所有元素都不相同，则 SA[rank[i]] = i。S<sub>l:2l</sub> 和 S<sub>l</sub> 的 rank 是直接对应的，S<sub>l:2l</sub> 的 rank[i] = S<sub>l</sub> 的 rank[i + l]。(这不是说 rank 数组有多个，实现中 rank 数组只有一个)

假设我们得到了 S<sub>l</sub> 对应的 rank，那我们就可以用如下代码来进行 S<sub>2l</sub> 中两两元素的比较。

    /* i, j are the indices of S sequence */
    int cmp(int i, int j)
    {
        /* compare [0:l] part */
        if (rank[i] != rank[j]) {
            return rank[i] < rank[j];
        }
        /* compare [l:2l] part */
        int ri = i + l < T ? rank[i + l] : -1;
        int rj = j + l < T ? rank[j + l] : -1;
        return ri < rj;
    }
