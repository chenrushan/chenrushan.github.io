---
layout: post
title: 10 - Quasi Newton Method
categories: nnumop
tags: NPTEL, numerical optimization, quasi newton
---

### Quasi Newton Method

前一篇文章中提到了 Classical Newton 的诸多问题，针对这些问题有了 Quasi Newton Method，其基本思想是在每步迭代计算 descent direction 时不用公式 $\b{d}^k = -(H^k)^{-1} \b{g}^k$，而是用 $\b{d}^k = -B^k \b{g}^k$，也就是找到一个矩阵 $B^k$ 去近似 $(H^k)^{-1}$，相当于在 $\b{x}^k$ 处选择下面的近似函数

$$f(\b{x}) \approx y^k(\b{x}) = f(\b{x}^k) + {\b{g}^k}^T(\b{x} - \b{x}^k) + \frac{1}{2} (\b{x} - \b{x}^k)^T (B^k)^{-1} (\b{x} - \b{x}^k)$$

利用这一近似我们就将求解 linear system ($H^k \b{d}^k = -\b{g}^k$) 的操作转变为 matrix vector multiplication ($-B^k \b{g}^k$) 操作，计算量从 $O(N^3)$ 降到了 $O(N^2)$

那如何得到一个好的对 $(H^k)^{-1}$ 的近似矩阵呢？Quasi Newton 对 $B^k$ 做了如下约束

----------

* 要求 $B^k$ 是 symmetric matrix

* 要求 $B^k$ 是 positive definite matrix，保证每步迭代方向都是下降的

* 要求 $y^k(\b{x})$ 在点 $\b{x}^k, \b{x}^{k-1}$ 的 gradient 必须等于 $f(\b{x})$ 在点 $\b{x}^k, \b{x}^{k-1}$ 的 gradient，这其实就是要求 $y^k(\b{x})$ 要尽可能好得近似 $f(\b{x})$

    $y^k(\b{x})$ 的 gradient 是

    $$\nabla y^k(\b{x}) = \b{g}^k + (B^k)^{-1} (\b{x} - \b{x}^k)$$

    * 对于点 $\b{x}^k$ 这个要求天然就满足，因为 $\nabla y^k(\b{x}^k) = \b{g}^k$

    * 对于点 $\b{x}^{k-1}$，该要求等价于 $\b{g}^{k-1} = \b{g}^k + (B^k)^{-1} (\b{x}^{k-1} - \b{x}^k)$

        令 $\gamma^{k-1} = \b{g}^k - \b{g}^{k-1}, \delta^{k-1} = \b{x}^k - \b{x}^{k-1}$，则该条件等价于

        $$B^k \gamma^{k-1} = \delta^{k-1}$$

        这个公式又被称为 secant equation

----------

综合上述三个约束，生成 $B^k$ 的问题可以表示成

$$
\begin{align\*}
& \text{find } B^k \\\\
\text{s.t. } & B = B^T \\\\
& \det(\text{leading principal minors of } B) > 0 \\\\
& B^k \gamma^{k-1} = \delta^{k-1}
\end{align\*}
$$
 
$B^k$ 是一个 symmetric matrix，因此共包含 $\frac{n(n+1)}{2}$ 个变量，第二个对 leading principal minors 的约束对应 n 个不等式，最后一个约束对应 n 个等式，由于变量的个数多于等式和不等式的个数，所以上面的问题不止有一个解。根据对上述问题不同的解法，也就有了不同的 Quasi Newton Method，常见的包括如下 3 种

* Rank one correction
* DFP algorithm (<b>D</b>avidon, <b>F</b>letcher, <b>P</b>owell)
* BFGS algorithm (<b>B</b>royden, <b>F</b>letcher, <b>G</b>oldfarb, <b>S</b>hanno)

三种算法的核心区别就是如何得到 $B^k$，计算 descent direction 用的都是 $\b{d}^k = -B^k \b{g}^k$，其余包括 line search 什么的也都一样，下面分别介绍这三种算法

<blockquote>
下面的介绍中我计算的是 $B^{k+1}$ 而不是 $B^k$，其本质没有任何区别，就是为了公式看上去能干净一些，如果用的是 $B^k$，则等号左边通常是一堆的 $k-1$ 上标，看上去有点乱
</blockquote>

### Rank One Correction

这种算法使用下面的公式求得 $B^{k+1}$

$$B^{k+1} = B^{k} + a \b{u}\b{u}^T \;\; a \in \mathbb{R}, \b{u} \in \mathbb{R}^n$$

