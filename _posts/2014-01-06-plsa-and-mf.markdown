---
layout: post
title: PLSA and Matrix Factorization
categories: ml
tags: plsa, matrix factorization, kl divergence
---

### PLSA 的两种分解法

PLSA 的优化目标是如下 likelihood function：

$$\sum\_{d}\sum\_{w}n(w, d)log P(w, d|\theta)$$

其中 $n(w, d)$ 表示 $w$ 和 $d$ 共现的频次，$P(w, d|\theta)$ 表示 $w$ 和 $d$ 的联合概率，$\theta$ 即为我们要训练得到的参数，根据 $P(w, d|\theta)$ 的不同分解方法，$\theta$ 会不一样。

$P(w, d|\theta)$ 有两种分解方法：

$$P(w, d|\theta)=\sum\_{z}P(d)P(z|d)P(w|z)$$

或者

$$P(w, d|\theta)=\sum\_{z}P(z)P(d|z)P(w|z)$$

其中：

* 第一种方法对应 $d \rightarrow z \rightarrow w$ 的生成过程，比较易于理解，$\theta$ 包含 3 类参数：$P(d), P(z|d), P(w|z)$。

* 第二种方法对应的 $\theta$ 包含 $P(z), P(d|z), P(w|z)$，这种分解不那么容易从直观上理解，但有意思的是，这种分解方法与 matrix factorization 相对应。

### PLSA 与 Matrix Factorization

按照上面第二种分解法

* 将 $P(d|z)$ 放入一个矩阵 $L$, $L$ 的行对应 $d$，列对应 $z$
* 将 $P(z)$ 放入一个对角阵 $U$
* 将 $P(w|z)$ 放入另一个矩阵 $R$，$R$ 的行对应 $z$，列对应 $w$

另外将 $P(w, d|\theta)$ 放入另一个矩阵 $\overline{D}$，其行对应 $d$，列对应 $w$，则有：

$$\overline{D} = L\times U\times R$$

任意一个 $P(w, d|\theta)$ 可以认为是 $L$ 中的行与 $R$ 中的列的加权的内积，权重为 $U$ 中对应的 $p(z)$，如下图所示。

<object data="/resource/plsa/plsa_mf.svg" type="image/svg+xml" class="blkcenter"></object>

如果输入包含 $n$ 个 doc，$m$ 个 word，同时指定 topic 个数为 $r$，则上述 4 个矩阵的维度分别为：$\overline{D}\_{n\times m}, L\_{m\times r}, U\_{r\times r}, R\_{r\times n}$。

上面提到 PLSA 优化一个 likelihood function，进一步深入研究这个 likelihood，其实它等价于 KL divergence。

$$\sum\_{d}\sum\_{w}n(w, d)log P(w, d|\theta)$$
$$= -\sum\_{d}\sum\_{w}n(w, d)log \frac{1}{P(w, d|\theta)}$$
$$\sim -\sum\_{d}\sum\_{w}P(w, d)log \frac{1}{P(w, d|\theta)}$$
$$\sim -\sum\_{d}\sum\_{w}P(w, d)log \frac{P(w, d)}{P(w, d|\theta)}$$

其中最后一个式子去掉负号就表示经验分布 $P(w, d)$ 和我们训练得到的分布 $P(w, d|\theta)$ 的 KL divergence，所以针对 PLSA，最大化 likelihood 就等价于最小化与经验分布间的 KL divergence，所以 PLSA 实际上是要去拟合经验分布。

如果从矩阵分解的角度看，**PLSA 就是一个以最小化两个矩阵间 KL divergence 为目标的矩阵分解**，以 $D$ 表示存放 $P(w, d)$ 的矩阵，即 $min\\; KL(D\parallel \overline{D})$。其与 SVD 这样的矩阵分解算法区别就在于 loss function 的不同，SVD 对应的 loss function 是 $min\\; \left\Vert D-\overline{D} \right\Vert\_{F}^{2}$，即两个矩阵差值的 frobenius norm。

<!--
根据第二种分解得到的 EM 迭代是这样的：

* E-step:

    $$P(z|w,d)=\frac{P(z)P(d|z)P(w|z)}{\sum\_{z}P(z)P(d|z)P(w|z)}$$

* M-step:

    $$P(z)=\frac{\sum\_{d}\sum\_{w}n(w,d)P(z|w,d)}{\sum\_{d}\sum\_{w}n(d,w)}$$
    $$P(w|z)=\frac{\sum\_{d}n(w,d)P(z|w,d)}{\sum\_{w}\sum\_{d}n(w,d)P(z|w,d)}$$
    $$P(d|z)=\frac{\sum\_{w}n(w,d)P(z|w,d)}{\sum\_{d}\sum\_{w}n(w,d)P(z|w,d)}$$
-->

