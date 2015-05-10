---
layout: post
title: Mathmatical Background in Detail
categories: numop
tags: NPTEL, numerical optimization
---

这篇笔记给出 [Mathmatical Background](/nnumop/2014/03/21/NP-02-mathback/)
中一些重要结论的证明

---

<a name="orthcolumn"></a>
<blockquote>
<p>对于一个 squre matrix $Q$</p>
<ul>
<li>$Q$ 的 column vector 是 orthogonal 不能推出 $Q$ 的 row vector 是 orthogonal 的</li>
<li>$Q$ 的 column vector 是 orthonormal 等价于 $Q$ 的 row vetor 是 orthonormal 的</li>
</ul>
</blockquote>

* Proof

    对于第一个结论可以举反例证明，比如

    $$Q = \begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 0 & 1 \\\\ 1 & 0 & 0 \end{pmatrix}$$

    其中第二列 $0$ 向量与任何向量都是 orthogonal 的，所以 column 之间是
    orthogonal 的，但 row 之间显然不是

    对于第二个结论，如果 $Q$ 的 column 是 orthonormal，则有 $Q^T Q = I$，
    由于 $Q$ 是 square matrix，所以有 $QQ^T = I$ (这个结论在后面有证明)，即
    $(Q^T)^T(Q^T) = I$，所以 $Q^T$ 的 column 是 orthonormal 的，这等价于 $Q$
    的 row 是 orthonormal 的 $\EOP$

<a name="detAB"></a>
<blockquote>
$\det(AB) = \det(A)\det(B)$
</blockquote>

* Proof

    Take $2\times 2$ matrix as example, $A = [\b{a}\_1, \b{a}\_2], B = [\b{b}\_1, \b{b}\_2]$.
    ($a\_{ij}$ means element at **column i, row j**, not row i column j as usual).

    $$
    \begin{align\*}
    \det(AB) = & \det[\b{a}\_1, \b{a}\_2]\times [\b{b}\_1, \b{b}\_2] \\\\
    = & \det[b\_{11}\b{a}\_1 + b\_{12}\b{a}\_2, b\_{21}\b{a}\_1 + b\_{22}\b{a}\_2] \\\\
    = & b\_{11}\det[\b{a}\_1, b\_{21}\b{a}\_1 + b\_{22}\b{a}\_2] + b\_{12}
        \det[\b{a}\_2, b\_{21}\b{a}\_1 + b\_{22}\b{a}\_2] \\\\
    = & c\_1\det[\b{a}\_1, \b{a}\_1] + c\_2\det[\b{a}\_1, \b{a}\_2] + c\_3
        \det[\b{a}\_2, \b{a}\_1] + c\_4\det[\b{a}\_2, \b{a}\_2]
    \end{align\*}
    $$

    Here, the exact form of $c\_{i}$ doesn't matter, anyway they are some function
    of $b\_{ij}$.

    There are 4 terms in the last formula, among them, $\det[\b{a}\_1, \b{a}\_1],
    \det[\b{a}\_2, \b{a}\_2]$ are equal to 0, $\det[\b{a}\_2, \b{a}\_1] =
    -\det[\b{a}\_1, \b{a}\_2]$, so $\det(AB)$ can be further reduced to

    $$\det(AB) = c\det(A)$$

    Let $A = I$, we have $\det(B) = c\det(I) = c$, so $\det(AB) = \det(A)\det(B)$.

    The above reasoning can be easily extended to $n\times n$ matrix. $\EOP$

<a name="creqrr"></a>
<blockquote>
Given any $m \times n$ matrix $A$, its column rank always equals its row rank
</blockquote>