可以看到它在 $B^{k}$ 的基础上加了一个 rank 为 1 的 matrix，所以叫 rank one correction。这其中 $B^{k}$ 是已知的，我们需要确定的是 $a$ 和 $\b{u}$。

根据 secant equation

$$
\begin{align\*}
& (B^{k} + a \b{u}\b{u}^T) \gamma^{k} = \delta^{k} \\\\
\Longleftrightarrow & \; a \b{u}\b{u}^T \gamma^{k} = \delta^{k} - B^{k} \gamma^{k} \\\\
\Longleftrightarrow & \; a \b{u}^T \gamma^{k} \b{u} = \delta^{k} - B^{k} \gamma^{k} \;\; (\because \b{u}^T \gamma^{k} \in \mathbb{R}) \\\\
\end{align\*}
$$

为了解最后一个 equation，Rank one correction 这么做，令 $a \b{u}^T \gamma^{k} = 1$，则有

$$
\begin{align\*}
\b{u} = & \delta^{k} - B^{k} \gamma^{k} \\\\
a = & \frac{1}{\b{u}^T \gamma^{k}}
\end{align\*}
$$

这样计算 $B^{k+1}$ 的公式就是

$$B^{k+1} = B^k + \frac{(\delta^k - B^k\gamma^k)(\delta^k - B^k\gamma^k)^T}{(\delta^k - B^k\gamma^k)^T \gamma^k}$$

----------

下面分析一下 rank one correction

* 如果 $B^k$ 是 symmetric matrix，则 $B^{k+1}$ 一定是 symmetric matrix

* $B^{k+1}$ 满足 secant equation，因为我们就是用这个 equation 求出的 $B^{k+1}$

* $B^{k+1}$ 不一定 positive definite，易知如果 $B^k$ positive definite 且分母 $(\delta^k - B^k\gamma^k)^T \gamma^k > 0$，则 $B^{k+1}$ 也是 positive definite matrix (根据 positive definite 的定义即可证明)，但问题是 $(\delta^k - B^k\gamma^k)^T \gamma^k$ 没法保证 $> 0$，举个例子，考虑函数

    $$f(\b{x}) = \frac{x\_1^4}{4} + \frac{x\_2^2}{2} - x\_1 x\_2 + x\_1 - x\_2$$

    给定初始点 $\b{x}^0 = [0.59607, 0.59607]^T$，则

    $$H^0 = \begin{pmatrix} 0.94913 & 0.14318 \\\\ 0.14318 & 0.59702 \end{pmatrix}$$

    这里 $H^0$ positive definite，但是 $(\delta^0 - B^0\gamma^0)^T \gamma^0 = -0.03276 < 0$

    $$H^1 = \begin{pmatrix} 0.94481 & 0.23324 \\\\ 0.23324 & -1.2788 \end{pmatrix}$$

    可以验证 $H^1$ 并不是 positive definite matrix

    (例子来源于 An Introduction to Optimization [Edwin K. P. Chong, Stanislaw H. Zak])

    因此 $\b{d}^{k+1}$ 并不能保证是 descent direction

* 如果 $(\delta^k - B^k\gamma^k)^T \gamma^k$ 接近于 $0$，则实际在计算 $B^{k+1}$ 可能会遇到问题

### DFP Algorithm (Rank Two Correction)

DFP 是一个 rank two 的算法，最早由 Davidon 在 1959 年提出，后来 Fletcher 和 Powell 在 1963 年先后做了修改，所以算法取名为 DFP。DFP 计算 $B^{k+1}$ 的公式是

$$B^{k+1} = B^{k} + a \b{u}\b{u}^T + b \b{v}\b{v}^T\;\; a,b \in \mathbb{R}, \b{u},\b{v} \in \mathbb{R}^n$$

从公式可以看到，DFP 加了两个不同的 rank 为 1 的 matrix，比 rank one correction 多了一个。这里我们需要确定的变量有 4 个，分别是 $a, b, \b{u}, \b{v}$。另外，下面我就直接假设 $B^k$ 是 symmetric matrix。

根据 secant equation

$$
\begin{align\*}
& (B^{k} + a \b{u}\b{u}^T + b \b{v}\b{v}^T) \gamma^{k} = \delta^{k} \\\\
\Longleftrightarrow & \; a \b{u}\b{u}^T \gamma^{k} + b \b{v}\b{v}^T \gamma^{k} = \delta^{k} - B^{k} \gamma^{k} \\\\
\Longleftrightarrow & \; a \b{u}^T \gamma^{k} \b{u} + b \b{v}^T \gamma^{k} \b{v} = \delta^{k} - B^{k} \gamma^{k} \;\; (\because \b{u}^T \gamma^{k}, \b{v}^T \gamma^{k} \in \mathbb{R}) \\\\
\end{align\*}
$$

