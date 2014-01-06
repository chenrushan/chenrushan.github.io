---
layout: post
title: PLSA 和 Matrix Factorization 的关系
categories: ml
tags: plsa, matrix factorization, kl divergence
---

PLSA 的优化目标是如下 likelihood function：

<object data="/resource/plsa/plsa_likelihood.svg" type="image/svg+xml" class="blkcenter"></object>

其中 n(w, d) 表示 w 和 d 共现的频次，P(w, d|&theta;) 表示 w 和 d 的联合概率，&theta; 即为我们要训练得到的参数，根据 P(w, d|&theta;) 的不同分解方法，&theta; 会不一样。

P(w, d|&theta;) 有两种分解方法：

<object data="/resource/plsa/p_wd_1.svg" type="image/svg+xml" class="blkcenter"></object>

或者

<object data="/resource/plsa/p_wd_2.svg" type="image/svg+xml" class="blkcenter"></object>

其中：

* 第一种方法对应 d &rarr; z &rarr; w 的生成过程，比较易于理解，&theta; 包含 3 类参数：P(d), P(z|d), P(w|z)。

* 第二种方法对应的 &theta; 包含 P(z), P(d|z), P(w|z)，这种分解不那么容易从直观上理解，但它更实用，因为有了 P(z), P(d|z), P(w|z)，我们可以推导出 P(z|d), P(z|w) 等任何你需要的信息 (通过 bayesian equation 做变换即可)，这是第一种分解方法所不能实现的。更有意思的是，这种分解方法对应了一个 matrix factorization 的过程。

PLSA 实现如下矩阵分解：

<object data="/resource/plsa/plsa_mf.svg" type="image/svg+xml" class="blkcenter"></object>

其中：

* D 为原始矩阵，矩阵中的每个元素为 P(w, d)，这个 P(w, d) 是由训练数据算得的经验分布
* L 中每个元素表示 P(d|z)
* U 为对角阵，对角线上每个元素表示 P(z)
* R 中每个元素表示 P(w|z)

上面提到 PLSA 优化一个 likelihood function，进一步深入研究这个 likelihood，其实它等价于一个 KL divergence。


