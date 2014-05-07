---
layout: post
title: 05 - Convex Function
categories: nnumop
tags: NPTEL, numerical optimization
---

#### Convex Function

<blockquote>
令 $C \in \mathbb{R}^n$ 为非空 convex set，函数 $f: C \rightarrow \mathbb{R}$，如果 $f$ 满足如下条件

$$ f(\lambda \boldsymbol{x}_1 + (1 - \lambda) \boldsymbol{x}_2) \leq \lambda f(\boldsymbol{x}_1) + (1 - \lambda) f(\boldsymbol{x}_2) \;\; \forall \lambda \in [0, 1], \boldsymbol{x}_1,\boldsymbol{x}_2 \in C $$

则函数 $f$ 称为 convex function
</blockquote>

注意 $C$ 是个 convex set，否则不能保证所有的 $\lambda \boldsymbol{x}\_1 + (1 - \lambda)\boldsymbol{x}\_2$ 都在 $C$ 内。

如果条件中 $\leq$ 变成 $<$，同时 $\lambda \in (0, 1)$ 则函数 $f$ 成为 strictly convex function。

Convex function 用下面的图表示最直观了

<object data="/resource/NNP/05-convex-func/convex_func.svg" type="image/svg+xml" class="blkcenter"></object>

Convex function 和 Concave function 是两个相对的概念，函数 $f$ 如果是 concave function，则 $-f$ 就是 convex function；如果 $f$ 如果是 strictly concave function，则 $-f$ 就是 strictly convex function。

#### Convex Programming Problem

所谓的 convex programming problem，其实就是指如下问题

$$
\begin{align}
\min f(\boldsymbol{x}) \\\\
s.t. \boldsymbol{x} \in C
\end{align}
$$

其中 $C$ 是 convex set，$f: C \rightarrow \mathbb{R}$ 为 convex function

----------

<blockquote>
Convex programming 中每个 local minimum 都是 global minimum
</blockquote>

* 证明

  <object data="/resource/NNP/05-convex-func/localisglobal.svg" type="image/svg+xml" class="blkcenter"></object>

----------

<blockquote>
Convex programming 的所有 global minimum 构成一个 convex set
</blockquote>

通俗的讲就是如果一个 convex programming problem 有多个最优解，那这些最优解必然是在一块的，不是分散的，如下图所示

<object data="/resource/NNP/05-convex-func/many_global.svg" type="image/svg+xml" class="blkcenter"></object>

其中最优解是连在一起的。
