---
layout: post
title: 06 - Multi-Dimensional Unconstrained Optimization
categories: nnumop
tags: NPTEL, numerical optimization
---

#### Descent Direction

Descent direction 在 multi-dimensional optimization 中是一个非常重要的概念，很多优化算法的核心就是如何构造一个好的 descent direction。

<blockquote>
令 $\bar{\boldsymbol{x}} \in \mathbb{R}^n$，如果存在一个方向 $\boldsymbol{d} \in \mathbb{R}^n, \delta > 0$ 使得 $f(\bar{\boldsymbol{x}} + \alpha \boldsymbol{d}) < f(\bar{\boldsymbol{x}}) \; \forall \alpha \in (0, \delta)$，则 $\boldsymbol{d}$ 就被称为 descent direction
</blockquote>

所以 $\boldsymbol{d}$ 和 $\boldsymbol{x}$ 处于一个空间内

<blockquote>
令 $f \in \mathcal{C}^1, \bar{\boldsymbol{x}} \in \mathbb{R}^n$，$g(\bar{\boldsymbol{x}})$ 为 $f$ 在 $\bar{\boldsymbol{x}}$ 处的 gradient，如果 $g^T(\bar{\boldsymbol{x}})d < 0$，则 $d$ 为 $f$ 在 $\bar{\boldsymbol{x}}$ 处的 descent direction
</blockquote>

* 证明

  因为 $f\in \mathcal{C}^1$，所以 $g \in \mathcal{C}^0$，又因为 $g^T(\bar{\boldsymbol{x}})\boldsymbol{d} < 0$，所以必存在 $\delta$，使得 $g^T(\boldsymbol{x})\boldsymbol{d} < 0 \; \forall \boldsymbol{x} \in B(\bar{\boldsymbol{x}}, \delta)$
  
  令 $\alpha \in (0, \delta)$，根据 Truncated taylor series 有

  $$
  f(\bar{\boldsymbol{x}} + \alpha \boldsymbol{d}) = f(\bar{\boldsymbol{x}}) + g^T(\boldsymbol{x}) \alpha \boldsymbol{d}
  $$

  其中 $\boldsymbol{x} \in LS[\bar{\boldsymbol{x}}, \bar{\boldsymbol{x}} + \alpha\boldsymbol{d}] \in B(\bar{\boldsymbol{x}}, \delta)$，所以 $g^T(\boldsymbol{x})\boldsymbol{d} < 0$，因此 $f(\bar{\boldsymbol{x}} + \alpha \boldsymbol{d}) < f(\bar{\boldsymbol{x}})$ **证毕**

#### 1st Order Necessary Condition

<blockquote>
令 $f: \mathbb{R}^n \rightarrow \mathbb{R}, f\in \mathcal{C}^1$，如果 $\boldsymbol{x}^*$ 是 local minimum，则 $g(\boldsymbol{x}^*) = 0$
</blockquote>

* 证明

  假设 $\boldsymbol{x}^*$ 是 local minimum 且 $g(\boldsymbol{x}^*) \neq 0$，令 $\boldsymbol{d} = -g(\boldsymbol{x}^*)$，则 $g^T(\boldsymbol{x}^*)d < 0$，也就是 $\boldsymbol{d}$ 是 descent direction，这与 $\boldsymbol{x}^*$ 是 local minimum 的事实不符，因此 $g(\boldsymbol{x}^*) = 0$

这个定理为优化算法提供了一个算法停止的条件，满足 $g(\boldsymbol{x}^*) = 0$ 的点被称为 stationary point，stationary point 有 3 种可能，分别是 local maximum, local minimum, saddle point，因此单纯 $g(\boldsymbol{x}^*) = 0$ 还是不够的。

#### 2nd Order Necessary Condition

<blockquote>
令 $f: \mathbb{R}^n \rightarrow \mathbb{R}, f\in \mathcal{C}^2$，如果 $\boldsymbol{x}^*$ 是 local minimum，则 $H(\boldsymbol{x}^*)$ 是 positive semi-definite matrix
</blockquote>

* 证明

  假设存在 $\boldsymbol{d}$ 使得 $\boldsymbol{d}^T H(\boldsymbol{x}^*)\boldsymbol{d} < 0$，由于 $f \in \mathcal{C}^2$，所以 $H \in \mathcal{C}$，因此存在 $\delta > 0$，使得 $\boldsymbol{d}^T H(\boldsymbol{x}^* + \alpha \boldsymbol{d})\boldsymbol{d} < 0 \; \forall \alpha \in (0, \delta)$，根据 Truncated taylor series

  $$
  f(\boldsymbol{x}^* + \alpha \boldsymbol{d}) = f(\boldsymbol{x}^*) + g(\boldsymbol{x}^*)\alpha \boldsymbol{d} + \alpha \boldsymbol{d}^T H(\bar{\boldsymbol{x}}) \alpha \boldsymbol{d}
  $$

  其中 $\bar{\boldsymbol{x}} \in LS(\boldsymbol{x}^*, \boldsymbol{x}^* + \alpha \boldsymbol{d})$，根据前面定理，$g(\boldsymbol{x}^*) = 0$，这样就有 $f(\boldsymbol{x}^* + \alpha \boldsymbol{d}) < f(\boldsymbol{x}^*)$，这与 $\boldsymbol{x}^*$ 是 local minimum 相违背。 **证毕**

#### 2nd Order Sufficient Condition

<blockquote>
令 $f: \mathbb{R}^n \rightarrow \mathbb{R}, f\in \mathcal{C}^2$，如果 $g(\boldsymbol{x}^*) = 0, H(\boldsymbol{x}^*)$ 是 positive definite matrix，则 $\boldsymbol{x}^*$ 是 strictly local minimum
</blockquote>

证明简单略去
