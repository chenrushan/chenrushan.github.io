---
layout: post
title: 03 - unconstrained optimization for 1 dimensional function
categories: nnumop
tags: NPTEL, numerical optimization
---

#### 1d unconstrained optimization

这门课程的重点是 multi-dimensional function 的 constrained optimization，但它用到的很多技术都来自于 unconstrained optimization，而无论是 1-dimensional 还是 multi-dimensional 它们优化的思想都是想通的，因此这篇文章就介绍 optimization 中最简单的 1-dimensional(1d) unconstrained optimization。这个问题可以表示为

$$ \min\_{x\in X} \; f(x) $$

其中 $X \subseteq R, f: X \rightarrow \mathbb{R}$，举个例子，如函数 $f(x) = (x - a)^2 + b$

<object data="/resource/NNP/03-1d-uncon-op/x^2.svg" type="image/svg+xml" class="blkcenter"></object>

显然能够最小化 $f(x)$ 的点是 $a$，这个点也被称作 global minimum。

#### Global Minimum

<blockquote>
给定 $x^*\in X$ 如果 $f(x^*) \leq f(x) \; \forall x \in X$，则 $x^*$ 被称为 global minimum
</blockquote>

但是很多时候 global minimum 很难得到，比如下面这个函数

<object data="/resource/NNP/03-1d-uncon-op/function.svg" type="image/svg+xml" class="blkcenter"></object>

从图里我们很容易看出 global minimum 是 $x\_2$，但是我们很难设计出一种算法直接得到这么一个解，因此在大多数情况下，我们是去求解 local minimum，而不是 global minimum。

#### Local Minimum

<blockquote>
给定 $x^*\in X$ 如果存在 $\delta \in \mathbb{R}$，使得 $f(x^*) \leq f(x) \; \forall x \in X \cap B(x^*, \delta)$，则 $x^*$ 被称为 local minimum
</blockquote>

根据这个定义，上图中的 $x\_1$ 到 $x\_5$ 都是 local minimum，其中 $x\_2$ 是 global minimum。

也许有人认为，如果我们有办法遍历所有的 local minimum，我们就可以得到 global minimum，其实不然，以下面这个函数为例

<object data="/resource/NNP/03-1d-uncon-op/fun3.svg" type="image/svg+xml" class="blkcenter"></object>

这个函数有一个 local minimum，但这个 local minimum 并不是 global minimum，因为 global minimum 并不存在。
