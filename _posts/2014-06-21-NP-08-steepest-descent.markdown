---
layout: post
title: 08 - Steepest Descent Algorithm
categories: nnumop
tags: NPTEL, numerical optimization
---

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

当 $\theta = 2\pi$ 时这个式子最小，也就是 $\boldsymbol{d}^k$ 和 $\boldsymbol{g}^k$ 的夹角 $2\pi$ 时上述近似函数值最小，如下图所示