显然最后一个 equation 是有很多解的，DFP 是这么解的，令

$$
\begin{align\*}
\b{u} = & \delta^{k} \\\\
\b{v} = & - B^{k} \gamma^{k} \\\\
a \b{u}^T \gamma^{k} = & 1 \\\\
b \b{v}^T \gamma^{k} = & 1
\end{align\*}
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

        给定任意 $\b{v} \in \mathbb{R}^n \neq 0$

        $$
        \begin{align\*}
        \b{v}^T B^{k+1} \b{v} = & \b{v}^T B^k \b{v} + \frac{\b{v}^T \delta^k {\delta^k}^T \b{v}}{ {\delta^k}^T \gamma^k} - \frac{ \b{v}^T B^k \gamma^k {\gamma^k}^T B^k \b{v}}{ {\gamma^k}^T B^k \gamma^k} \\\\
        = & \b{v}^T B^k \b{v} + \frac{(\b{v}^T \delta^k)^2}{ {\delta^k}^T \gamma^k} - \frac{ (\b{v}^T B^k \gamma^k)^2}{ {\gamma^k}^T B^k \gamma^k}
        \end{align\*}
        $$

        由于 $B^k$ 是 symmetric positive definite matrix，所以可以另 $B^k = {B^k}^{1/2}{B^k}^{1/2}$，定义

        $$
        \begin{align\*}
        \boldsymbol{\eta} = & {B^k}^{1/2} \b{v} \\\\
        \boldsymbol{\rho} = & {B^k}^{1/2} \gamma^k
        \end{align\*}
        $$

        则有

        $$
        \begin{align\*}
        \b{v}^T B^{k+1} \b{v} = & \boldsymbol{\eta}^T \boldsymbol{\eta} + \frac{(\b{v}^T \delta^k)^2}{ {\delta^k}^T \gamma^k} - \frac{(\boldsymbol{\eta}^T \boldsymbol{\rho})^2}{\boldsymbol{\rho}^T \boldsymbol{\rho}} \\\\
        = & \frac{(\Vert \boldsymbol{\eta} \Vert \Vert \boldsymbol{\rho} \Vert)^2 - (\boldsymbol{\eta}^T \boldsymbol{\rho})^2}{\boldsymbol{\rho}^T \boldsymbol{\rho}} + \frac{(\b{v}^T \delta^k)^2}{ {\delta^k}^T \gamma^k}
        \end{align\*}
        $$

        * 根据 Cauchy-Schwarz inequality $(\Vert \boldsymbol{\eta} \Vert \Vert \boldsymbol{\rho} \Vert)^2 - (\boldsymbol{\eta}^T \boldsymbol{\rho})^2 \geq 0$
        * $\boldsymbol{\rho}^T \boldsymbol{\rho} = {\gamma^k}^T B^k \gamma^k$，由于 $B^k$ 是 positive definite matrix，所以 $\boldsymbol{\rho}^T \boldsymbol{\rho} > 0$
        * ${(\b{v}^T \delta^k)^2} \geq 0$
        * ${ {\delta^k}^T \gamma^k} = -(\alpha^k B^k \b{g}^k)^T (\b{g}^{k+1} - \b{g}^k)$，由于使用 exact line search，根据 $\frac{\partial f(\b{x}^k + \alpha^k \b{d}^k)}{\partial \alpha^k} = 0$ 易推出 ${\b{g}^k}^T B^k \b{g}^{k+1} = 0$，所以 ${ {\delta^k}^T \gamma^k} = \alpha^k {\b{g}^k}^T B^k \b{g}^k > 0$

        综合上述条件 $\b{v}^T B^{k+1} \b{v} \geq 0$，所以 $B^{k+1}$ 是 positive semi-definite matrix

    * <p style="background-color: #9f9">接下来证明 $B^{k+1}$ 是 positive definite</p>

        这个主要是证明 $(\Vert \boldsymbol{\eta} \Vert \Vert \boldsymbol{\rho} \Vert)^2 - (\boldsymbol{\eta}^T \boldsymbol{\rho})^2$ 和 ${(\b{v}^T \delta^k)^2}$ 不能同时为 0，假设二者同时为 0，则有 
        
        $$\boldsymbol{\eta} = \mu \boldsymbol{\rho}, \;\; \mu \in \mathbb{R}$$

        这个等价于 $\b{v} = \mu \gamma^k$，又 $\b{v}^T \delta^k = \mu {\gamma^k}^T \delta^k = 0$，这与前面 ${\gamma^k}^T \delta^k > 0$ 的结论矛盾

        所以 $(\Vert \boldsymbol{\eta} \Vert \Vert \boldsymbol{\rho} \Vert)^2 - (\boldsymbol{\eta}^T \boldsymbol{\rho})^2$ 和 ${(\b{v}^T \delta^k)^2}$ 不能同时为 0，因此 $B^{k+1}$ 是 positive definite matrix

