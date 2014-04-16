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

注意它和 vector space 的区别 (视频里一直用 vector subspace，但我觉得用 space 就可以了，因为 vector subspace 我觉得是个相对的概念，而且 vector subspace 本身也是 vector space)，vector space 要求如果 $\boldsymbol{x}\_1, \boldsymbol{x}\_2 \in A$ 则 $\alpha \boldsymbol{x}\_1 + \beta \boldsymbol{x}\_2 \in A \;\; \forall \alpha, \beta \in \mathbb{R}$，它要求任意的 linear combination 都属于 $A$，比 affine space 更严格。所以，$\boldsymbol{0}$ 必须是 vector space 的一个元素，而对于 affine space 则没有这个要求，如下图所示

<object data="/resource/NNP/04-convex/affine_vector.svg" type="image/svg+xml" class="blkcenter"></object>

<blockquote>
如果 A 为 affine space，$\boldsymbol{x}_0 \in A$，则 $\{\boldsymbol{x} - \boldsymbol{x}_0: \boldsymbol{x} \in A\}$ 为 vector space
</blockquote>

证明：

$$
\begin{align}
& \boldsymbol{y}\_1, \boldsymbol{y}\_2 \in \\{\boldsymbol{x} - \boldsymbol{x}\_0: \boldsymbol{x} \in A\\} \\\\
\Rightarrow & \boldsymbol{y}\_1 + \boldsymbol{x}\_0, \boldsymbol{y}\_2 + \boldsymbol{x}\_0 \in A \\\\
\Rightarrow & (1 - \lambda)(\boldsymbol{y}\_1 + \boldsymbol{x}\_0) + \lambda(\boldsymbol{y}\_2 + \boldsymbol{x}\_0) \in A \;\; \forall \lambda \in \mathbb{R} \\\\
\Rightarrow & (1 - \lambda)\boldsymbol{y}\_1 + \lambda\boldsymbol{y}\_2 + \boldsymbol{x}\_0 \in A \;\; \forall \lambda \in \mathbb{R} \\\\
\Rightarrow & (1 - \lambda)\boldsymbol{y}\_1 + \lambda\boldsymbol{y}\_2 \in \\{\boldsymbol{x} - \boldsymbol{x}\_0: \boldsymbol{x} \in A\\} \;\; \forall \lambda \in \mathbb{R}
\end{align}
$$

