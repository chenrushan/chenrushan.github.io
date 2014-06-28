---
layout: post
title: 08 - Steepest Descent Algorithm
categories: nnumop
tags: NPTEL, numerical optimization
---

<span style="background-color:#afa">这篇文章中画了很多 contour 的图，是通过这个[脚本](../../../../resource/NNP/08-steepest/examples.py)实现的</span>

#### Steepest Descent Algorithm

Steepest Descent Algorithm 在每一轮迭代的过程中对函数做 affine approximation，也就是用一阶 taylor series 去近似 $f(\boldsymbol{x})$

$$f(\boldsymbol{x}) \approx f(\boldsymbol{x}^k) + f'(\boldsymbol{x}^k)(\boldsymbol{x} - \boldsymbol{x}^k)$$

其中 $\boldsymbol{x}^k$ 表示第 k 轮迭代得到的 $\boldsymbol{x}$，$\boldsymbol{x} - \boldsymbol{x}^k$ 实际上就是我们要找的 $\boldsymbol{d}^k$，为了方便后面用 $f^k$ 表示 $f(\boldsymbol{x}^k)$，$\boldsymbol{g}^k$ 表示 $f'(\boldsymbol{x}^k)$，这样上式就变成 $f(\boldsymbol{x}^k) + {\boldsymbol{g}^k}^T \boldsymbol{d}^k$

Steepest Descent 就是去找到能够最小化近似函数的 $\boldsymbol{d}^k$，即

$$ \underset{\boldsymbol{d}^k}{\arg\min} \;\; f(\boldsymbol{x}^k) + {\boldsymbol{g}^k}^T \boldsymbol{d}^k$$

这里面 $f(\boldsymbol{x}^k)$ 是个 constant，可以从式子中去掉，另外，如果 $\boldsymbol{d}^k$ 不做任何限制的话，它可以是任意一个无穷小的向量，这样优化就没有意义了，所以我们限制 $\Vert \boldsymbol{d}^k \Vert = 1$，这样最小化问题就变成了

$$
\begin{align}
\underset{\boldsymbol{d}^k}{\arg\min} \;\; {\boldsymbol{g}^k}^T \boldsymbol{d}^k \\\\
s.t. \Vert \boldsymbol{d}^k \Vert = 1
\end{align}
$$

这个优化问题很好解

$$
{\boldsymbol{g}^k}^T \boldsymbol{d}^k = \Vert \boldsymbol{g}^k \Vert \Vert \boldsymbol{d}^k \Vert \cos \theta = \Vert \boldsymbol{g}^k \Vert \cos \theta
$$

当 $\theta = \pi$ 时这个式子最小，也就是 $\boldsymbol{d}^k$ 和 $\boldsymbol{g}^k$ 的夹角 $\pi$ 时上述近似函数值最小，如下图所示

<object data="/resource/NNP/08-steepest/descent.svg" type="image/svg+xml" class="blkcenter"></object>

上节中提到 $\boldsymbol{d}^k$ 都可以表示成 $-A^k \boldsymbol{g}^k$，对于 steepest descent，$A^k = I$。

#### Examples

现在让我们通过几个例子来看看 steepest descent 在不同情况下的表现

##### $f(\boldsymbol{x}) = (\boldsymbol{x}\_1 - 7)^2 + (\boldsymbol{x}\_2 - 2)^2$

这个函数最优值在 (7, 2)，利用 steepest descent algorithm + exact line search，不论初始点选择在哪儿都是一步就能到最优点，如下图所示

<img style="width:80%" src="/resource/NNP/08-steepest/circular.png" />

##### $f(\boldsymbol{x}) = 4\boldsymbol{x}\_1^2 + \boldsymbol{x}\_2^2 -2\boldsymbol{x}\_1\boldsymbol{x}\_2$

这个函数的最优值点在 (0, 0)，同样我们用 steepest descent + exact line search

* 初始点为 (-1, -2)，函数的收敛过程如下图所示，以 0.001 为 gradient norm 的阈值，共迭代 27 步，实现见开头给出的脚本

  <img style="width:80%" src="/resource/NNP/08-steepest/ellip2.png" />

* 初始点为 (1, 0)，函数的收敛过程如下图所示，以 0.001 为 gradient norm 的阈值，共迭代 5 步

  <img style="width:80%" src="/resource/NNP/08-steepest/ellip1.png" />

这个例子我们可以看出初始点的不同对收敛速度是有影响的

##### $f(\boldsymbol{x}) = 100(\boldsymbol{x}\_2 - \boldsymbol{x}\_1^2)^2 + (1 - \boldsymbol{x}\_1)^2$

这个是著名的 Rosenbrock function，其最优值出现在 (1, 1) 点，利用 steepest descent + backtrack line search ($\hat{\alpha} = 0.5, \lambda = 0.3, c\_1 = 1\times 10^{-4}$)

* 初始点为 (0.6, 0.6)，收敛过程如下图所示，以 0.001 为 gradient norm 的阈值，共迭代 2029 步

  <img style="width:80%" src="/resource/NNP/08-steepest/rosen1.png" />

* 初始点为 (-1.2, 1)，收敛过程如下图所示，以 0.001 为 gradient norm 的阈值，共迭代 2300 步

  <img style="width:80%" src="/resource/NNP/08-steepest/rosen2.png" />

对于这个例子，不管你选那个初始点，迭代的过程总是很慢

上面的几个例子中，收敛的过程有快有慢，下面我们从理论的角度看看是什么导致了这种区别

#### Convergence Rate of Steepest Descent Algorithm