### BFGS Algorithm

BFGS 分别由 Broyden, Fletcher, Goldfarb, Shanno 四人于 1970 年独立提出，它也用到了 rank two correction，但不是用在 $B^{k+1}$ 上，而是用在 $(B^{k+1})^{-1}$ 上，令 $G^{k+1} = (B^{k+1})^{-1}$，则有

$$G^{k+1} = G^{k} + a \b{u}\b{u}^T + b \b{v}\b{v}^T\;\; a,b \in \mathbb{R}, \b{u},\b{v} \in \mathbb{R}^n$$

由于 $B^{k+1} \gamma^{k} = \delta^{k}$，因此 $G^{k+1} \delta^{k} = \gamma^{k}$，运用在 DFP 一节中给出的解题步骤，可得

$$G^{k+1} = G^k + \frac{\gamma^k {\gamma^k}^T}{ {\gamma^k}^T \delta^k} - \frac{G^k \delta^k {\delta^k}^T G^k}{ {\delta^k}^T G^k \delta^k}$$

可以看出，它和 DFP 中 $B^{k+1}$ 的迭代公式形式是完全一样的，不同的是 $\delta^k$ 和 $\gamma^k$ 的角色做了互换

有了 $G^{k+1}$，$B^{k+1} = (G^{k+1})^{-1}$，这里有一个 inverse operation，由于 $G^{k+1}$ 有相对简单的形式，所以对它做 inverse 直接有 closed form solution，下面给出相关的 Sherman-Morrison-Woodbury formula

<blockquote>
Let $A$ be a nonsingular matrix. Let $\b{u}$ and $\b{v}$ be column vectors such that $1 + \b{v}^T A^{-1} \b{v} \neq 0$. Then $A + \b{u}\b{v}^T$ is nonsingular, and

$$ (A + \b{u}\b{v}^T)^{-1} = A^{-1} - \frac{(A^{-1} \b{u})(\b{v}^T A^{-1})}{1 + \b{v}^T A^{-1} \b{v}}$$
</blockquote>

连续两次在 $G^{k+1}$ 上应用这个公式可得

$$ B^{k+1} = B + (1 + \frac{\gamma^T B \gamma}{\delta^T \gamma}) \frac{\delta \delta^T}{\delta^T \gamma} - (\frac{\delta \gamma^T B + (\delta \gamma^T B)^T}{\delta^T \gamma}) $$

为了公式看上去简洁，对符合做了省略，其中 $B$ 就是 $B^k$，$\delta$ 就是 $\delta^k$，$\gamma$ 就是 $\gamma^k$

这个公式可以写成更简洁的形式

$$ 
\begin{align\*}
B^{k+1} = & \; {V^k}^T B^k V^k + \frac{\delta^k {\delta^k}^T}{ {\gamma^k}^T \delta^k} \\\\
\text{where} & \;\; V^k = I - \frac{\gamma^k {\delta^k}^T}{ {\gamma^k}^T \delta^k}
\end{align\*}
$$

根据与 DFP 一节中给出的证明相同的证明，可以得出 $G^{k+1}$ 在 exact line search 的情况下一定是 positive definite matrix，因此 $B^{k+1}$ 也一定是 positive definite matrix。Powell 在 Some global convergence properties of a variable metric algorithm for minimization without exact line searches 这篇文章中进一步证明了对于 convex function，BFGS + Wolfe line search 可以达到 global convergence

#### limited-memory BFGS (lBFGS)

BFGS 虽然是个高效的算法，但其每步迭代要存储一个矩阵 $B^k$，对于参数规模较大的函数，这个空间上的消耗显然是不可接受的，也因此有了所谓的 limited-memory BFGS，其与 BFGS 的区别主要是以下两点

