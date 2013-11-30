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

  S = {string[k:n] | k &isin; [0, n)} 表示 string 的所有 suffix 集合

  S = {mississippi, ississippi, ssissippi, sissippi, issippi, ssippi, sippi, ippi, ppi, pi, i}

* <span class="code">S<sub>i:j</sub></span>

  S<sub>i:j</sub> = {s[i:j] | s &isin; S} 表示所有 suffix 的 [i:j] 子串集合

  s[i:j] = s[i:len(s)] if j > len(s)

  s[i:j] = \<NULL\> (空串) if i >= len(s)

  S<sub>1:3</sub> = {is, ss, si, is, ss, si, ip, pp, pi, i, \<NULL\>}

* <span class="code">S<sub>l</sub></span>

  S<sub>l</sub> = S<sub>0:l</sub>

* `SA`

  表示 suffix array，SA[i] 存储 str 的索引值，指向第 i 小后缀

  SA[2] = 4 (表示第 2 小的后缀是 issippi)

### Prefix-doubling Algorithm

#### 基本思想

构建一个 SA 最简单的方法就是调用 qsort 对所有的后缀进行排序，qsort 的 compare 调用比较两两后缀文本的大小。这种方法的时间复杂度就是 O(T<sup>2</sup>logT)，因为 qsort 中每次 compare 的代价为 O(T)。这种方法虽然简单，但效率不高，因为它没有在排序的过程中利用 SA 的一些特有的性质。

首先很容易意识到

> 任一后缀的后缀依然是 str 的一个后缀

举个例子，考虑后缀 "ssippi"，"ippi" 是这一后缀的后缀，同时也是原始字符串的后缀。

根据这一性质，我们可以得到如下推论。

> 任一后缀的任一子串必然是某一后缀的前缀

看着有点绕，一看例子就明白了，"sip" 是 "ssippi" 的一个子串，同时也是 "sippi" 这个后缀的前缀。

根据上面的推论，假设我们有了 S<sub>l</sub> 这个集合的序，那就等价于有了 S<sub>i:i+l</sub> 这个集合的序，当 i = l 时，S<sub>i:i+l</sub> = S<sub>l:2l</sub>，同时有了 S<sub>l</sub> 和 S<sub>l:2l</sub> 的序，我们就可以很容易推出 S<sub>2l</sub> 集合的序。具体的实现细节参考下一小节。

既然从 S<sub>l</sub> 的序推出 S<sub>2l</sub> 的序很简单，我们就可以设计这么一个算法，一开始的时候 SA 包含 S<sub>1</sub> 的序，然后推出 S<sub>2</sub> 的序，然后推出 S<sub>4</sub> 的序，直到 S<sub>T</sub> 的序，S<sub>T</sub> 就等于 S，这就完成了对所有后缀的排序。这就是所谓的 prefix-doubling algorithm。这里共进行了 logT 次排序，如果每次排序用 qsort，由于每个 compare 的时间为 O(1)，所以每次 qsort 的时间为 O(TlogT)，则总时间为 O(Tlog<sup>2</sup>T)。

#### 部分实现细节

为了能把 S<sub>i:i+l</sub> 的序和 S<sub>l</sub> 的序快速对应上，我们需要在 SA 的基础上添加一个额外的数组 rank，rank[i] 表示以 str[i] 开头的后缀在所有后缀中的序，相等的 key 对应相等的 rank，如果所有的 key 都是不同的，则 SA[rank[i]] = i。

假设我们已知 S<sub>l</sub> 的序，同时 rank 也相应设置好了，那我们就用如下代码来进行 S<sub>2l</sub> 中两两元素的比较。

    /* compare prefixes of length 2l based on the sorting
       result * of prefixes of length l */
    int cmp(const void *_s1, const void *_s2)
    {
        int s1 = *(int *)_s1, s2 = *(int *)_s2;
    
        /* compare first part */
        if (rank[s1] != rank[s2]) {
            return rank[s1] < rank[s2];
        }
        /* check if there's no [l, 2l) substring of these 2 suffixes */
        if (s1 + l >= T) {
            return 0;
        }
        /* compare second part */
        return rank[s1 + l] < rank[s2 + l];
    }
