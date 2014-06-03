---
layout: post
title: 07 - Line Search Technique
categories: nnumop
tags: NPTEL, numerical optimization
---

这一节回答上一节最后提出的几个问题

#### Stopping Conditions

前面提到利用 $g(\boldsymbol{x}^k) = 0$ 只能确定 $\boldsymbol{x}^k$ 是个 stationary point，必须再根据 $H(\boldsymbol{x}^k)$ 的性质才能确定 $\boldsymbol{x}^k$ 是否为真的 local minimum，但在实际中由于计算和判断 $H(\boldsymbol{x}^k)$ 涉及的计算资源较多，所以通常只利用 $g(\boldsymbol{x}^k)$ 来作为 stopping condition，并且也不是判断 $g(\boldsymbol{x}^k)$ 是否等于 $0$，由于计算机的精度问题，通常这个判断是很难成立的。

实际中常用的 stopping condition 包括

* $\Vert g(\boldsymbol{x}^k) \Vert \leq \varepsilon$

* $\frac{f(\boldsymbol{x}^k) - f(\boldsymbol{x}^{k+1})}{|f(\boldsymbol{x}^k)|} \leq \varepsilon$

其中 $\varepsilon$ 是一个用户指定的很小的数，第一个条件就是 $g(\boldsymbol{x}^k) = 0$ 的一个近似，第二个条件表示当前轮的迭代是否能使 $f(\boldsymbol{x}^k)$ 有显著下降

#### Speed of Convergence

<blockquote>
假设优化过程对应 sequence $\{\boldsymbol{x}^k\}_{k \geq 0}$，且 $\boldsymbol{x}^*$ 为 local minimum，如果下式成立

$$\lim_{k\rightarrow \infty} \frac{|\boldsymbol{x}^{k+1} - \boldsymbol{x}^*|}{|\boldsymbol{x}^k - \boldsymbol{x}^*|^a} = \alpha$$

则 $a$ 表示 order of convergence，$\alpha$ 表示 convergence rate
</blockquote>