* lBFGS 每步迭代并不存储矩阵，而是存储前 $m$ 步迭代的 $\gamma$ 和 $\delta$

* 为了完全避免掉存任何矩阵相关的信息，lBFGS 直接计算 $B^k \b{g}^k$，而不是先得到 $B^k$ 然后再和 $\b{g}^k$ 做 matrix vector multiplication，这样做能让每步迭代只涉及 vector operation，如 inner product, addition 等，下面我们会看到为什么 $B^k \b{g}^k$ 只包含 vector operation

根据上面给出的公式

$$B^{k} = {V^{k-1}}^T B^{k-1} V^{k-1} + \frac{\delta^{k-1} {\delta^{k-1}}^T}{ {\gamma^{k-1}}^T \delta^{k-1}}$$

这是个递归公式，展开 $m$ 步可得 (方便起见，定义 $\rho^k = \frac{1}{ {\gamma^{k}}^T \delta^{k}}, \rho^k \in \mathbb{R}$)

$$
\begin{align\*}
B^{k} = & {V^{k-1}}^T B^{k-1} V^{k-1} + \rho^{k-1} {\delta^{k-1} {\delta^{k-1}}^T} \\\\
= & {V^{k-1}}^T {V^{k-2}}^T B^{k-2} V^{k-2} V^{k-1} + \rho^{k-2} {V^{k-1}}^T \delta^{k-2} {\delta^{k-2}}^T V^{k-1} + \rho^{k-1} {\delta^{k-1} {\delta^{k-1}}^T} \\\\
= & \cdots \\\\
= & ({V^{k-1}}^T \cdots {V^{k-m}}^T) B^{k-m} ({V^{k-m}} \cdots V^{k-1}) + \\\\
  & \rho^{k-m} ({V^{k-1}}^T \cdots {V^{k-m+1}}^T) \delta^{k-m} {\delta^{k-m}}^T (V^{k-m+1} \cdots V^{k-1}) + \\\\
  & \cdots \;+ \\\\
  & \rho^{k-1} {\delta^{k-1} {\delta^{k-1}}^T}
\end{align\*}
$$

最后一个式子中除了 $B^{k-m}$ 以外，其余的所有变量都能以 $\gamma$ 和 $\delta$ 表示。为了让 $B^k$ 能完全由前 $m$ 步的 $\gamma$ 和 $\delta$ 计算出来，lBFGS 在每一步迭代都选择一个矩阵去替换 $B^{k-m}$，这个矩阵每步都可以是不同的，但通常都是形式相对简单的矩阵，比如 diagonal matrix。令第 k 步选择的矩阵为 $B\_0^k$，这样每步迭代中 lBFGS 计算

$$
\begin{align\*}
B^{k}\b{g}^k = & ({V^{k-1}}^T \cdots {V^{k-m}}^T) B\_0^k ({V^{k-m}} \cdots V^{k-1})\b{g}^k + \\\\
  & \rho^{k-m} ({V^{k-1}}^T \cdots {V^{k-m+1}}^T) \delta^{k-m} {\delta^{k-m}}^T (V^{k-m+1} \cdots V^{k-1}) \b{g}^k + \\\\
  & \rho^{k-m+1} ({V^{k-1}}^T \cdots {V^{k-m+2}}^T) \delta^{k-m+1} {\delta^{k-m+1}}^T (V^{k-m+2} \cdots V^{k-1}) \b{g}^k + \\\\
  & \cdots \;+ \\\\
  & \rho^{k-1} {\delta^{k-1} {\delta^{k-1}}^T}\b{g}^k
\end{align\*}
$$

----------

下面我们看看怎么实现这个公式使得它可以(几乎)完全由 vector operation 来完成

* 首先定义两个变量

    $$
    \begin{align\*}
    \eta\_i = & (V^{k-i} V^{k-i+1} \cdots V^{k-1}) \b{g}^k\\\\
    \xi\_i = & \rho^{k-i} {\delta^{k-i}}^T (V^{k-i+1} \cdots V^{k-1}) \b{g}^k \\\\
    \end{align\*}
    $$
    
    其中 $\eta\_i \in \mathbb{R}^n, \xi\_i \in \mathbb{R}$ 由此可得
    
    $$
    \begin{align\*}
    \xi\_i = & \rho^{k-i} {\delta^{k-i}}^T \eta\_{i-1} \\\\
    \eta\_i = & V^{k-i} \eta\_{i-1} = (I - \rho^{k-i} \gamma^{k-i} {\delta^{k-i}}^T) \eta\_{i-1} = \eta\_{i-1} - \xi\_{i} \gamma^{k-i}
    \end{align\*}
    $$
    
    可以看出 $\xi\_i$ 和 $\eta\_i$ 的计算都只涉及 vector operation
  
