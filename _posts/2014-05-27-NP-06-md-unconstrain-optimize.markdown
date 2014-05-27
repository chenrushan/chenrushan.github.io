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
