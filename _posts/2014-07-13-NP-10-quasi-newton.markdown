---
layout: post
title: 10 - Quasi Newton Method
categories: nnumop
tags: NPTEL, numerical optimization, quasi newton
---

#### Quasi Newton Method

前一篇文章中提到了 Classical Newton 的诸多问题，针对这些问题有了 Quasi Newton Method，其基本思想是在每步迭代得到 descent direction 的时候并不计算 $\boldsymbol{d}^k = -(H^k)^{-1} \boldsymbol{g}^k$，而是计算 $\boldsymbol{d}^k = -B^k \boldsymbol{g}^k$，也就是在每步迭代时找到一个矩阵 $B^k$ 去近似 $(H^k)^{-1}$，这样每步迭代的近似函数就变为

$$f(\boldsymbol{x}) \approx y^k(\boldsymbol{x}) = f(\boldsymbol{x}^k) + {\boldsymbol{g}^k}^T(\boldsymbol{x} - \boldsymbol{x}^k) + \frac{1}{2} (\boldsymbol{x} - \boldsymbol{x}^k)^T (B^k)^{-1} (\boldsymbol{x} - \boldsymbol{x}^k)$$

利用这一近似我们就将求解 linear system 的操作转变为 matrix vector multiplication 操作，计算量大大下降

Quasi Newton 是一类算法，常见的包括如下 3 种

* Rank one correction
* DFP algorithm (<b>D</b>avidon, <b>F</b>letcher, <b>P</b>owell)
* BFGS algorithm (<b>B</b>royden, <b>F</b>letcher, <b>G</b>oldfarb, <b>S</b>hanno)

这三种算法的共同点是

* 构造 $B^k$ 使用的信息包括 $B^{k-1}, \boldsymbol{x}^{k-1}, \boldsymbol{g}^{k-1}, \boldsymbol{x}^{k}, \boldsymbol{g}^{k}$

* 要求 $y^k(\boldsymbol{x})$ 在点 $\boldsymbol{x}^k, \boldsymbol{x}^{k-1}$ 的 gradient 必须等于 $f(\boldsymbol{x})$ 在点 $\boldsymbol{x}^k, \boldsymbol{x}^{k-1}$ 的 gradient

  $y^k(\boldsymbol{x})$ 的 gradient 是

  $$\nabla y^k(\boldsymbol{x}) = \boldsymbol{g}^k + (B^k)^{-1} (\boldsymbol{x} - \boldsymbol{x}^k)$$

  * 对于点 $\boldsymbol{x}^k$ 这个要求天然就满足，因为 $\nabla y^k(\boldsymbol{x}^k) = \boldsymbol{g}^k$

  * 对于点 $\boldsymbol{x}^{k-1}$，该要求等价于 $\boldsymbol{g}^{k-1} = \boldsymbol{g}^k + (B^k)^{-1} (\boldsymbol{x}^{k-1} - \boldsymbol{x}^k)$

      定义 $\gamma^{k-1} = \boldsymbol{g}^k - \boldsymbol{g}^{k-1}, \delta^{k-1} = \boldsymbol{x}^k - \boldsymbol{x}^{k-1}$，则该条件等价于

      $$B^k \gamma^{k-1} = \delta^{k-1}$$

三种算法的区别就是如何构造 $B^k$，下面分别介绍这三种算法

#### Rank One Correction



