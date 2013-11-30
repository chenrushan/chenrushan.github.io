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


