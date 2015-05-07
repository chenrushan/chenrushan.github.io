---
layout: post
title: 06 - Multi-Dimensional Unconstrained Optimization
categories: nnumop
tags: NPTEL, numerical optimization
---

### Descent Direction

Descent direction 在 multi-dimensional optimization 中是一个非常重要的概念，很多优化算法的核心就是如何构造 descent direction

<blockquote>
令 $\bar{\b{x}} \in \mathbb{R}^n$，如果存在一个方向 $\b{d} \in \mathbb{R}^n, \delta > 0$ 使得 $f(\bar{\b{x}} + \alpha \b{d}) < f(\bar{\b{x}}) \; \forall \alpha \in (0, \delta)$，则 $\b{d}$ 就被称为 descent direction
</blockquote>

所以 $\b{d}$ 和 $\b{x}$ 处于一个空间内

<blockquote>
令 $f \in \mathcal{C}^1, \bar{\b{x}} \in \mathbb{R}^n$，$g(\bar{\b{x}})$ 为 $f$ 在 $\bar{\b{x}}$ 处的 gradient，如果 $g^T(\bar{\b{x}})d < 0$，则 $d$ 为 $f$ 在 $\bar{\b{x}}$ 处的 descent direction
</blockquote>

* 证明

    因为 $f\in \mathcal{C}^1$，所以 $g \in \mathcal{C}^0$，又因为 $g^T(\bar{\b{x}})\b{d} < 0$，所以必存在 $\delta$，使得
    
    $$g^T(\b{x})\b{d} < 0 \; \forall \b{x} \in LS(\bar{\b{x}}, \bar{\b{x}} + \delta \b{d})$$
    
    令 $\alpha \in (0, \delta)$，根据 Truncated taylor series 有

    $$
    f(\bar{\b{x}} + \alpha \b{d}) = f(\bar{\b{x}}) + g^T(\b{x}) \alpha \b{d}
    $$

    其中 $\b{x} \in LS(\bar{\b{x}}, \bar{\b{x}} + \alpha\b{d})$，所以 $g^T(\b{x})\b{d} < 0$，因此 $f(\bar{\b{x}} + \alpha \b{d}) < f(\bar{\b{x}})$ **证毕**

这个定理通俗的说就是所有与 gradient 成钝角的方向都是下降方向，如下图所示

<object data="/resource/NNP/06-md-op/descent.svg" type="image/svg+xml" class="blkcenter"></object>

注意到当 $\alpha > \hat{\alpha}$ 时，函数值反而变大。

### 1st Order Necessary Condition

<blockquote>
令 $f: \mathbb{R}^n \rightarrow \mathbb{R}, f\in \mathcal{C}^1$，如果 $\b{x}^*$ 是 local minimum，则 $g(\b{x}^*) = 0$
</blockquote>

* 证明

    假设 $\b{x}^\*$ 是 local minimum 且 $g(\b{x}^\*) \neq 0$，令 $\b{d} = -g(\b{x}^\*)$，则 $g^T(\b{x}^\*)d < 0$，也就是 $\b{d}$ 是 descent direction，这与 $\b{x}^\*$ 是 local minimum 的事实不符，因此 $g(\b{x}^\*) = 0$

这个定理为优化算法提供了一个算法停止的条件，满足 $g(\b{x}^\*) = 0$ 的点被称为 stationary point，stationary point 有 3 种可能，分别是 local maximum, local minimum, saddle point，因此单纯 $g(\b{x}^\*) = 0$ 还是不够的。

### 2nd Order Necessary Condition

<blockquote>
令 $f: \mathbb{R}^n \rightarrow \mathbb{R}, f\in \mathcal{C}^2$，如果 $\b{x}^*$ 是 local minimum，则 $H(\b{x}^*)$ 是 positive semi-definite matrix
</blockquote>

* 证明

    假设存在 $\b{d}$ 使得 $\b{d}^T H(\b{x}^\*)\b{d} < 0$，由于 $f \in \mathcal{C}^2$，所以 $H \in \mathcal{C}$，因此存在 $\delta > 0$，使得
    $$\b{d}^T H(\b{x}^\* + \alpha \b{d})\b{d} < 0 \; \forall \alpha \in (0, \delta)$$
    
    根据 Truncated taylor series

    $$
    f(\b{x}^\* + \alpha \b{d}) = f(\b{x}^\*) + g(\b{x}^\*)\alpha \b{d} + \alpha \b{d}^T H(\bar{\b{x}}) \alpha \b{d}
    $$

    其中 $\bar{\b{x}} \in LS(\b{x}^\*, \b{x}^\* + \alpha \b{d})$，根据前面定理，$g(\b{x}^\*) = 0$，这样就有 $f(\b{x}^\* + \alpha \b{d}) < f(\b{x}^\*)$，这与 $\b{x}^\*$ 是 local minimum 相违背。 **证毕**

### 2nd Order Sufficient Condition

<blockquote>
令 $f: \mathbb{R}^n \rightarrow \mathbb{R}, f\in \mathcal{C}^2$，如果 $g(\b{x}^*) = 0, H(\b{x}^*)$ 是 positive definite matrix，则 $\b{x}^*$ 是 strictly local minimum
</blockquote>

证明简单略去

### Iterative Optimization Algorithm

上面的理论给出了 Iterative Optimization 的理论基础，一个迭代优化算法会产生一个 sequence $\\{\b{x}^k\\}_{k \geq 0}$，这个 sequence 会最后收敛到一个 local minimum，这样的迭代算法可以用下面的框架表示

    Initialize $\b{x}^0, k = 0$
    while stopping condition is not satisfied
      Find $\b{x}^{k+1}$ such that $f(\b{x}^{k+1}) < f(\b{x}^k)$
      Set $k = k+1$
    end while
    output $\b{x}^* = \b{x}^k$

这个迭代算法中有这个几个点需要注意

* 怎么找到符合条件的 $\b{x}^{k+1}$
* Stopping condition 怎么确定
* 算法是否会最终收敛，如果能收敛，收敛的速度多快
* 根据初始值 $\b{x}^0$ 的不同，算法的收敛性和收敛速度会不会受到影响
