---
layout: post
title: Convexity of Logistic Regression Loss Function
categories: ml
tags: lr, logistic regression, convexity
---

这篇文章主要是给出 logistic regression (以下简称 LR) 的 loss function 的 convexity 证明，由于 sigmoid function 是 LR loss 的组成部分，但是 sigmoid 本身是 non-convex 的，所以如果没注意的话，可能会误以为 LR 的 loss 也是 non-convex 的，其实不然，下面给出证明，证明的方法是验证 LR loss 对应的 Hessian matrix 是个 positive semi-definite matrix

#### LR Loss Function

定义 sigmoid function $h\_w(x) = \frac{1}{1 + \exp(-w^T x)}$，假设训练数据共有 $m$ 个样本，则其 likelihood 可以表示为

$$ \prod\_{i=1}^m h\_w(x\_i)^{y\_i} (1 - h\_w(x\_i))^{1 - y\_i} $$

其中 $x\_i \in \mathbb{R}^n$ 为样本，$y\_i$ 为每个样本的 label，$y\_i \in \\{0, 1\\}$，这里用 $\\{0, 1\\}$ 作为 $y\_i$ 的集合，有很多文献用的是 $\\{-1, 1\\}$，用 $\\{-1, 1\\}$ 的好处是你可以把 likelihood 表示得更好看些，但是具体系统实现上，还是用 $\\{0, 1\\}$ 要方便，因此这里就用 $\\{0, 1\\}$ 来作为每个样本的 label 集合

LR 的目标是 maximum likelihood，按照通常的做法，我们对 likelihood 做个 $-\log$ 变换，把问题变为 $\arg\min$ 问题，做了变换之后，我们定义如下 LR 的 loss function

$$ L(w) = -\sum\_{i=1}^m (y\_i \log h\_w(x\_i) + (1 - y\_i) \log (1 - h\_w(x\_i))) $$

#### Convexity Proof


