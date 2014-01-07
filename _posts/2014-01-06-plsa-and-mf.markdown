---
layout: post
title: PLSA 和 Matrix Factorization 的关系
categories: ml
tags: plsa, matrix factorization, kl divergence
---

PLSA 的优化目标是如下 likelihood function：

$$\sum\_{d}\sum\_{w}n(w, d)log P(w, d|\theta)$$

其中 $n(w, d)$ 表示 $w$ 和 $d$ 共现的频次，$P(w, d|\theta)$ 表示 $w$ 和 $d$ 的联合概率，$\theta$ 即为我们要训练得到的参数，根据 $P(w, d|\theta)$ 的不同分解方法，$\theta$ 会不一样。

$P(w, d|\theta)$ 有两种分解方法：

$$P(w, d|\theta)=\sum\_{z}P(d)P(z|d)P(w|z)$$

或者

$$P(w, d|\theta)=\sum\_{z}P(z)P(d|z)P(w|z)$$

其中：

* 第一种方法对应 $d \rightarrow z \rightarrow w$ 的生成过程，比较易于理解，$\theta$ 包含 3 类参数：$P(d), P(z|d), P(w|z)$。

* 第二种方法对应的 $\theta$ 包含 $P(z), P(d|z), P(w|z)$，这种分解不那么容易从直观上理解，但它更实用，因为有了 $P(z), P(d|z), P(w|z)$，我们可以推导出 $P(z|d), P(z|w)$ 等任何你需要的信息 (通过 bayesian equation 做变换即可)，这是第一种分解方法所不能实现的。更有意思的是，这种分解方法对应了一个 matrix factorization 的过程。

PLSA 实现如下矩阵分解：

<object data="/resource/plsa/plsa_mf.svg" type="image/svg+xml" class="blkcenter"></object>

其中：

* $D$ 为原始矩阵，矩阵中的每个元素为 $P(w, d)$，这个 $P(w, d)$ 是由训练数据算得的经验分布
* $L$ 中每个元素表示 $P(d|z)$
* $U$ 为对角阵，对角线上每个元素表示 $P(z)$
* $R$ 中每个元素表示 $P(w|z)$

假设输入包含 $n$ 个 doc，$m$ 个 word，同时指定 topic 个数为 $r$，则上述 4 个矩阵的维度分别为：$D\_{n\times m}, L\_{m\times r}, U\_{r\times r}, R\_{r\times n}$。

上面提到 PLSA 优化一个 likelihood function，进一步深入研究这个 likelihood，其实它等价于 KL divergence。

$$\sum\_{d}\sum\_{w}n(w, d)log P(w, d|\theta)$$
$$= -\sum\_{d}\sum\_{w}n(w, d)log \frac{1}{P(w, d|\theta)}$$
$$\sim -\sum\_{d}\sum\_{w}P(w, d)log \frac{1}{P(w, d|\theta)}$$
$$\sim -\sum\_{d}\sum\_{w}P(w, d)log \frac{P(w, d)}{P(w, d|\theta)}$$

其中最后一个式子去掉负号就表示 $P(w, d)$ 的经验分布和我们训练得到的分布的 KL divergence，所以针对 PLSA，最大化 likelihood 就等价于去最小化与经验分布间的 KL divergence，所以 PLSA 实际上就是要去拟合经验分布。

根据第二种分解得到的 EM 迭代是这样的：

* E-step:

    $$P(z|w,d)=\frac{P(z)P(d|z)P(w|z)}{\sum\_{z}P(z)P(d|z)P(w|z)}$$

* M-step:

    $$P(z)=\frac{\sum\_{d}\sum\_{w}n(w,d)P(z|w,d)}{\sum\_{d}\sum\_{w}n(d,w)}$$
    $$P(w|z)=\frac{\sum\_{d}n(w,d)P(z|w,d)}{\sum\_{w}\sum\_{d}n(w,d)P(z|w,d)}$$
    $$P(d|z)=\frac{\sum\_{w}n(w,d)P(z|w,d)}{\sum\_{d}\sum\_{w}n(w,d)P(z|w,d)}$$