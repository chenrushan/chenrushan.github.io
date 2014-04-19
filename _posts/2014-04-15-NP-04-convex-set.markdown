---
layout: post
title: 04 - Convex Set
categories: nnumop
tags: NPTEL, numerical optimization
---

这篇文章主要介绍各种和 Convex Set 相关的概念和性质。

#### Line and Line Segment

<blockquote>
给定两个点 $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathbb{R}^n$，line 可以被定义为

$$(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2 \;\; \forall \lambda \in \mathbb{R} $$
</blockquote>

考虑下面这个图

<object data="/resource/NNP/04-convex/line.svg" type="image/svg+xml" class="blkcenter"></object>

根据向量相加的原则可知虚线上的点都可以表示成 $\boldsymbol{x}\_1 + \lambda (\boldsymbol{x}\_2 - \boldsymbol{x}\_1) \; \forall \lambda \in \mathbb{R}$，也就是 $(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2$。

对于 line segment，只要限定 $\lambda$ 在 $[0, 1]$ 之间即可，即

<blockquote>
给定两个点 $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathbb{R}^n$，line segment 可以被定义为

$$(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2 \;\; \forall \lambda \in [0, 1] $$

Line segment 也被记为 $LS[\boldsymbol{x}_1, \boldsymbol{x}_2]$
</blockquote>

#### Affine Set

<blockquote>
给定集合 $A \in \mathbb{R}^n$，如果 $\forall \boldsymbol{x}_1, \boldsymbol{x}_2 \in A, \lambda \in \mathbb{R}$ 有 $(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2 \in A$，则 $A$ 被称为 Affine Set/Affine Space.
</blockquote>

这里给出一个推论，如果 $A$ 是 affine set，$\boldsymbol{x}\_1, \boldsymbol{x}\_2, \boldsymbol{x}\_3 \in A$，则 $\boldsymbol{x}\_1 + \lambda(\boldsymbol{x}\_2 - \boldsymbol{x}\_3) \in A$ (之所以给这个推论是为了下面定理的证明)。

* 证明

  $$
  \begin{align}
  & \boldsymbol{x}\_1, \boldsymbol{x}\_2, \boldsymbol{x}\_3 \in A \\\\
  \Rightarrow & (1-\alpha) \boldsymbol{x}\_1 + \alpha \boldsymbol{x}\_2,\; (1-\beta)\boldsymbol{x}\_2 + \beta \boldsymbol{x}\_3 \in A \\\\
  \Rightarrow & (1-\gamma)((1-\alpha) \boldsymbol{x}\_1 + \alpha \boldsymbol{x}\_2) + \gamma ((1-\beta)\boldsymbol{x}\_2 + \beta \boldsymbol{x}\_3) \in A \\\\
  \equiv & (1-\gamma)(1-\alpha) \boldsymbol{x}\_1 + (\alpha - \alpha \gamma + \gamma) \boldsymbol{x}\_2 - \beta\gamma (\boldsymbol{x}\_2 - \boldsymbol{x}\_3) \in A
  \end{align}
  $$

  特别的，令 $(\alpha - \alpha \gamma + \gamma) = 0$，即 $\alpha = \frac{\gamma}{\gamma - 1}$，则有 $\boldsymbol{x}\_1 - \beta\gamma (\boldsymbol{x}\_2 - \boldsymbol{x}\_3) \in A$，令 $\lambda = -\beta\gamma$，即 $\boldsymbol{x}\_1 + \lambda(\boldsymbol{x}\_2 - \boldsymbol{x}\_3) \in A$。

<blockquote>
如果 $A$ 是 affine space，$\boldsymbol{x}_1, \boldsymbol{x}_2, \cdots, \boldsymbol{x}_n \in A$ 且 $\sum_{i=1}^n \lambda_i = 1$，则 $\sum_{i=1}^n \lambda_i \boldsymbol{x}_i \in A$
</blockquote>

* 证明 (Induction)

  * 当 $n = 1$ 时，上面的理论显然成立

  * 假设当 $n = k - 1$ 是，上述结论成立，当 $n = k$ 时有

     $$
     \begin{align}
     \sum\_{i = 1}^{k} \lambda\_i \boldsymbol{x}\_i = & \lambda\_1 \boldsymbol{x}\_1 + \lambda\_2 \boldsymbol{x}\_2 + \cdots + (1 - \sum\_{i = 1}^{k - 1} \lambda\_i) \boldsymbol{x}\_k \;\; (\because \sum\_{i=1}^{k} \lambda\_i = 1) \\\\
     = & (\lambda\_1 \boldsymbol{x}\_1 + \lambda\_2 \boldsymbol{x}\_2 + \cdots + \lambda\_{k-2} \boldsymbol{x}\_{k-2} + (1 - \sum\_{i = 1}^{k - 2} \lambda\_i) \boldsymbol{x}\_k) + \lambda\_{k-1}(\boldsymbol{x}\_{k-1} - \boldsymbol{x}\_{k}) \\\\
     = & \boldsymbol{y} + \lambda\_{k-1}(\boldsymbol{x}\_{k-1} - \boldsymbol{x}\_{k}) \;\; (\boldsymbol{y} \in A) \\\\
     \end{align}
     $$

     根据上面的推论 $\boldsymbol{y} + \lambda\_{k-1}(\boldsymbol{x}\_{k-1} - \boldsymbol{x}\_{k}) \in A$，所以对于 $n = k$ 上述结论也成立。

----------

注意 affine space 和 vector space 的区别 (视频里一直用 vector subspace，但我觉得用 space 就可以了，因为 vector subspace 我觉得是个相对的概念，而且 vector subspace 本身也是 vector space)，vector space 要求如果 $\boldsymbol{x}\_1, \boldsymbol{x}\_2 \in A$ 则 $\alpha \boldsymbol{x}\_1 + \beta \boldsymbol{x}\_2 \in A \;\; \forall \alpha, \beta \in \mathbb{R}$，它要求任意的 linear combination 都属于 $A$，比 affine space 更严格。所以，$\boldsymbol{0}$ 必须是 vector space 的一个元素，而对于 affine space 则没有这个要求，如下图所示

<object data="/resource/NNP/04-convex/affine_vector.svg" type="image/svg+xml" class="blkcenter"></object>

<blockquote>
如果 A 为 affine space，$\boldsymbol{x}_0 \in A$，则 $\{\boldsymbol{x} - \boldsymbol{x}_0: \boldsymbol{x} \in A\}$ 为 vector space
</blockquote>

* 证明

  令 $V = \\{\boldsymbol{x} - \boldsymbol{x}\_0: \boldsymbol{x} \in A\\}, \;\; \boldsymbol{x}\_1, \boldsymbol{x}\_2 \in A$，则 $\boldsymbol{x}\_1 - \boldsymbol{x}\_0, \boldsymbol{x}\_2 - \boldsymbol{x}\_0 \in V$

  $$
  \begin{align}
  & \alpha(\boldsymbol{x}\_1 - \boldsymbol{x}\_0) + \beta(\boldsymbol{x}\_2 - \boldsymbol{x}\_0) \;\; (\forall \alpha, \beta \in \mathbb{R})\\\\
  = & \alpha \boldsymbol{x}\_1 + \beta \boldsymbol{x}\_2 + (1 - \alpha - \beta) \boldsymbol{x}\_0 - \boldsymbol{x}\_0 \\\\
  = & \boldsymbol{y} - \boldsymbol{x}\_0
  \end{align}
  $$

  根据前面定理可知，$\boldsymbol{y} \in A$，所以 $\boldsymbol{y} - \boldsymbol{x}\_0 \in V$，因此 $V$ 是一个 vector space。

----------

$A\boldsymbol{x} = \boldsymbol{b}$ 的解集属于 affine set

#### Convex Set

<blockquote>
给定集合 $C \in \mathbb{R}^n$，如果 $\forall \boldsymbol{x}_1, \boldsymbol{x}_2 \in C, \lambda \in [0, 1]$ 有 $(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2 \in C$，则 $C$ 被称为 Convex Set.
</blockquote>

注意到这里的定义和 affine set 的极为相似，区别只在 $\lambda$ 的范围。对于 affine set，它要求经过 $\boldsymbol{x}\_1, \boldsymbol{x}\_2$ 的整个 line 都在集合中，而 convex set 只要求连接 $\boldsymbol{x}\_1, \boldsymbol{x}\_2$ 的 line segment 在集合中即可，所以 convex set 的要求要松很多，所有的 affine set 都同时是 convex set。

Convex set 的例子包括 empty set, singleton set, $\mathbb{R}$ 等等。

在 convex set 的基础上我们可以构造新的 convex set，常见操作包括

* Scalar multiple $\alpha C = \\{\alpha \boldsymbol{x}: \boldsymbol{x} \in C\\}$

* Sum of two sets $C = \\{\boldsymbol{x}\_1 + \boldsymbol{x}\_2: \boldsymbol{x}\_1 \in C\_1, \boldsymbol{x}\_2 \in C\_2\\}$

* Intersection $C = \cap\_i C\_i$

上述操作得到的 set 依然是 convex set，证明比较简单，就略过了。

#### Hyperplane

<blockquote>
Hyperplane 可以被定义为 $\boldsymbol{ax}=b$，其中 $\boldsymbol{a}$ 是 hyperplane 的 normal vector
</blockquote>
