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

