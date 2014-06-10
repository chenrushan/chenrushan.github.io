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

$$\lim_{k\rightarrow \infty} \frac{\Vert \boldsymbol{x}^{k+1} - \boldsymbol{x}^*\Vert }{\Vert \boldsymbol{x}^k - \boldsymbol{x}^*\Vert^p} = \beta \;\; \beta < \infty$$

则 $p$ 表示 order of convergence，$\beta$ 表示 convergence rate
</blockquote>

注意到这里的分子分母都是表示离最优点的距离，所以上面的定义是用距离的比值来表示 convergence 的快慢

* $p = 1, 0 < \beta < 1$ (linear convergence)

  * $\beta = 0.1, \Vert \boldsymbol{x}^0 - \boldsymbol{x}^* \Vert = 0.1$

     收敛过程是 $10^{-1}, 10^{-2}, 10^{-3}, 10^{-4}, ...$

  * $\beta = 0.9, \Vert \boldsymbol{x}^0 - \boldsymbol{x}^* \Vert = 0.1$

     收敛过程是 $10^{-1}, 0.09, 0.081, 0.0729, ...$

  可以看到 $\beta$ 越小，收敛越快

* $p = 2, \beta > 0$ (quadratic convergence)

  * $\beta = 1, \Vert \boldsymbol{x}^0 - \boldsymbol{x}^* \Vert = 0.1$

     收敛过程是 $10^{-1}, 10^{-2}, 10^{-4}, ...$

  可以看出 quadratic 的收敛过程比 linear 要快得多

* superlinear convergence

  如果收敛过程符合如下条件

  $$\lim_{k\rightarrow \infty} \frac{\Vert \boldsymbol{x}^{k+1} - \boldsymbol{x}^* \Vert}{\Vert \boldsymbol{x}^k - \boldsymbol{x}^* \Vert} = 0, \lim_{k\rightarrow \infty} \frac{\Vert \boldsymbol{x}^{k+1} - \boldsymbol{x}^* \Vert}{\Vert \boldsymbol{x}^k - \boldsymbol{x}^* \Vert^2} = \infty$$

  这被称为 superlinear convergence，它的收敛速度介于 linear 和 quadratic 之间
  
由于 linear convergence 收敛得慢，而 quadratic convergence 虽然收敛快但是需要的资源太多，所以大多数算法都是属于 superlinear convergence

#### Find $\boldsymbol{x}^{k+1}$

从 $\boldsymbol{x}^k$ 到 $\boldsymbol{x}^{k + 1}$ 需要明确以下两点

* 确定 descent direction $d^{k}$
* 确定 step length $\alpha^{k}$

关于 descent direction 的确定会在后面的好多节中详细叙述，这里讲一下如何确定 step length，假设 $\boldsymbol{d}^k$ 已经确定，求解 $\alpha^k$ 的方法分为两种，分别是 Exact line search 和 Inexact line search。

##### Exact line search

把 $\alpha^k$ 的求解当成是另一个优化问题，即在每一步迭代过程中再求解

$$\alpha^k = \min\_{\alpha} f(\boldsymbol{x}^k + \alpha \boldsymbol{d}^k)$$

由于 $\alpha$ 是个 scalar，所以这是一个一维优化问题。

##### Inexact line search

Exact line search 有时会带来性能上的问题，这时就需要使用近似的方法，不过在使用近似的方法时需要注意以下几点

* $\alpha^k$ 不能太大，太大函数值反而上升
* $\alpha^k$ 不能太小，太小则函数值的变化太小，收敛也慢
* 函数值下降相对于 $\alpha^k$ 要比较显著，函数值下降不一定要求绝对值很大，但应该相对于 $\alpha^k$ 是显著的，换句话说，就是 rate of decrease 要比较大

为了保证以上 3 点就有了 Armijo's condition, Goldstein's condition 和 Wolfe's condition

假设 $f(\boldsymbol{x}^k + \alpha \boldsymbol{d}^k)$ 的函数图像是这样 (其中 $\alpha$ 是变量)

<object data="/resource/NNP/07-line-search/f_alpha.svg" type="image/svg+xml" class="blkcenter"></object>

