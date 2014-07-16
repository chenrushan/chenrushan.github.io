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

      这个公式又被称为 secant equation

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

所以三种算法的核心区别就是如何得到 $B^k$，计算 descent direction 用的都是 $\boldsymbol{d}^k = -B^k \boldsymbol{g}^k$，其余部分包括 line search 什么的也都一样，下面分别介绍这三种算法

<p style="background-color: #9f9">下面的介绍中我计算的是 $B^{k+1}$ 而不是 $B^k$，其本质没有任何区别，就是为了公式看上去能干净一些，如果用的是 $B^k$，则等号左边通常是一堆的 $k-1$ 上标，看上去有点乱</p>

#### Rank One Correction

这种算法使用下面的公式求得 $B^{k+1}$

$$B^{k+1} = B^{k} + a \boldsymbol{u}\boldsymbol{u}^T \;\; a \in \mathbb{R}, \boldsymbol{u} \in \mathbb{R}^n$$

可以看到它在 $B^{k}$ 的基础上加了一个 rank 为 1 的 matrix，所以叫 rank one correction。这其中 $B^{k}$ 是已知的，我们需要确定的是 $a$ 和 $\boldsymbol{u}$。

根据 secant equation

$$
\begin{align}
& (B^{k} + a \boldsymbol{u}\boldsymbol{u}^T) \gamma^{k} = \delta^{k} \\\\
\Longleftrightarrow & \; a \boldsymbol{u}\boldsymbol{u}^T \gamma^{k} = \delta^{k} - B^{k} \gamma^{k} \\\\
\Longleftrightarrow & \; a \boldsymbol{u}^T \gamma^{k} \boldsymbol{u} = \delta^{k} - B^{k} \gamma^{k} \;\; (\because \boldsymbol{u}^T \gamma^{k} \in \mathbb{R}) \\\\
\end{align}
$$

最后一个 equation 怎么解呢？Rank one correction 是这么做的，令 $a \boldsymbol{u}^T \gamma^{k} = 1$，则有

$$
\begin{align}
\boldsymbol{u} = & \delta^{k} - B^{k} \gamma^{k} \\\\
a = & \frac{1}{\boldsymbol{u}^T \gamma^{k}}
\end{align}
$$

这样计算 $B^{k+1}$ 的公式就是

$$B^{k+1} = B^k + \frac{(\delta^k - B^k\gamma^k)(\delta^k - B^k\gamma^k)^T}{(\delta^k - B^k\gamma^k)^T \gamma^k}$$

----------

下面分析一下 rank one correction

* 如果 $B^k$ 是 symmetric matrix，则 $B^{k+1}$ 一定是 symmetric matrix

* $B^{k+1}$ 满足 secant equation，因为我们就是用这个 equation 求出的 $B^{k+1}$

* $B^{k+1}$ 不一定 positive definite，易知如果 $B^k$ positive definite 且分母 $(\delta^k - B^k\gamma^k)^T \gamma^k > 0$，则 $B^{k+1}$ 也是 positive definite matrix (根据 positive definite 的定义即可证明)，但问题是 $(\delta^k - B^k\gamma^k)^T \gamma^k$ 没法保证 $> 0$，举个例子，考虑函数

  $$f(\boldsymbol{x}) = \frac{x\_1^4}{4} + \frac{x\_2^2}{2} - x\_1 x\_2 + x\_1 - x\_2$$

  给定初始点 $\boldsymbol{x}^0 = [0.59607, 0.59607]^T$，则

  $$H^0 = \begin{pmatrix} 0.94913 & 0.14318 \\\\ 0.14318 & 0.59702 \end{pmatrix}$$

  这里 $H^0$ positive definite，但是 $(\delta^0 - B^0\gamma^0)^T \gamma^0 = -0.03276 < 0$

  $$H^1 = \begin{pmatrix} 0.94481 & 0.23324 \\\\ 0.23324 & -1.2788 \end{pmatrix}$$

  可以验证 $H^1$ 并不是 positive definite matrix

  (例子来源于 An Introduction to Optimization [Edwin K. P. Chong, Stanislaw H. Zak])

  因此 $\boldsymbol{d}^{k+1}$ 并不能保证是 descent direction

