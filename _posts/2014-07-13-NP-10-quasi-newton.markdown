---
layout: post
title: 10 - Quasi Newton Method
categories: nnumop
tags: NPTEL, numerical optimization, quasi newton
---

#### Quasi Newton Method

前一篇文章中提到了 Classical Newton 的诸多问题，针对这些问题有了 Quasi Newton Method，其基本思想是在每步迭代得到 descent direction 的时候并不计算 $\boldsymbol{d}^k = -(H^k)^{-1} \boldsymbol{g}^k$，而是计算 $\boldsymbol{d}^k = -B^k \boldsymbol{g}^k$，也就是在每步迭代时找到一个矩阵 $B^k$ 去近似 $(H^k)^{-1}$，这样迭代的近似函数就变为

$$f(\boldsymbol{x}) \approx y^k(\boldsymbol{x}) = f(\boldsymbol{x}^k) + {\boldsymbol{g}^k}^T(\boldsymbol{x} - \boldsymbol{x}^k) + \frac{1}{2} (\boldsymbol{x} - \boldsymbol{x}^k)^T (B^k)^{-1} (\boldsymbol{x} - \boldsymbol{x}^k)$$

利用这一近似我们就将求解 linear system 的操作转变为 matrix vector multiplication 操作，计算量大大下降

那如何得到一个比较好的对 $(H^k)^{-1}$ 近似的矩阵呢？Quasi Newton 对 $B^k$ 做了如下约束

----------

* 要求 $B^k$ 是 symmetric matrix

* 要求 $B^k$ 是 positive definite matrix，这样保证每步迭代方向都是下降的

* 要求 $y^k(\boldsymbol{x})$ 在点 $\boldsymbol{x}^k, \boldsymbol{x}^{k-1}$ 的 gradient 必须等于 $f(\boldsymbol{x})$ 在点 $\boldsymbol{x}^k, \boldsymbol{x}^{k-1}$ 的 gradient，这其实就是要求 $y^k(\boldsymbol{x})$ 要尽可能好得近似 $f(\boldsymbol{x})$

  $y^k(\boldsymbol{x})$ 的 gradient 是

  $$\nabla y^k(\boldsymbol{x}) = \boldsymbol{g}^k + (B^k)^{-1} (\boldsymbol{x} - \boldsymbol{x}^k)$$

  * 对于点 $\boldsymbol{x}^k$ 这个要求天然就满足，因为 $\nabla y^k(\boldsymbol{x}^k) = \boldsymbol{g}^k$

  * 对于点 $\boldsymbol{x}^{k-1}$，该要求等价于 $\boldsymbol{g}^{k-1} = \boldsymbol{g}^k + (B^k)^{-1} (\boldsymbol{x}^{k-1} - \boldsymbol{x}^k)$

      定义 $\gamma^{k-1} = \boldsymbol{g}^k - \boldsymbol{g}^{k-1}, \delta^{k-1} = \boldsymbol{x}^k - \boldsymbol{x}^{k-1}$，则该条件等价于

      $$B^k \gamma^{k-1} = \delta^{k-1}$$

----------

综合上述三个约束，生成 $B^k$ 的问题可以表示成

$$
\begin{align}
& \text{find } B^k \\\\
\text{s.t. } & B = B^T \\\\
& \det(\text{leading principal minors of } B) > 0 \\\\
& B^k \gamma^{k-1} = \delta^{k-1}
\end{align}
$$
 
$B^k$ 是一个 symmetric matrix，因此共包含 $\frac{n(n+1)}{2}$ 个变量，第二个对 leading principal minors 的约束对应 n 个不等式，最后一个约束对应 n 个等式，由于变量的个数多于等式和不等式的个数，所以上面的问题不止有一个解。根据对上述问题不同的解法，也就有了不同的 Quasi Newton Method，常见的包括如下 3 种

* Rank one correction
* DFP algorithm (<b>D</b>avidon, <b>F</b>letcher, <b>P</b>owell)
* BFGS algorithm (<b>B</b>royden, <b>F</b>letcher, <b>G</b>oldfarb, <b>S</b>hanno)

下面分别介绍这三种算法

#### Rank One Correction