图中有两条虚线

* 横虚线的函数是 $y = f(\boldsymbol{x}^k)$，即 $f(\boldsymbol{x}^k + \alpha \boldsymbol{d}^k)$ 在 $\alpha  = 0$ 的取值
* 斜虚线的函数是 $y = f(\boldsymbol{x}^k) + \alpha g^T(\boldsymbol{x}^k)\boldsymbol{d}^k$，即 $f(\boldsymbol{x}^k + \alpha \boldsymbol{d}^k)$ 在 $\alpha  = 0$ 处的切线

下面分别讨论这 3 种 condition

* Armijo's condition

  Armijo's condition 给出下面的绿色虚线，由于其斜率介于 $0$ 和 $g^T(\boldsymbol{x}^k)\boldsymbol{d}^k$ 之间，所以可以将斜率值定义为 $c\_1 g^T(\boldsymbol{x}^k)\boldsymbol{d}^k \; c_1 \in (0, 1)$
  
  <object data="/resource/NNP/07-line-search/amijo.svg" type="image/svg+xml" class="blkcenter"></object>

  Armijo's condition 要求 step length $\alpha^k$ 满足 $f(\boldsymbol{x}^k + \alpha^k \boldsymbol{d}^k) < f(\boldsymbol{x}^k) + c\_1 \alpha^k g^T(\boldsymbol{x}^k)\boldsymbol{d}^k$

  这个条件一来保证了 $\alpha^k$ 不会太大，因为上述条件保证了函数值一定是下降的；二来保证了 rate of decrease 不会太小，因为 $\frac{f(\boldsymbol{x}^k) - f(\boldsymbol{x}^k + \alpha^k \boldsymbol{d}^k)}{\alpha^k} > c\_1 g^T(\boldsymbol{x}^k)\boldsymbol{d}^k$，其中 $g^T(\boldsymbol{x}^k)\boldsymbol{d}^k$ 为最大可能的 rate of decrease。

* Goldstein's condition

  Goldstein's condition 给出下面的红色虚线，由于其斜率介于 $0$ 和 $g^T(\boldsymbol{x}^k)\boldsymbol{d}^k$ 之间，所以可以将斜率值定义为 $c\_2 g^T(\boldsymbol{x}^k)\boldsymbol{d}^k \; c_2 \in (0, 1)$

  <object data="/resource/NNP/07-line-search/goldstein.svg" type="image/svg+xml" class="blkcenter"></object>

  Goldstein's condition 要求 step length $\alpha^k$ 满足 $f(\boldsymbol{x}^k + \alpha^k \boldsymbol{d}^k) > f(\boldsymbol{x}^k) + c\_2 \alpha^k g^T(\boldsymbol{x}^k)\boldsymbol{d}^k$，这样 $\alpha$ 就必须大于 $\hat{\alpha}$，这个条件保证了 step length 不会太小

  通常 Goldstein's condition 和 Armijo's condition 一起使用，这样就同时满足了前面提出的 3 个要求，在这种情况下，$c\_2$ 的取值范围是 $(c\_1, 1)$

* Wolfe's condition

  Wolfe's condition 的作用和 Goldstein's condition 是一样的，都是要保证 step length 不会太小，只是用的方法不一样，Wolfe's condition 通过限制 $\alpha^k$ 处的函数斜率来保证的。如下图中给出的斜虚线，假设其斜率有 $c g^T(\boldsymbol{x}^k)\boldsymbol{d}^k \; c\in (0, 1)$

  <object data="/resource/NNP/07-line-search/wolfe.svg" type="image/svg+xml" class="blkcenter"></object>

  Wolfe's condition 要求 $f'(\boldsymbol{x}^k + \alpha^k \boldsymbol{d}^k) > c g^T(\boldsymbol{x}^k) \boldsymbol{d}^k$，这样符合条件的 $\alpha$ 就只能是 $(\hat{\alpha}\_1, \hat{\alpha}\_2) \cup (\hat{\alpha}\_3, +\infty)$，也就保证了 step length 不会太小

  同样 Wolfe's condition 也通常和 Armijo's condition 一起使用
