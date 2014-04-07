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

根据 Weiestrass' therom，如果 $X$ 是个 compact set，同时 $f(x)$ 是个 continuous function，那 global minimum 一定存在。

但是很多时候 global minimum 很难得到，比如下面这个函数

<object data="/resource/NNP/03-1d-uncon-op/function.svg" type="image/svg+xml" class="blkcenter"></object>

从图里我们很容易看出 global minimum 是 $x\_2$，但是我们很难设计出一种算法直接得到这么一个解，因此在大多数情况下，我们是去求解 local minimum，而不是 global minimum。

#### Local Minimum

<blockquote>
给定 $x^*\in X$ 如果存在 $\delta \in \mathbb{R}$，使得 $f(x^*) \leq f(x) \; \forall x \in X \cap B(x^*, \delta)$，则 $x^*$ 被称为 local minimum
</blockquote>

根据这个定义，上图中的 $x\_1$ 到 $x\_5$ 都是 local minimum，其中 $x\_4$ 有点特别，其周围存在一个水平线段，在这个区域内都有 $f(x) = f(x\_4)$。

也许有人认为，如果我们有办法遍历所有的 local minimum，我们就可以得到 global minimum，其实不然，以下面这个函数为例

<object data="/resource/NNP/03-1d-uncon-op/fun3.svg" type="image/svg+xml" class="blkcenter"></object>

这个函数有一个 local minimum，但这个 local minimum 并不是 global minimum，因为 global minimum 并不存在。

明确了问题，接下来就要看看我们怎么去得到 local minimum，为此，我们需要知道 local minimum 具有什么特点，如何从数学上更明确得定义出 local minimum。下面我们我们分别给出一个点是 local minimum 的 sufficient 和 necessary condition

* necessary condition: 就是所有 local minimum 都具备的条件

* sufficient condition: 就是只要点 $x$ 满足这个条件，$x$ 就一定是 local minimum

#### First order necessary condition

<blockquote>
令 $f\in \mathcal{C}^1$，如果 $x^*$ 是 local minimum，则 $f'(x^*) = 0$
</blockquote>

之所以叫 first order necessary condition，就是因为这个 condition 用到了 $f(x)$ 的 first order derivative。

证明如下 (反证法)

----------

假设存在 $x^\*$ 为 local minimum 且 $f'(x^\*) \neq 0$，暂且令 $f'(x^\*) > 0$，$< 0$ 的情况同理。

$f \in \mathcal{C}^1 \Rightarrow f' \in \mathcal{C}^0$，由于 $f'(x^\*) > 0$，所以存在 $\delta$ 使得 $f'(x) > 0 \;\; \forall x \in B(x^\*, \delta)$。根据 Truncated Taylor series，我们有

$$f(x) = f(x^\*) + f'(\bar{x})(x - x^\*) \;\; \bar{x} \in (x^\*, x)$$

由于 $\bar{x} \in B(x^\*, \delta)$，所以 $f'(\bar{x}) > 0$，取 $x \in (x^\* - \delta, x^\*)$，则有 $x - x^\* < 0$，这样就有 $f'(\bar{x})(x - x^\*) < 0$，也就是 $f(x) < f(x^\*) \; \forall x \in (x^\* - \delta, x^\*)$，这与 $x^\*$ 是 local minimum 相矛盾。

因此如果 $x^\*$ 是 local minimum，则有 $f'(x^\*) = 0$。

----------

但是 $f'(x^\*) = 0$ 并不是 sufficient condition，对于如下两个函数

<object data="/resource/NNP/03-1d-uncon-op/f'(x)=0.svg" type="image/svg+xml" class="blkcenter"></object>

都有 $f'(a) = 0$，但只有左边的函数在 $a$ 处是最小值。

注意到，对于左边函数，我们有 $f''(a) \geq 0$，而这其实就是 $x^\*$ 为 local minimum 的第二个 necessary condition。

#### Second order necessary condition

<blockquote>
令 $f \in \mathcal{C}^2$，如果 $x^*$ 是 local minimum，则 $f''(x^*) \geq 0$
</blockquote>

证明如下 (反证法)

----------

假设存在 $x^\*$ 是 local minimum 同时 $f''(x^\*) < 0$。

$f \in \mathcal{C}^2 \rightarrow f'' \in \mathcal{C}^0$，由于 $f''(x^\*) < 0$，所以存在 $\delta$ 使得 $f''(x) < 0 \; \forall x \in B(x^\*, \delta)$。根据 Truncated Taylor series，我们有

$$f(x) = f(x^\*) + f'(x^\*)(x - x^\*) + \frac{1}{2} f''(\bar{x})(x - x^\*)^2 \;\; \bar{x} \in (x^\*, x)$$

由于 $\bar{x} \in B(x^\*, \delta)$，所以 $f''(\bar{x}) < 0$，而 $(x - x^\*)^2 \geq 0$，所以有 $f''(\bar{x})(x - x^\*)^2 \leq 0$，另外根据前面的 first order necessary condition，$f'(x^\*) = 0$，这样就有 $f(x) < f(x^\*)$，这与 $x^\*$ 是 local minimum 相矛盾。

因此如果 $x^\*$ 是 local minimum，则有 $f''(x^\*) \geq 0$。

----------

但是 $f''(x^\*) \geq 0$ 同样不是 sufficient condition，比如下面这个函数 $f(x) = (x - a)^3 + b$。
