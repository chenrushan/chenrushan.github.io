---
layout: post
title: 03 - unconstrained optimization for 1 dimensional function
categories: nnumop
tags: NPTEL, numerical optimization
---

#### 1d unconstrained optimization

这门课程的重点是 multi-dimensional function 的 constrained optimization，但它用到的很多技术都来自于 unconstrained optimization，而无论是 1-dimensional 还是 multi-dimensional 它们优化的思想都是相通的，因此这篇文章就首先介绍 optimization 中最简单的 1-dimensional(1d) unconstrained optimization。这个问题可以表示为

$$ \min\_{x\in X} \; f(x) $$

其中 $X \subseteq R, f: X \rightarrow \mathbb{R}$，举个例子，如函数 $f(x) = (x - a)^2 + b$

<object data="/resource/NNP/03-1d-uncon-op/x^2.svg" type="image/svg+xml" class="blkcenter"></object>

这里能够最小化 $f(x)$ 的点是 $a$，这个点也被称作 global minimum。

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

这个函数只有一个 local minimum，但这个 local minimum 并不是 global minimum，因为 global minimum 并不存在。

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

如果 $x \in B(x^\*, \delta)$，则 $\bar{x} \in B(x^\*, \delta)$，则 $f'(\bar{x}) > 0$。取 $x \in (x^\* - \delta, x^\*)$，在这段区间内 $x - x^\* < 0$，这样就有 $f'(\bar{x})(x - x^\*) < 0$，也就是 $f(x) < f(x^\*) \; \forall x \in (x^\* - \delta, x^\*)$，这与 $x^\*$ 是 local minimum 相矛盾。

因此如果 $x^\*$ 是 local minimum，则有 $f'(x^\*) = 0$。

----------

但是 $f'(x^\*) = 0$ 并不是 sufficient condition，对于如下两个函数

<object data="/resource/NNP/03-1d-uncon-op/f'(x)=0.svg" type="image/svg+xml" class="blkcenter"></object>

都有 $f'(a) = 0$，但只有左边的函数在 $a$ 处是最小值。也因此满足 $f'(x) = 0$ 的 $x$ 并不被称为 minimum point，而是被称作 stationary point 或者 saddle point。

注意到，对于左边函数，我们有 $f''(a) \geq 0$，而这其实是 $x^\*$ 为 local minimum 的第二个 necessary condition。

#### Second order necessary condition

<blockquote>
令 $f \in \mathcal{C}^2$，如果 $x^*$ 是 local minimum，则 $f''(x^*) \geq 0$
</blockquote>

证明如下 (反证法)

----------

假设存在 $x^\*$ 是 local minimum 同时 $f''(x^\*) < 0$。

$f \in \mathcal{C}^2 \rightarrow f'' \in \mathcal{C}^0$，由于 $f''(x^\*) < 0$，所以存在 $\delta$ 使得 $f''(x) < 0 \; \forall x \in B(x^\*, \delta)$。根据 Truncated Taylor series，我们有

$$f(x) = f(x^\*) + f'(x^\*)(x - x^\*) + \frac{1}{2} f''(\bar{x})(x - x^\*)^2 \;\; \bar{x} \in (x^\*, x)$$

如果 $x \in B(x^\*, \delta)$，则 $\bar{x} \in B(x^\*, \delta)$，则 $f''(\bar{x}) < 0$，而 $(x - x^\*)^2 \geq 0$，所以有 $f''(\bar{x})(x - x^\*)^2 \leq 0$，另外根据前面的 first order necessary condition，$f'(x^\*) = 0$，这样就有 $f(x) < f(x^\*)$，这与 $x^\*$ 是 local minimum 相矛盾。

因此如果 $x^\*$ 是 local minimum，则有 $f''(x^\*) \geq 0$。

----------

但是 $f''(x^\*) \geq 0$ 同样不是 sufficient condition，比如函数 $f(x) = (x - a)^3 + b$。

<object data="/resource/NNP/03-1d-uncon-op/x^3.svg" type="image/svg+xml" class="blkcenter"></object>

$f(x)$ 在 $a$ 点的 $f'(a) = 0, f''(a) = 0$ 但是 $a$ 并不是 local minimum。

#### Necessary and sufficient condition

<blockquote>
令 $f(x) \in \mathcal{C}^{\infty}$，$f^{(k)}(x)$ 表示 $f(x)$ 的 k 阶导，一个点 $x^*$ 是 local minimum 当且仅当 sequence $\{ f^{(k)}(x) \}$  $(k = 1, 2, 3, \cdots)$ 中第一个非 0 $f^{(k)}(x)$ 对应的 k 是偶数且 $f^{(k)}(x) > 0$
</blockquote>

举个例子，上面的 $f(x) = (x - a)^3 + b$，$f^{(1)}(a) = 0, f^{(2)}(a) = 0, f^{(3)}(a) = 6$，这里第一个非 0 $f^{(k)}(x)$ 虽然大于 0，但出现在奇数 $k$ 位置，因此 $a$ 不是该函数的最小值。

#### 求解 Local minimum

根据上面的一堆 condition 我们可以得到如下求解 local minimum 的算法

1. 先根据 $f'(x) = 0$ 得出所有可能的 stationary point

2. 依次验证所有 stationary point 的各阶导数看是否符合 local minimum 的条件

----------

考虑 $min\_{x \in \mathbb{R}} (x^2 - 1)^3$

首先根据一阶导得到所有的 stationary point

$$ f'(x) = 6x(x^2 - 1)^2 = 0 \Rightarrow f'(0) = f'(1) = f'(-1) = 0$$

所以 stationary point 包括 $0, 1, -1$。然后分别验证这几个点的各阶导数

* 对于 $0$，$f''(0) = 6 > 0$

* 对于 $1$，$f''(1) = 0, f'''(1) = 48 > 0$

* 对于 $-1$，$f''(-1) = 0, f'''(-1) = -48 < 0$

由此可知，$0$ 是 local minimum，而 $1$ 和 $-1$ 都不是。

----------

上面的问题中，我们通过直接求解的方式得出了所有的 stationary point，但现实中很多函数无法或者很难进行这样的计算，比如 $f(x) = x^2 + e^x$，对于这个函数我们就很难直接求解 stationary point，这时我们就需要考虑使用数值方法。