* Proof

    我们知道给定任何一个 $m\times n$ matrix $A$，我们都可以通过 row elementrary
    operation 和 column elementrary operation 将 $A$ 转变为
    $\begin{pmatrix} I\_r & 0 \\\\ 0 & 0 \end{pmatrix}$，这些操作可以以 matrix
    multiplication 的方式来表示，以 $E^r$ 表示 row elementrary operation，$E^c$
    表示 column elementrary operation，则有

    $$
    E^r\_k\cdots E^r\_1 A E^c\_1 \cdots E^c\_l =
    \begin{pmatrix} I\_r & 0 \\\\ 0 & 0 \end{pmatrix}
    $$

    易知 $\begin{pmatrix} I\_r & 0 \\\\ 0 & 0 \end{pmatrix}$ 的 column rank =
    row rank = $r$，因此我们只要证明 $E^r$ 和 $E^c$ 不改变 $A$ 的 column rank
    和 row rank 即可，下面只给出 $E^r$ 相关的证明，$E^c$ 相关的证明类似。为方便
    起见，令 $A' = E^r A$

    <p style="background-color: #9f9">首先证明 $A'$ 和 $A$ 的 column rank
    是相等的</p>
    
    以 $C\_i$ 表示 $A$ 的 column，$C'\_i$ 表示 $A'$ 的 column，易知
    $C'\_i = E^r C\_i$
    
    给定任何一个 $C\_i$ 的组合 $C\_{i\_1}, \cdots, C\_{i\_h}$，如果存在非零系数
    $\a\_1, \cdots, \a\_h (\a\_i\in\mathbb{R})$ 使得
    $\sum\_{j=1}^{h} \a\_j C\_{i\_j} = 0$，则有

    $$
    \sum\_{j=1}^{h} \a\_j C\_{i\_j} = 0 \Ra
    \sum\_{j=1}^{h} \a\_j E^r C\_{i\_j} = 0 \Ra
    \sum\_{j=1}^{h} \a\_j C'\_{i\_j} = 0
    $$

    换句话说，如果 $C\_{i\_1}, \cdots, C\_{i\_h}$ linear dependent，则
    $C'\_{i\_1}, \cdots, C'\_{i\_h}$ 也必然 linear dependent，这个结论等价于如果
    $C'\_{i\_1}, \cdots, C'\_{i\_h}$ linear independent，则
    $C\_{i\_1}, \cdots, C\_{i\_h}$ 也必然 linear independent (就是离散数学里学
    的 $A \Ra B \Leftrightarrow \neg B \Ra \neg A$)。这样我们就有

    $$\text{column_rank}(A') \leq \text{column_rank}(A)$$

    由于 $E^r$ 是可逆的，所以 $A$ 可以表示为 $(E^r)^{-1}A'$，根据上面同样的论述
    可知

    $$\text{column_rank}(A) \leq \text{column_rank}(A')$$

    因此有 $\text{column_rank}(A) = \text{column_rank}(A')$

    <p style="background-color: #9f9">接下来证明 $A'$ 和 $A$ 的 row rank
    是相等的</p>

    以 $R\_i$ 表示 $A$ 的 row，$R'\_i$ 表示 $A'$ 的 row

    由于总共有 3 种 row elementrary operation，这里只考虑一种，即 row
    addition 操作，其他两种类似，假设 $E^r$ 改变的是第 $j$ 行，即 $R'\_j =
    R\_j + \beta R\_k$，易知 $E^r$ 并没有改变行与行之间的线性关系，也就是说，
    如果存在非零 $\a\_1, \cdots, \a\_h$ 使得 $\sum\_{j=1}^{h} \a\_j R\_{i\_j}
    = 0$，则必有 $\sum\_{j=1}^{h} \a\_j R'\_{i\_j} = 0$，根据证明 column rank
    过程中的相同的论述，可知

    $$\text{row_rank}(A') \leq \text{row_rank}(A)$$

    同样由于 $E^r$ 是可逆的，我们可以推出

    $$\text{row_rank}(A) \leq \text{row_rank}(A')$$

    因此有

    $$\text{row_rank}(A) = \text{row_rank}(A')$$

    综上所述，row elementrary operation 并不会改变 $A$ 的 row rank 和 column
    rank，同样，column elementrary operation 也不会改变 $A$ 的 row rank 和
    column rank，因此 $A$ 的 column rank 和 row rank 都等于 $I\_r$ 的 row rank
    和 column rank，即 $r$ $\EOP$

<a name="ABBA"></a>
<blockquote>
If $A, B$ are square matrices, then $AB = I \Ra BA = I$
</blockquote>

* Proof

    假设 $A, B$ 都是 $n\times n$ matrix。等式两边同乘以 $B$，有

    $$B = BAB = (BA)B \Ra (I - BA)B = 0$$

    如果能证明 $B$ 是个 rank 为 n 的矩阵，则能推出 $I - BA = 0$，即 $BA = I$

    为证明 $B$ rank 为 n，只需要证明 $B$ 的 column 是 linear independent 的
    (当然也可以证明 row 是 linear independent，二者等价)

    令 $\\{e\_i\\}\_{i = 1 \cdots n}$ 表示 $I$ 的每一列，则 $B$ 的每一列可以表示
    为 $\\{Be\_i\\}$，假设 $\\{a\_i, a\_i \in \mathbb{R}\\}$ 满足

    $$\sum\_i a\_i Be\_i = 0$$

    两边同乘以 $A$ 有

    $$\sum\_i a\_i ABe\_i = 0 \Ra \sum\_i a\_i e\_i = 0$$
    
    由于 $e\_i$ linear independent，因此 $a\_i = 0 \; \forall i$，也就是说
    B 的 column 之间是 linear independent 的，这样也就推出了 $I - BA = 0$ $\EOP$

<a name="symreal"></a>
<blockquote>
A symmetric matrix $A \in \mathbb{R}^{n\times n}$ has $n$ real eigenvalues
</blockquote>

* Proof

    (关于复数的知识可以参考
    [1](http://betterexplained.com/articles/a-visual-intuitive-guide-to-imaginary-numbers/) 和
    [2](http://betterexplained.com/articles/intuitive-arithmetic-with-complex-numbers/))

    假设 $A$ 存在复数的 eigenvalue $\lambda$，由于 $A\b{x} = \lambda \b{x}$ 且
    $A$ 中每个元素都是实数，所以 $\b{x}$ 中必然存在一个或多个复数

    记 $\b{x}$ 的共轭为 $\bar{\b{x}}$，对 $A\b{x} = \lambda \b{x}$
    两边取共轭，有 $\overline{A \b{x}} = \overline{\lambda \b{x}} \Ra
    A\bar{\b{x}} = \bar{\lambda}\bar{\b{x}}$，对前一个等式两边统乘以
    $\bar{\b{x}}^T$，后一个等式两边统乘以 $\b{x}^T$，可得

    $$
    \begin{cases}
    \bar{\b{x}}^T A\b{x} = \lambda \bar{\b{x}}^T \b{x} \\\\
    \b{x}^T A \bar{\b{x}} = \bar{\lambda} \b{x}^T \bar{\b{x}}
    \end{cases}
    $$

    两个等式相减，可得

    $$
    \bar{\b{x}}^T A\b{x} - \b{x}^T A \bar{\b{x}} =
    (\lambda - \bar{\lambda}) \bar{\b{x}}^T \b{x}
    $$

    由于 $A$ 是 symmetric matrix，所以左边两项相等(很容易验证，对于一个
    symmetric matrix, $\b{x}^T A\b{y} = \b{y}^T A\b{x}$)，也就是
    $(\lambda - \bar{\lambda}) \bar{\b{x}}^T \b{x} = 0$，而对于非零向量
    $\bar{\b{x}}^T \b{x}$ 不可能为 0，因此 $\lambda = \bar{\lambda}$，而满足
    这一等式的 $\lambda$ 只能是实数 $\EOP$

<a name="symorth"></a>
<blockquote>
For symmetric matrix, the eigenvectors of different eigenvalues are orthogonal
</blockquote>

* Proof

    $$
    \begin{align\*}
    & (A \b{x}\_i)^T \b{x}\_j = \b{x}\_i^T A^T \b{x}\_j = \b{x}\_i^T A \b{x}\_j \\\\
    \Rightarrow & \lambda\_i \b{x}\_i^T \b{x}\_j = \b{x}\_i^T \lambda\_j \b{x}\_j =
                  \lambda\_j \b{x}\_i^T \b{x}\_j \\\\
    \Rightarrow & \b{x}\_i^T \b{x}\_j = 0
    \end{align\*}
    $$

<a name="symmulti"></a>
<blockquote>
If $\lambda_i$ is a repeated root with multiplicity m >= 2, then there exist
m orthonormal eigenvectors corresponding to $\lambda_i$
</blockquote>

* Proof

    下面假设 matrix 的维度为 $n\times n$

    首先一个 eigenvalue 必对应至少一个 eigenvector，假设 $\lambda\_i$ 的
    multiplicity 为 $m$，下面我们证明当 $m \geq 2$ 时，$\lambda\_i$ 至少对应 2
    个 eigenvector

    由于一个 eigenvalue 必对应至少一个 eigenvector，假设 $\b{x}\_i$ 为
    $\lambda\_i$ 对应的 eigenvector，且 $\Vert \b{x}\_i \Vert = 1$
    (这个很容易实现，如果长度不为 1，就做个归一化好了)，现在基于 $\b{x}\_i$
    构建一个 orthonormal basis $P = (\b{x}\_i, \b{u}\_1, \cdots, \b{u}\_{n-1})$
    (给定任意一个向量，我们都可以很容易找到另外 $n-1$ 个向量与之构成一个 basis，
    然后利用 Gram-Schmidt Procedure 就可以得到一个 orthonormal basis)。为方便起见，
    记 $U = (\b{u}\_1, \cdots, \b{u}\_{n-1}), P = (\b{x}\_i, U)$，则

    $$
    \begin{align\*}
    P^T AP = & \begin{pmatrix} \b{x}\_i^T \\\\ U^T \end{pmatrix} A (\b{x}\_i, U)
    = \begin{pmatrix} \b{x}\_i^T A \b{x}\_i & \b{x}\_i^T A U \\\\
      U^T A \b{x}\_i & U^T AU \end{pmatrix} \\\\
    = & \begin{pmatrix} \b{x}\_i^T A \b{x}\_i & \b{0} \\\\ \b{0} & U^T AU \end{pmatrix}
    = \begin{pmatrix} \lambda\_i & \b{0} \\\\ \b{0} & U^T AU \end{pmatrix}
    \end{align\*}
    $$

    记 $Q = U^T AU$，$Q$ 为 $(n-1)\times(n-1)$ matrix，基于上面的等式有

    $$\det(P^T AP - \lambda I) = (\lambda\_i - \lambda) \det(Q - \lambda I\_{n-1})$$

    由于 $P^T AP$ 和 $A$ 是 similar matrix，所以二者的 eigenvalue 是相同的，
    因此对于 $P^T AP$，$\lambda\_i$ 的 multiplicity 也是 $m$，这样
    $\det(P^T AP - \lambda I)$ 的展开式中必包含 $m$ 项 $\lambda - \lambda\_i$，
    由于 $m \geq 2$，这意味着 $\det(Q - \lambda I\_{n-1})$ 中也包含至少一项
    $\lambda - \lambda\_i$，这说明 $\lambda\_i$ 也是 $Q$ 的 eigenvalue，假设其
    对应的 eigenvector 为 $\b{y}\_i$，则有

    $$
    P^T AP \begin{pmatrix} 1 \\\\ \b{y}\_i \end{pmatrix} = 
    \begin{pmatrix} \lambda\_i & \b{0} \\\\ \b{0} & Q \end{pmatrix}
    \begin{pmatrix} 1 \\\\ \b{y}\_i \end{pmatrix} =
    \lambda\_i \begin{pmatrix} 1 \\\\ \b{y}\_i \end{pmatrix}
    $$

    上式两边统乘以 $P$，有

    $$
    A(P \begin{pmatrix} 1 \\\\ \b{y}\_i \end{pmatrix}) = 
    \lambda\_i (P\begin{pmatrix} 1 \\\\ \b{y}\_i \end{pmatrix})
    $$

    也就是说 $P\begin{pmatrix} 1 \\\\ \b{y}\_i \end{pmatrix}$ 为 $A$ 对应于
    $\lambda\_i$ 的 eigenvector，这个向量和 $\b{x}\_i$ 是 linear independent
    的 (否则可以推出 $\b{x}\_i, \b{u}\_1, \cdots, \b{u}\_{n-1}$ 之间是 linear
    dependent 的，而前面我们已经说了 $\b{x}\_i, \b{u}\_1, \cdots, \b{u}\_{n-1}$
    是 linear independent 的)，这样我们就找到了 $A$ 的另一个 eigenvector，证明了
    当 $m \geq 2$ 时，$\lambda\_i$ 至少对应 2 个 linear independent eigenvector

    基于上述相同的过程，我们可以证明当 $m \geq 3$ 时，$\lambda\_i$ 至少有 3 个
    linear independent eigenvector，只需令 $P = (\b{x}\_{i\_1}, \b{x}\_{i\_2},
    \b{u}\_1, \cdots, \b{u}\_{n-2})$ 即可，其中 $\b{x}\_{i\_1}, \b{x}\_{i\_2}$
    为 $\lambda\_i$ 已知的必然存在的两个 linear independent eigenvector。
    以此类推，当 $m \geq k$ 时，$\lambda\_i$ 至少有 $k$ 个 linear independent
    eigenvector

    最后，显然 $\lambda\_i$ 不可能有超过 $m$ 个的 eigenvector，否则所有
    eigenvalue 对应的 eigenvector 个数要超过 $n$ 了，因此，multiplicity
    为 $m$ 的 eigenvalue，必然对应 m 个 linear independent 的 eigenvector $\EOP$

<a name="posdefeigen"></a>
<blockquote>
$A$ is positive definite iff all its eigenvalues are positive
</blockquote>

* Proof

    * eigenvalues are positive $\Rightarrow$ $A$ is positive definite

        $$
        \begin{align\*}
        \b{x}^T A \b{x} = & \b{x}^T S \Lambda S^T \b{x} \\\\
        = & \b{y}^T \Lambda \b{y} \\\\
        = & \sum\_i \lambda\_i y\_i^2
        \end{align\*}
        $$

        So if $\lambda\_i \gt 0 \;\; \forall i$, $\b{x}^T A \b{x} \gt 0$.

    * $A$ is positive definite $\Rightarrow$ eigenvalues are positive

        Let $\b{x}\_i$ be eigenvector

        $$
        \begin{align\*}
        & A \text{ is positive definite} \\\\
        \Rightarrow & \b{x}\_i^T A \b{x}\_i \gt 0 \\\\
        \Rightarrow & \b{x}\_i^T \lambda\_i \b{x}\_i \gt 0 \\\\
        \Rightarrow & \lambda\_i \gt 0\EOP
        \end{align\*}
        $$

<a name="gradper"></a>
<blockquote>
Gradient is perpenticular to level surface (contour line)
</blockquote>

证明前简单回顾一下空间曲线的方程

空间曲线可以用如下方程表示(按高数书中以3维空间为例)

$$
\begin{cases} x = x(t) \\\\ y = y(t) \\\\ z = z(t) \end{cases} \;\;\; t \in (\a, \beta)
$$

空间曲面可以用如下方程表示

$$
\begin{cases} x = x(s, t) \\\\ y = y(s, t) \\\\ z = z(s, t) \end{cases} \;\;\;
s \in (a, b), t \in (\a, \beta)
$$

这个可以从“点，线，面”的关系来理解，对于曲线方程，如果固定 $t = t\_0$，我们就
得到了一个点 $(x(t\_0), y(t\_0), z(t\_0))$，因此连续变化的 $t$ 就构成了一个
曲线。对于曲面方程，固定 $s$，我们就得到一个曲线方程，让曲线沿着 $s$ 这个维度
变化就得到了一个曲面

给定上面的曲线方程，其在某个点 $t\_0$ 的切向量可以表示为 $(x'(t\_0), y'(t\_0),
z'(t\_0))$，其中 $'$ 表示导数

* Proof

    以常见的2维等高线为例，等高线属于2维空间意味着函数属于3维空间，假设函数为
    $z = f(x, y)$，所谓某点处的 gradient 与等高线垂直，实际上指的是该点的
    gradient 与等高线的切线垂直

    对于函数 $z$，其等高线可以表示为 $f(x, y) = c$，其中 $c$ 为常数，同时2
    维空间中的任意曲线可以表示为 $\begin{cases} x = x(t) \\\\ y = y(t) \end{cases}$，
    将该表示法带入 $f(x, y) = c$，得 $f(x(t), y(t)) = c$
    
    给定 $t = t\_0$，记 $P = (x(t\_0), y(t\_0))$，对等式两边求导有

    $$
    \frac{\p f}{\p x}\Bigr| \_P \frac{\p x}{\p t} \Bigr| \_{t\_0} +
    \frac{\p f}{\p y}\Bigr| \_P \frac{\p y}{\p t} \Bigr| \_{t\_0} = 0
    $$

    换一种表示法

    $$
    \langle \frac{\p f}{\p x}\Bigr|\_P, \frac{\p f}{\p y}\Bigr|\_P \rangle \cdot
    \langle \frac{\p x}{\p t}\Bigr|\_{t\_0}, \frac{\p y}{\p t}\Bigr|\_{t\_0} \rangle = 0
    $$

    也就是两个向量内积为0，其中前一个向量就是 $f$ 在点 $P$ 处的
    gradient，后一个向量是切向量，所以 gradient 和切向量相互垂直，由于 $t\_0$
    是任意给定的，因此，gradient 和切向量在等高线的任何一点都相互垂直，这也就是
    上面所说的 gradient 和等高线相互垂直 $\EOP$

---

### Reference

* Reference for complex number
  [1](http://betterexplained.com/articles/a-visual-intuitive-guide-to-imaginary-numbers/) and
  [2](http://betterexplained.com/articles/intuitive-arithmetic-with-complex-numbers/)
* For proof related to symmetric matrix see [1](http://www.quandt.com/papers/basicmatrixtheorems.pdf)
* See [wikipedia](http://en.wikipedia.org/wiki/Elementary_matrix) for info about
  elementrary operations

