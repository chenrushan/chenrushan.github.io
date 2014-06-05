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

其中 $\varepsilon$ 是一个用户指定的很小的数，第一个条件就是 $g(\boldsymbol{x}^k) = 0$ 的一个近似，第二个条件表示当前轮的迭代是否能使 $f(\boldsymbol{x}^k)$ 有显著下降，如果没有，则停止迭代

#### Speed of Convergence

<blockquote>
假设优化过程对应 sequence $\{\boldsymbol{x}^k\}_{k \geq 0}$，且 $\boldsymbol{x}^*$ 为 local minimum，如果下式成立

$$\lim_{k\rightarrow \infty} \frac{\Vert \boldsymbol{x}^{k+1} - \boldsymbol{x}^*\Vert }{\Vert \boldsymbol{x}^k - \boldsymbol{x}^*\Vert^p} = \beta$$

则 $p$ 表示 order of convergence，$\beta$ 表示 convergence rate
</blockquote>

* $p = 1, 0 < \beta < 1$ (linear convergence)

  * $\beta = 0.1, \Vert \boldsymbol{x}^0 - \boldsymbol{x}^* \Vert = 0.1$

     收敛过程是 $10^{-1}, 10^{-2}, 10^{-3}, 10^{-4}, ...$

  * $\beta = 0.9, \Vert \boldsymbol{x}^0 - \boldsymbol{x}^* \Vert = 0.1$

     收敛过程是 $10^{-1}, 0.09, 0.081, 0.0729, ...$

  可以看到 $\beta$ 越小，收敛越快

* $p = 2, \beta > 0$ (qudratic convergence)

  * $\beta = 1, \Vert \boldsymbol{x}^0 - \boldsymbol{x}^* \Vert = 0.1$

     收敛过程是 $10^{-1}, 10^{-2}, 10^{-4}, ...$

  可以看出 quadratic 的收敛过程比 linear 要快得多

* superlinear convergence

  如果收敛过程符合如下条件

  $$\lim_{k\rightarrow \infty} \frac{\Vert \boldsymbol{x}^{k+1} - \boldsymbol{x}^* \Vert}{\Vert \boldsymbol{x}^k - \boldsymbol{x}^* \Vert} = 0, \lim_{k\rightarrow \infty} \frac{\Vert \boldsymbol{x}^{k+1} - \boldsymbol{x}^* \Vert}{\Vert \boldsymbol{x}^k - \boldsymbol{x}^* \Vert^2} = \infty$$

  这被称为 superlinear convergence，它的收敛速度介于 linear 和 quadratic 之间，我们后续见到的大多算法都属于 superlinear convergence

Error function

#### Find $\boldsymbol{x}^{k+1}$

从 $\boldsymbol{x}^k$ 到 $\boldsymbol{x}^{k + 1}$ 需要明确以下两点

* 确定 descent direction $d^{k}$
* 确定 step length $\alpha^{k}$

关于 descent direction 的确定会在后面的好多节中详细叙述，这里讲一下如何确定 step length，假设 $\boldsymbol{d}^k$ 已经确定，求解 $\alpha^k$ 的方法分为两种

* Exact line search

  把 $\alpha^k$ 的求解当成是另一个优化问题，即在每一步迭代过程中再求解

  $$\alpha^k = \min\_{\alpha} f(\boldsymbol{x}^k + \alpha \boldsymbol{d}^k)$$

* Inexact line search

  Exact line search 有时会带来性能上的问题，这就需要使用近似的方法