* 有了上面两个变量 $B^k\b{g}^k$ 可以表示为

    $$
    \begin{align\*}
    B^{k}\b{g}^k = & ({V^{k-1}}^T \cdots {V^{k-m}}^T) B\_0^k \eta\_m + \\\\
      & ({V^{k-1}}^T \cdots {V^{k-m+1}}^T) \delta^{k-m} \xi\_m + \\\\
      & ({V^{k-1}}^T \cdots {V^{k-m+2}}^T) \delta^{k-m+1} \xi\_{m-1} + \\\\
      & \cdots \;+ \\\\
      & \delta^{k-1} \xi\_1
    \end{align\*}
    $$
    
    这个公式可以进一步以递归的形式表示，举个例子，假设 $m = 3$，则有
    
    $$
    \begin{align\*}
    B^{k}\b{g}^k = & {V^{k-1}}^T ({V^{k-2}}^T ({V^{k-3}}^T B\_0^k \eta\_3 + \delta^{k-3} \xi\_3) + \delta^{k-2} \xi\_2) + \delta^{k-1} \xi\_1
    \end{align\*}
    $$
    
    根据这个观察定义如下变量
    
    $$ \zeta\_i = \left\\{ \begin{array}{ll} B\_0^k\eta\_m & i = m + 1 \\\\ {V^{k-i}}^T \zeta\_{i+1} + \delta^{k-i} \xi\_i & i \in [1, m] \end{array} \right.$$
    
    $\zeta\_i \in \mathbb{R}^n$，可以看出 $\zeta\_1$ 就是我们要的 $B^k \b{g}^k$，具体分析一下这个分段函数
    
    * $i = m + 1$ 部分涉及一个 matrix vector multiplication，但由于通常 $B\_0^k$ 是形式较为简单的 matrix，比如 diagonal matrix，所以 $B\_0^k \b{g}^k$ 的计算量比较小，对于 diagonal matrix，这里计算量为 $O(n)$
    
    * 对于 $i \in [1, m]$ 部分，展开可得
    
        $$
        \begin{align\*}
        \zeta\_i = & {V^{k-i}}^T \zeta\_{i+1} + \delta^{k-i} \xi\_i \\\\
        = & (I - \rho^{k-i}\delta^{k-i} {\gamma^{k-i}}^T) \zeta\_{i+1} + \delta^{k-i} \xi\_i \\\\
        = & \zeta\_{i+1} + \delta^{k-i} (\xi\_i - \rho^{k-i}({\gamma^{k-i}}^T\zeta\_{i+1})) \\\\
        \end{align\*}
        $$
    
        这里面涉及的 vector operation 包括 inner product, subtraction 等

----------

根据前面定义的 $\eta, \xi, \zeta$ 可以得出如下计算 $B^k \b{g}^k$ 的伪代码

    $\eta_0 = \b{g}^k$
    for $i$ from $1$ to $m$
      $\xi_i = \rho^{k-i} {\delta^{k-i}}^T \eta_{i-1}$
      $\eta_i = \eta_{i-1} - \xi_{i} \gamma^{k-i}$

    $\zeta_{m+1} = B_0^k\eta_m$
    for $i$ from $m$ to $1$
      $\zeta_{i} = \zeta_{i+1} + \delta^{k-i} (\xi_i - \rho^{k-i}({\gamma^{k-i}}^T\zeta_{i+1}))$

    output $\zeta_1$

这是一个 $O(mn)$ 的算法。lBFGS 每轮迭代都运行上述代码得到 descent direction，并且如果 $k > m$ 还需要 update 保存 $\gamma, \delta$ 的队列，去掉最后一个，加入最新的一个，然后继续下一轮迭代，直至算法收敛

关于 $B\_0^k$ 选择，一种被证明比较有效的方法是令 $B\_0^k = \frac{ {\delta^{k-1}}^T \gamma^{k-1}}{ {\gamma^{k-1}}^T \gamma^{k-1}} I$

### 总结

一些关于 Quasi-Newton method 的理论分析这篇文章中并没有给出，下面给出一些有用的结论

* Quasi-Newton 通常是 superlinear convergent algorithm
* BFGS (lBFGS) 是目前实践中最好用的 Quasi-Newton method，它对 line search 的精确度的要求相对不那么高