* 如果 $(\delta^k - B^k\gamma^k)^T \gamma^k$ 接近于 $0$，则实际在计算 $B^{k+1}$ 可能会遇到问题

#### DFP Algorithm

DFP 是一个 rank two 的算法，最早由 Davidon 在 1959 年提出，后来 Fletcher 和 Powell 在 1963 年先后做了修改，所以算法取名为 DFP。DFP 计算 $B^{k+1}$ 的公式是

$$B^{k+1} = B^{k} + a \boldsymbol{u}\boldsymbol{u}^T + b \boldsymbol{v}\boldsymbol{v}^T\;\; a,b \in \mathbb{R}, \boldsymbol{u},\boldsymbol{v} \in \mathbb{R}^n$$

从公式可以看到，DFP 加了两个不同的 rank 为 1 的 matrix，比 rank one correction 多了一个。这里我们需要确定的变量有 4 个，分别是 $a, b, \boldsymbol{u}, \boldsymbol{v}$。另外，下面我就直接假设 $B^k$ 是 symmetric matrix。

根据 secant equation

$$
\begin{align}
& (B^{k} + a \boldsymbol{u}\boldsymbol{u}^T + b \boldsymbol{v}\boldsymbol{v}^T) \gamma^{k} = \delta^{k} \\\\
\Longleftrightarrow & \; a \boldsymbol{u}\boldsymbol{u}^T \gamma^{k} + b \boldsymbol{v}\boldsymbol{v}^T \gamma^{k} = \delta^{k} - B^{k} \gamma^{k} \\\\
\Longleftrightarrow & \; a \boldsymbol{u}^T \gamma^{k} \boldsymbol{u} + b \boldsymbol{v}^T \gamma^{k} \boldsymbol{v} = \delta^{k} - B^{k} \gamma^{k} \;\; (\because \boldsymbol{u}^T \gamma^{k}, \boldsymbol{v}^T \gamma^{k} \in \mathbb{R}) \\\\
\end{align}
$$

显然最后一个 equation 是有很多解的，DFP 是这么解的，令

$$
\begin{align}
\boldsymbol{u} = & \delta^{k} \\\\
\boldsymbol{v} = & - B^{k} \gamma^{k} \\\\
a \boldsymbol{u}^T \gamma^{k} = & 1 \\\\
b \boldsymbol{v}^T \gamma^{k} = & 1
\end{align}
$$

这样进一步可以求得 $a = \frac{1}{ {\delta^k}^T \gamma^k}, b = -\frac{1}{ {\gamma^k}^T B^k \gamma^k}$

因此计算 $B^{k+1}$ 的公式就是

$$B^{k+1} = B^k + \frac{ \delta^k {\delta^k}^T }{ {\delta^k}^T \gamma^k} - \frac{ B^k \gamma^k {\gamma^k}^T B^k }{ {\gamma^k}^T B^k \gamma^k}$$

----------

<blockquote>
在使用 exact line search 的情况下，如果 $B^k$ 是 symmetric positive definite matrix，则 $B^{k+1}$ 也是
</blockquote>

