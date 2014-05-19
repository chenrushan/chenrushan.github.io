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

如果条件中 $\leq$ 变成 $<$，同时 $\lambda \in (0, 1)$ 则函数 $f$ 称为 strictly convex function。

Convex function 用下面的图表示最直观了

<object data="/resource/NNP/05-convex-func/convex_func.svg" type="image/svg+xml" class="blkcenter"></object>

Convex function 和 Concave function 是两个相对的概念，$f$ 如果是 concave function，$-f$ 就是 convex function；如果 $f$ 是 strictly concave function，$-f$ 就是 strictly convex function。

#### Convex Programming Problem

所谓的 convex programming problem，就是指如下问题

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

  假设 local minimum 为 $\boldsymbol{x}^*$，根据 local minimum 的定义我们知道

  $$\boldsymbol{x}^* = \underset{\boldsymbol{x} \in C \cap B(\boldsymbol{x}^*, \delta)}{\arg\min} f(\boldsymbol{x}) $$

  参考下图，其中绿色的圈表示 $C \cap B(\boldsymbol{x}^*, \delta)$

  <object data="/resource/NNP/05-convex-func/localisglobal.svg" type="image/svg+xml" class="blkcenter"></object>

  假设 $\boldsymbol{y} \in C \cap B(\boldsymbol{x}^*, \delta)$，$\boldsymbol{z}$ 为 $LS(\boldsymbol{x}^*, \boldsymbol{y})$ 延长线上任意一点且在 $C$ 内，则 $\boldsymbol{y}$ 可以表示为 $\lambda \boldsymbol{x} + (1 - \lambda) \boldsymbol{z} \; \lambda \in (0, 1)$，则有

  $$
  f(\boldsymbol{x}^*) \leq f(\boldsymbol{y}) = f(\lambda \boldsymbol{x}^* + (1 - \lambda) \boldsymbol{z}) \leq \lambda f(\boldsymbol{x}^*) + (1 - \lambda) f(\boldsymbol{z})
  $$

  这也就推出 $f(\boldsymbol{x}^*) \leq f(\boldsymbol{z})$

----------

<blockquote>
Convex programming 的所有 global minimum 构成一个 convex set
</blockquote>

通俗的讲就是如果一个 convex programming problem 有多个最优解，那这些最优解必然是在一块的，不是分散的，如下图所示

<object data="/resource/NNP/05-convex-func/many_global.svg" type="image/svg+xml" class="blkcenter"></object>

其中最优解是连在一起的。

* 证明

  假设 $\boldsymbol{x}\_1, \boldsymbol{x}\_2$ 为 local minimum

  $$
  f(\lambda \boldsymbol{x}\_1 + (1 - \lambda) \boldsymbol{x}\_2) \leq \lambda f(\boldsymbol{x}\_1) + (1 - \lambda) f(\boldsymbol{x}\_2) = f(\boldsymbol{x}\_1)
  $$

  这里不等号不能成立，所以 $\forall \lambda \in [0, 1] \; \lambda \boldsymbol{x}\_1 + (1 - \lambda) \boldsymbol{x}\_2$ 也都是 local minimum

#### Epigraph

给定 $f: X \rightarrow \mathbb{R}$，其对应的 epigraph 是集合 $\\{ (\boldsymbol{x}, y) : \boldsymbol{x} \in X, y \geq f(\boldsymbol{x})\\}$，所以 epigraph 属于 $\mathbb{R}^{n+1}$，参考下图，其中填充的部分就是 epigraph，当然 epigraph 是无限延伸的，这里只给出了其中的一部分而已。

<object data="/resource/NNP/05-convex-func/epigraph.svg" type="image/svg+xml" class="blkcenter"></object>

<blockquote>
给定 $C \in \mathbb{R}^n$ 为 convex set，$f: C \rightarrow \mathbb{R}$ 为 convex function 当且仅当其对应的 epigraph 为 convex set
</blockquote>

* 证明

  * convex function $\Rightarrow$ epigraph 为 convex set

     简单，略过

  * epigraph 为 convex set $\Rightarrow$ convex function

     利用 $(\boldsymbol{x}\_1, f(\boldsymbol{x}\_1)), (\boldsymbol{x}\_2, f(\boldsymbol{x}\_2)) \in$ epigraph 的性质即可证得

与 epigraph 相对的一个概念是 hypograph，hypograph 是这样的集合 $\\{ (\boldsymbol{x}, y) : \boldsymbol{x} \in X, y \leq f(\boldsymbol{x})\\}$

#### Level Set

Level set 是这么一个集合 $C\_{\alpha} = \\{ \boldsymbol{x} \in C : f(\boldsymbol{x}) \leq \alpha, \alpha \in \mathbb{R} \\}$

如果 $f(\boldsymbol{x})$ 是 convex function 则 $C\_{\alpha}$ 是一个 convex set (证明简单)，反之不成立，比如对于 $f(x) = x^3$，它的 level set 就是 convex set，但是函数并不是 convex function。

#### Hessian Matrix

<blockquote>
假设 $C \subset \mathbb{R}^n$ 是 open convex set，函数 $f: C \rightarrow \mathbb{R}$ 二阶连续可导，则 $f$ 是 convex function 当且仅当 $f$ 对应的 Hessian matrix 是 positive semi-definite matrix
</blockquote>

* 证明

  记 Hessian matrix 为 $H(\boldsymbol{x})$

  * $f$ is convex function $\Rightarrow$ $H(\boldsymbol{x})$ PSD

  * $H(\boldsymbol{x})$ PSD $\Rightarrow$ $f$ is convex function 

     给定 $\boldsymbol{x}\_1, \boldsymbol{x}\_2 \in C$，根据 Truncated Taylor Series 有

     $$f(\boldsymbol{x}\_2) = f(\boldsymbol{x}\_1) + f'(\boldsymbol{x}\_1)(\boldsymbol{x}\_2 - \boldsymbol{x}\_1) + \frac{1}{2} (\boldsymbol{x}\_2 - \boldsymbol{x}\_1)^T H(\boldsymbol{x}) (\boldsymbol{x}\_2 - \boldsymbol{x}\_1)$$

     其中 $\boldsymbol{x}$ 为 $\boldsymbol{x}\_1, \boldsymbol{x}\_2$ 之间的任意一点

     由于 $H(\boldsymbol{x})$ PSD，所以 $(\boldsymbol{x}\_2 - \boldsymbol{x}\_1)^T H(\boldsymbol{x}) (\boldsymbol{x}\_2 - \boldsymbol{x}\_1) \geq 0$，所以

     $$f(\boldsymbol{x}\_2) \geq f(\boldsymbol{x}\_1) + f'(\boldsymbol{x}\_1)(\boldsymbol{x}\_2 - \boldsymbol{x}\_1)$$

     根据前面的定理可知，$f$ 为 convex function