* 证明

  如果 $B^k$ 是 symmetric matrix，则 $B^{k+1}$ 显然也是，所以下面主要证明其 positive definitness

  * <p style="background-color: #9f9">首先证明 $B^{k+1}$ 是 positive semi-definite</p>

      给定任意 $\boldsymbol{v} \in \mathbb{R}^n \neq 0$

      $$
      \begin{align}
      \boldsymbol{v}^T B^{k+1} \boldsymbol{v} = & \boldsymbol{v}^T B^k \boldsymbol{v} + \frac{\boldsymbol{v}^T \delta^k {\delta^k}^T \boldsymbol{v}}{ {\delta^k}^T \gamma^k} - \frac{ \boldsymbol{v}^T B^k \gamma^k {\gamma^k}^T B^k \boldsymbol{v}}{ {\gamma^k}^T B^k \gamma^k} \\\\
      = & \boldsymbol{v}^T B^k \boldsymbol{v} + \frac{(\boldsymbol{v}^T \delta^k)^2}{ {\delta^k}^T \gamma^k} - \frac{ (\boldsymbol{v}^T B^k \gamma^k)^2}{ {\gamma^k}^T B^k \gamma^k}
      \end{align}
      $$

      由于 $B^k$ 是 symmetric positive definite matrix，所以可以另 $B^k = {B^k}^{1/2}{B^k}^{1/2}$，定义

      $$
      \begin{align}
      \boldsymbol{\eta} = & {B^k}^{1/2} \boldsymbol{v} \\\\
      \boldsymbol{\rho} = & {B^k}^{1/2} \gamma^k
      \end{align}
      $$

      则有

      $$
      \begin{align}
      \boldsymbol{v}^T B^{k+1} \boldsymbol{v} = & \boldsymbol{\eta}^T \boldsymbol{\eta} + \frac{(\boldsymbol{v}^T \delta^k)^2}{ {\delta^k}^T \gamma^k} - \frac{(\boldsymbol{\eta}^T \boldsymbol{\rho})^2}{\boldsymbol{\rho}^T \boldsymbol{\rho}} \\\\
      = & \frac{(\Vert \boldsymbol{\eta} \Vert \Vert \boldsymbol{\rho} \Vert)^2 - (\boldsymbol{\eta}^T \boldsymbol{\rho})^2}{\boldsymbol{\rho}^T \boldsymbol{\rho}} + \frac{(\boldsymbol{v}^T \delta^k)^2}{ {\delta^k}^T \gamma^k}
      \end{align}
      $$

      * 根据 Cauchy-Schwarz inequality $(\Vert \boldsymbol{\eta} \Vert \Vert \boldsymbol{\rho} \Vert)^2 - (\boldsymbol{\eta}^T \boldsymbol{\rho})^2 \geq 0$
      * $\boldsymbol{\rho}^T \boldsymbol{\rho} = {\gamma^k}^T B^k \gamma^k$，由于 $B^k$ 是 positive definite matrix，所以 $\boldsymbol{\rho}^T \boldsymbol{\rho} > 0$
      * ${(\boldsymbol{v}^T \delta^k)^2} \geq 0$
      * ${ {\delta^k}^T \gamma^k} = -(\alpha^k B^k \boldsymbol{g}^k)^T (\boldsymbol{g}^{k+1} - \boldsymbol{g}^k)$，由于使用 exact line search，根据 $\frac{\partial f(\boldsymbol{x}^k + \alpha^k \boldsymbol{d}^k)}{\partial \alpha^k} = 0$ 易推出 ${\boldsymbol{g}^k}^T B^k \boldsymbol{g}^{k+1} = 0$，所以 ${ {\delta^k}^T \gamma^k} = \alpha^k {\boldsymbol{g}^k}^T B^k \boldsymbol{g}^k > 0$

      综合上述条件 $\boldsymbol{v}^T B^{k+1} \boldsymbol{v} \geq 0$，所以 $B^{k+1}$ 是 positive semi-definite matrix

   * <p style="background-color: #9f9">接下来证明 $B^{k+1}$ 是 positive definite</p>

     这个主要是证明 $(\Vert \boldsymbol{\eta} \Vert \Vert \boldsymbol{\rho} \Vert)^2 - (\boldsymbol{\eta}^T \boldsymbol{\rho})^2$ 和 ${(\boldsymbol{v}^T \delta^k)^2}$ 不能同时为 0，假设二者同时为 0，则有 
     
     $$\boldsymbol{\eta} = \mu \boldsymbol{\rho}, \;\; \mu \in \mathbb{R}$$

     这个等价于 $\boldsymbol{v} = \mu \gamma^k$，又 $\boldsymbol{v}^T \delta^k = \mu {\gamma^k}^T \delta^k = 0$，这与前面 ${\gamma^k}^T \delta^k > 0$ 的结论矛盾

     所以 $(\Vert \boldsymbol{\eta} \Vert \Vert \boldsymbol{\rho} \Vert)^2 - (\boldsymbol{\eta}^T \boldsymbol{\rho})^2$ 和 ${(\boldsymbol{v}^T \delta^k)^2}$ 不能同时为 0，因此 $B^{k+1}$ 是 positive definite matrix
