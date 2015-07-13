---
layout: post
title: 04 - Convex Set
categories: nnumop
tags: NPTEL, numerical optimization
---

这篇文章主要介绍各种和 Convex Set 相关的概念和性质。

### Line and Line Segment

<blockquote>
给定两个点 $\b{x}_1, \b{x}_2 \in \mathbb{R}^n$，line 可以被定义为

$$(1 - \lambda) \b{x}_1 + \lambda \b{x}_2 \;\; \forall \lambda \in \mathbb{R} $$
</blockquote>

参考下面这个图

<object data="/resource/NNP/04-convex/line.svg" type="image/svg+xml" class="blkcenter"></object>

根据向量相加的原则可知虚线上的点都可以表示成 $\b{x}\_1 + \lambda (\b{x}\_2 - \b{x}\_1) \; \forall \lambda \in \mathbb{R}$，也就是 $(1 - \lambda) \b{x}\_1 + \lambda \b{x}\_2$。

对于 line segment，只要限定 $\lambda$ 在 $[0, 1]$ 之间即可，即

<blockquote>
给定两个点 $\b{x}_1, \b{x}_2 \in \mathbb{R}^n$，line segment 可以被定义为

$$(1 - \lambda) \b{x}_1 + \lambda \b{x}_2 \;\; \forall \lambda \in [0, 1] $$

Line segment 也被记为 $LS[\b{x}_1, \b{x}_2]$
</blockquote>

### Affine Set

<blockquote>
给定集合 $A \in \mathbb{R}^n$，如果 $\forall \b{x}_1, \b{x}_2 \in A, \lambda \in \mathbb{R}$ 有 $(1 - \lambda) \b{x}_1 + \lambda \b{x}_2 \in A$，则 $A$ 被称为 Affine Set/Affine Space.
</blockquote>

这里给出一个推论，如果 $A$ 是 affine set，$\b{x}\_1, \b{x}\_2, \b{x}\_3 \in A$，则 $\b{x}\_1 + \lambda(\b{x}\_2 - \b{x}\_3) \in A$ (之所以给这个推论是为了下面定理的证明)。

* 证明

    $$
    \begin{align\*}
    & \b{x}\_1, \b{x}\_2, \b{x}\_3 \in A \\\\
    \Rightarrow & (1-\alpha) \b{x}\_1 + \alpha \b{x}\_2,\; (1-\beta)\b{x}\_2 + \beta \b{x}\_3 \in A \\\\
    \Rightarrow & (1-\gamma)((1-\alpha) \b{x}\_1 + \alpha \b{x}\_2) + \gamma ((1-\beta)\b{x}\_2 + \beta \b{x}\_3) \in A \\\\
    \equiv & (1-\gamma)(1-\alpha) \b{x}\_1 + (\alpha - \alpha \gamma + \gamma) \b{x}\_2 - \beta\gamma (\b{x}\_2 - \b{x}\_3) \in A
    \end{align\*}
    $$

    特别的，令 $(\alpha - \alpha \gamma + \gamma) = 0$，即 $\alpha = \frac{\gamma}{\gamma - 1}$，上面最后一个式子就简化为 $\b{x}\_1 - \beta\gamma (\b{x}\_2 - \b{x}\_3) \in A$，令 $\lambda = -\beta\gamma$，即 $\b{x}\_1 + \lambda(\b{x}\_2 - \b{x}\_3) \in A$。

<blockquote>
如果 $A$ 是 affine space，$\b{x}_1, \b{x}_2, \cdots, \b{x}_n \in A$ 且 $\sum_{i=1}^n \lambda_i = 1$，则 $\sum_{i=1}^n \lambda_i \b{x}_i \in A$
</blockquote>

* 证明 (Induction)

    * 当 $n = 1$ 时，上面的理论显然成立

    * 假设当 $n = k - 1$ 是，上述结论成立，当 $n = k$ 时有

        $$
        \begin{align\*}
        \sum\_{i = 1}^{k} \lambda\_i \b{x}\_i = & \lambda\_1 \b{x}\_1 + \lambda\_2 \b{x}\_2 + \cdots + (1 - \sum\_{i = 1}^{k - 1} \lambda\_i) \b{x}\_k \;\; (\because \sum\_{i=1}^{k} \lambda\_i = 1) \\\\
        = & (\lambda\_1 \b{x}\_1 + \lambda\_2 \b{x}\_2 + \cdots + \lambda\_{k-2} \b{x}\_{k-2} + (1 - \sum\_{i = 1}^{k - 2} \lambda\_i) \b{x}\_k) + \lambda\_{k-1}(\b{x}\_{k-1} - \b{x}\_{k}) \\\\
        = & \b{y} + \lambda\_{k-1}(\b{x}\_{k-1} - \b{x}\_{k}) \;\; (\b{y} \in A) \\\\
        \end{align\*}
        $$

        根据上面的推论 $\b{y} + \lambda\_{k-1}(\b{x}\_{k-1} - \b{x}\_{k}) \in A$，所以对于 $n = k$ 结论也成立

注意 affine space 和 vector space 的区别 (视频里一直用 vector subspace，但我觉得用 space 就可以了，因为 vector subspace 我觉得是个相对的概念，而且 vector subspace 本身也是 vector space)，vector space 要求如果 $\b{x}\_1, \b{x}\_2 \in A$ 则 $\alpha \b{x}\_1 + \beta \b{x}\_2 \in A \;\; \forall \alpha, \beta \in \mathbb{R}$，它要求任意的 linear combination 都属于 $A$，比 affine space 更严格。所以，$\b{0}$ 必须是 vector space 的一个元素，而对于 affine space 则没有这个要求，如下图所示

<object data="/resource/NNP/04-convex/affine_vector.svg" type="image/svg+xml" class="blkcenter"></object>

<blockquote>
如果 A 为 affine space，$\b{x}_0 \in A$，则 $\{\b{x} - \b{x}_0: \b{x} \in A\}$ 为 vector space
</blockquote>

* 证明

    令 $V = \\{\b{x} - \b{x}\_0: \b{x} \in A\\}, \;\; \b{x}\_1, \b{x}\_2 \in A$，则 $\b{x}\_1 - \b{x}\_0, \b{x}\_2 - \b{x}\_0 \in V$

    $$
    \begin{align\*}
    & \alpha(\b{x}\_1 - \b{x}\_0) + \beta(\b{x}\_2 - \b{x}\_0) \;\; (\forall \alpha, \beta \in \mathbb{R})\\\\
    = & \alpha \b{x}\_1 + \beta \b{x}\_2 + (1 - \alpha - \beta) \b{x}\_0 - \b{x}\_0 \\\\
    = & \b{y} - \b{x}\_0
    \end{align\*}
    $$

    根据前面定理可知，$\b{y} \in A$，所以 $\b{y} - \b{x}\_0 \in V$，因此 $V$ 是一个 vector space。

$A\b{x} = \b{b}$ 的解集属于 affine set

<blockquote>
令 $X = \{ \b{x}_1, \b{x}_2, \cdots, \b{x}_k \}$，如果一个点 

$$\b{x} = \sum_{i=1}^{k} \lambda_i \b{x}_i, \;\; \sum_{i=1}^{k} \lambda_i = 1$$

则这个点被称为 affine combination of points in $X$。所有可能的 affine combination 构成的集合被称为 affine hull 

$$aff(X) = \{\sum_{i=1}^{k} \lambda_i \b{x}_i: \b{x}_1, \cdots, \b{x}_k \in X, \sum_{i=1}^{k} \lambda_i = 1\}$$
</blockquote>

### Convex Set

<blockquote>
给定集合 $C \in \mathbb{R}^n$，如果 $\forall \b{x}_1, \b{x}_2 \in C, \lambda \in [0, 1]$ 有 $(1 - \lambda) \b{x}_1 + \lambda \b{x}_2 \in C$，则 $C$ 被称为 Convex Set.
</blockquote>

注意到这里的定义和 affine set 的极为相似，区别只在 $\lambda$ 的范围。对于 affine set，它要求经过 $\b{x}\_1, \b{x}\_2$ 的整个 line 都在集合中，而 convex set 只要求连接 $\b{x}\_1, \b{x}\_2$ 的 line segment 在集合中即可，所以 convex set 的要求要松很多，所有的 affine set 都同时是 convex set。

下图左边是一个 convex set，右边不是

<object data="/resource/NNP/04-convex/convex_example.svg" type="image/svg+xml" class="blkcenter"></object>

Convex set 的例子包括 empty set, singleton set, $\mathbb{R}$ 等等。

在 convex set 的基础上我们可以构造新的 convex set，常见操作包括

* Scalar multiple $\alpha C = \\{\alpha \b{x}: \b{x} \in C\\}$
* Sum of two sets $C = \\{\b{x}\_1 + \b{x}\_2: \b{x}\_1 \in C\_1, \b{x}\_2 \in C\_2\\}$
* Intersection $C = \cap\_i C\_i$

上述操作得到的 set 依然是 convex set，证明比较简单，就略过了。

<blockquote>
给定集合 $S$，所有包含 $S$ 的 convex set 的交集被称为 $S$ 对应的 convex hull
</blockquote>

Convex hull 是包含 $S$ 的最小的 convex set。

### Hyperplane

<blockquote>
令 $\b{a} \in \mathbb{R}^n, \b{a} \neq 0, b \in \mathbb{R}$, 集合 $H = \{\b{x}: \b{a}^T \b{x} = b\}$ 被称为 hyperplane，其中 $\b{a}$ 被称为 normal vector
</blockquote>

另一种定义 hyperplane 的方法是，如果已知一个点 $\b{x}\_0 \in H$，则 hyperplane 可以表示为 $\b{a}^T (\b{x} - \b{x}\_0) = 0$

* 如果 $\Vert \b{a} \Vert = 1$，则 $b$ 就是原点到 $H$ 的距离
* Closed positive half-space: $\b{a}^T\b{x} \geq b$
* Closed negative half-space: $\b{a}^T\b{x} \leq b$

下图给出了一个对 $f(\b{x})$ 的 contour 的一阶近似的 hyperplane，其中 $g(\b{x}\_0)$ 是 gradient

<object data="/resource/NNP/04-convex/contour_app.svg" type="image/svg+xml" class="blkcenter"></object>

Hyperplane 是一个 convex set，所以 $A\b{x} = \b{b}$ 的解集也是一个 convex set，因为 $A\b{x} = \b{b}$ 可以被看成是一堆 $\b{a}^T\b{x} = b$ 的交集。

关于 hyperplane 的表示这里多说两句，用 $\b{a}^T \b{x} = b$ 表示 hyperplane 是比较科学的，因为这种表示法明确给出了 normal vector 和截距。举个例子，令 $\b{x} \in \mathbb{R}^2$，如果你用 $\b{x}\_1 = \b{x}\_2$ 表示一个 hyperplane，那你就不知道它的 normal vector 到底是什么，可以是 $(-1, 1)^T$ 也可以是 $(1, -1)^T$，如果你用 $(-1, 1)\begin{pmatrix}\b{x}\_1 \\\\ \b{x}\_2\end{pmatrix} = 0$ 表示，我就知道 normal vector 是 $(-1, 1)^T$，这样我也能明确知道直线下方的区域满足 $(-1, 1)\begin{pmatrix}\b{x}\_1 \\\\ \b{x}\_2\end{pmatrix} < 0$，上方的区域满足 $(-1, 1)\begin{pmatrix}\b{x}\_1 \\\\ \b{x}\_2\end{pmatrix} > 0$。所以总的来说，$\b{a}^T \b{x} = b$ 是一种很清晰的表示方法。

### Convex Set 相关定理

<blockquote>
给定 $S \subset \mathbb{R}^n$ 为 closed convex set，$\b{y} \notin S$，则存在唯一的一个点 $\b{x}_0 \in S$ 满足 $\b{x}_0 = \arg\min_{\b{x} \in S} \Vert \b{y} - \b{x} \Vert$
</blockquote>

* 证明

    * 首先证明存在这样的 $\b{x}\_0$

        由于 $\Vert \b{y} - \b{x} \Vert$ 是 continuous function，所以如果 $S$ 是 compact set，则根据 Weiestrass' therom，$S$ 中必存在一个点 $\b{x}\_0$ 使得 $\Vert \b{y} - \b{x} \Vert$ 最小。不过 $S$ 只是个 closed set，不是 bounded set，因此 Weiestrass' therom 不能直接应用。

        假设 $\b{x}\_1 \in S, \; \delta = \Vert \b{y} - \b{x}\_1 \Vert$，令 $C = \\{ \b{x}: \Vert \b{y} - \b{x} \Vert \leq 2\delta \\}$，如下图所示

        <object data="/resource/NNP/04-convex/convex_therom_1.svg" type="image/svg+xml" class="blkcenter"></object>

        易知 $S \cap C$ 一个 compact set，因此在 $S\cap C$ 中必存在一个点 $\b{x}\_0$ 满足 $\b{x}\_0 = \arg\min\_{\b{x} \in S \cap C} \Vert \b{y} - \b{x} \Vert$，而 $\Vert \b{y} - \b{x} \Vert > 2\delta \;\; \forall\b{x} \in S \setminus C$，因此 $\b{x}\_0$ 同样满足 $\b{x}\_0 = \arg\min\_{\b{x} \in S} \Vert \b{y} - \b{x} \Vert$。

    * 然后证明这个点唯一

        假设这个点不唯一，存在另一个点 $\b{x}\_1 \in S$ 满足条件，即 $\Vert \b{y} - \b{x}\_0 \Vert = \Vert \b{y} - \b{x}\_1 \Vert$，因为 $S$ 是个 convex set，所以 $\frac{\b{x}\_0 + \b{x}\_1}{2} \in S$。
        
        如果 $\b{x}\_0$ 和 $\b{x}\_1$ 不是一个点的话，根据三角不等式有 

        $$2\Vert \b{y} - \frac{\b{x}\_0 + \b{x}\_1}{2} \Vert < \Vert \b{y} - \b{x}\_0 \Vert + \Vert \b{y} - \b{x}\_1 \Vert = 2\Vert \b{y} - \b{x}\_0 \Vert$$

        也就是 $\Vert \b{y} - \frac{\b{x}\_0 + \b{x}\_1}{2} \Vert < \Vert \b{y} - \b{x}\_0 \Vert$，这与 $\b{x}\_0$ 是最小值点矛盾，所以 $\b{x}\_0$ 和 $\b{x}\_1$ 必是同一个点。

<blockquote>
给定 $S \subset \mathbb{R}^n$ 为 closed convex set，$\b{y} \notin S$ <br/>
$\b{x}_0 = \arg\min_{\b{x} \in S} \Vert \b{y} - \b{x} \Vert$ 当且仅当 $(\b{y} - \b{x}_0)^T(\b{x} - \b{x}_0) \leq 0 \;\; \forall \b{x} \in S$
</blockquote>

这个定理通俗一点讲，就是如果 $\b{x}\_0$ 是 $S$ 中与 $\b{y}$ 距离最近的点，则所有其他 $S$ 中的点和 $\b{x}\_0$ 的连线与 $\b{y}$ 和 $\b{x}\_0$ 的连线都构成钝角，如下图所示

<object data="/resource/NNP/04-convex/convex_therom_2.svg" type="image/svg+xml" class="blkcenter"></object>

* 证明
  
    * $\b{x}\_0 = \arg\min\_{\b{x} \in S} \Vert \b{y} - \b{x} \Vert \Rightarrow (\b{y} - \b{x}\_0)^T(\b{x} - \b{x}\_0) \leq 0 \;\; \forall \b{x} \in S$

        由于 $\b{x}\_0$ 是最小值点，所以 $\forall \b{x} \in S$，我们都有 $\Vert \b{y} - \b{x}\_0 \Vert^2 \leq \Vert \b{y} - (\b{x}\_0 + \lambda(\b{x} - \b{x}\_0))\Vert^2\;\; \lambda \in [0, 1]$，把左边式子展开有

        $$
        \begin{align\*}
        \Vert \b{y} - \b{x}\_0 \Vert^2 & \leq \Vert \b{y} - (\b{x}\_0 + \lambda(\b{x} - \b{x}\_0))\Vert^2 \\\\
        & = \Vert \b{y} - \b{x}\_0 \Vert^2 - 2 \lambda \Vert  \b{y} - \b{x}\_0 \Vert \Vert \b{x} - \b{x}\_0\Vert + \lambda^2 \Vert \b{x} - \b{x}\_0\Vert \\\\
        \end{align\*}
        $$

        由此推出 $2 \Vert  \b{y} - \b{x}\_0 \Vert \Vert \b{x} - \b{x}\_0\Vert \leq \lambda \Vert \b{x} - \b{x}\_0\Vert$，不等式两边对 $\lambda$ 取极限 $\lambda \rightarrow 0^+$，有 $(\b{y} - \b{x}\_0)^T(\b{x} - \b{x}\_0) \leq 0$

    * $(\b{y} - \b{x}\_0)^T(\b{x} - \b{x}\_0) \leq 0 \;\; \forall \b{x} \in S \Rightarrow \b{x}\_0 = \arg\min\_{\b{x} \in S} \Vert \b{y} - \b{x} \Vert$

        $$
        \begin{align\*}
        \Vert \b{y} - \b{x} \Vert^2 = & \Vert (\b{y} - \b{x}\_0) - (\b{x} - \b{x}\_0) \Vert^2 \\\\
        = & \Vert \b{y} - \b{x}\_0 \Vert^2 - 2 \Vert \b{y} - \b{x}\_0 \Vert\Vert \b{x} - \b{x}\_0 \Vert + \Vert \b{x} - \b{x}\_0 \Vert^2
        \end{align\*}
        $$

        所以如果 $(\b{y} - \b{x}\_0)^T(\b{x} - \b{x}\_0) \leq 0$ 则 $\Vert \b{y} - \b{x} \Vert^2 \geq \Vert \b{y} - \b{x}\_0 \Vert^2\;\; \forall \b{x} \in S$

### Seperating Hyperplane

<blockquote>
给定集合 $S_1, S_2$，如果存在 hyperplane $\b{a}^T\b{x} = b$ 满足 $\b{a}^T\b{x} \geq b \; \forall x \in S_1,\;\b{a}^T\b{x} \leq b \; \forall x \in S_2$，则 $\b{a}^T\b{x} = b$ 称为 $S_1, S_2$ 的 seperating hyperplane。
</blockquote>

* 如果条件变为 $\b{a}^T\b{x} > b \; \forall x \in S\_1,\;\b{a}^T\b{x} < b \; \forall x \in S\_2$，则称为 strictly seperate
* 如果条件变为 $\b{a}^T\b{x} \geq b + \varepsilon \; \forall x \in S\_1 \; \forall \varepsilon > 0,\;\b{a}^T\b{x} \leq b \; \forall x \in S\_2$，则称为 strongly seperate

根据上面给出的两个 convex set 定理，给定一个 closed convex set $S$ 和点
$\b{y} \notin S$，一定存在一个 hyperplane $\b{a}^T\b{x} = b$ 能 seperate
$\b{y}$ 和 $S$，下面是两个这样的 hyperplane

* 令 $\b{a} = \b{y} - \b{x}\_0, b = \b{a}^T \b{x}\_0$ (该 hyperplane 经过 $\b{x}\_0$)

    因为 $(\b{y} - \b{x}\_0)^T(\b{x} - \b{x}\_0) \leq 0 \;\; \forall \b{x} \in S$，
    所以 $\b{a}^T\b{x} \leq b \; \forall \b{x} \in S$，而 $\b{a}^T \b{y} - b =
    (\b{y} - \b{x}\_0)^T(\b{y} - \b{x}\_0)$，因为 $\b{y} \neq \b{x}\_0$，所以
    $\b{a}^T \b{y} > b$

* 令 $\b{a} = \b{y} - \b{x}\_0, b = \b{a}^T \b{y}$ (该 hyperplane 经过 $\b{y}$)

    易证 $(\b{y} - \b{x}\_0)^T(\b{x} - \b{y}) < (\b{y} - \b{x}\_0)^T(\b{x} -
    \b{x}\_0)$ (两边相减即可得该不等式)，而 $\forall \b{x} \in S, (\b{y} -
    \b{x}\_0)^T(\b{x} - \b{x}\_0) \leq 0$ 所以 $\forall \b{x} \in S$ 都有
    $(\b{y} - \b{x}\_0)^T(\b{x} - \b{y}) < 0$，也就是 $S \subset H^-$

<blockquote>
如果 $S_1, S_2$ 是非空且无交集的 convex set，那必然存在一个 hyperplane 能 seperate $S_1, S_2$
</blockquote>

* 证明

    令 $S = S\_1 - S\_2 = \\{\b{x}\_1 - \b{x}\_2 : \b{x}\_1 \in S\_1, \b{x}\_2 \in S\_2\\}$，易知 $\b{0} \notin S$。

    根据上面的结论，可以构造一个 hyperplane $H: \b{a}^T(\b{x} - \b{0}) = 0$ 使得 $S \subset H^-$。也就是存在 hyperplane 使得 $\b{a}^T\b{x}\_1 < \b{a}^T\b{x}\_2$。
  
### Cone

<blockquote>
给定集合 $C$，如果给定任一 $\b{x} \in C$ 都有 $\lambda \b{x} \in C \; \forall \lambda \in \mathbb{R}$，则 $C$ 被称为 Cone
</blockquote>

* Example. 一条直线是一个 cone，两条相交的直线也是一个 cone

### Farkas' Lemma

<blockquote>
令 $A \in \mathbb{R}^{m\times n}, \b{c} \in \mathbb{R}^n$，则下面两个结论有且只有一个是成立的 <br/>
1. $\exists \b{x} \in \mathbb{R}^n \;\;\st\;\; A\b{x} \leq \b{0}, \b{c}^T \b{x} > 0$<br/>
2. $\exists \b{y} \in \mathbb{R}^m \;\;\st\;\; A^T\b{y} = \b{c}, \b{y} \geq \b{0}$
</blockquote>

首先从几何的角度直观理解一下 Farkas' lemma。令 $A = \begin{pmatrix} \b{a}\_1
\\\\ \b{a}\_2 \\\\ \b{a}\_3 \end{pmatrix}$，其中 $\b{a}\_i$
为行向量，考虑下面的两个图，左边图对应上面的结论 1，其中蓝色区域对应所有满足
$A\b{x} \leq 0$ 的 $\b{x}$，$\b{c}$ 与这些 $\b{x}$ 的内积都 $\gt 0$。
右边图对应结论 2，其中 $\b{c}^T\b{x} < 0$，但 $\b{c}$ 可以表示为 3 个 $\b{a}$
向量的线性组合同时系数都大于 0。很明显这两个结论是相互独立的，因为一个要求
$\b{c}$ 处于以 $\b{a}\_1$ 和 $\b{a}\_3$ 为边界的区域之外，一个要求处于这个
边界之内

<object data="/resource/NNP/04-convex/farkas.svg" type="image/svg+xml" class="blkcenter"></object>

* 证明

    * 如果结论 2 成立，则用反证法即可很快的证明 $A\b{x} \leq \b{0}$ 和 $\b{c}^T
      \b{x} > 0$ 不能同时成立

    * 如果结论 2 不成立

        结论 2 不成立等价于存在集合 $S = \\{\b{x}: \b{x} = A^T\b{y}, \b{y} \geq
        0\\}$ 且 $\b{c} \notin S$
        
        根据前面 seperating hyperplane 得到的结论，必然存在一个 hyperplane 能
        seperate $S$ 和 $\b{c}$，假设该 hyperplane 为 $\b{a}^T\b{x} = b$，则有
        $\b{a}^T\b{x} \leq b \; \forall\b{x} \in S$ 同时 $\b{a}^T\b{c} > b$

        因为 $\b{0} \in S$ 所以 $b \geq 0$，所以 $\b{a}^T\b{c} > 0$

        对于 $S$ 中的 $\b{x}$，$b \geq \b{a}^T\b{x} = \b{a}^T A^T \b{y} =
        \b{y}^T A\b{a}$，因为 $\b{y} \geq 0$，所以如果 $A\b{a} > \b{0}$，我令
        $\b{y}$ 趋于无穷大，则 $\b{y}^T A\b{a} \leq b$ 这个不等式必然不能成立，
        因此必有 $A\b{a} \leq 0$

        所以 $\b{a}$ 就是我们要找的满足结论 1 中两个不等式的 $\b{x}$

根据 Farkas' lemma，可以得出如下推论

<blockquote>
令 $A \in \mathbb{R}^{m\times n}$，则下面两个结论有且只有一个是成立的 <br/>
1. $\exists \b{x} \in \mathbb{R}^n \;\;\st\;\; A\b{x} < \b{0}$<br/>
2. $\exists \b{y} \in \mathbb{R}^m \;\;\st\;\; A^T\b{y} = \b{0}, \b{y} \geq \b{0}$
</blockquote>

乍一看好像令 $\b{c} = \b{0}$ 就能得出这个推论，其实不然，首先推论里结论 1 是
$A^T\b{x} < 0$ 而不是 $A^T\b{x} \leq 0$，另外 $\b{c} = \b{0}$ 是不符合 Farkas'
Lemma 的，因为 Farkas' Lemma 要求 $\b{c}^T\b{x} > 0$

* 证明

    由于 $A\b{x} < 0$ 所以 $A\b{x} + z\b{e} = (A, \b{e})\begin{pmatrix} \b{x} \\\\ z\end{pmatrix}\leq 0$ 其中 $z > 0, \b{e} = (1, 1, ..., 1)^T \in \mathbb{R}^m$。

    令 $\b{c} = (0, 0, ..., 0, 1)^T \in \mathbb{R}^{n+1}$，则有 $\b{c}^T \begin{pmatrix} \b{x} \\\\ z\end{pmatrix} > 0$。

    这样也就有了 Farkas' lemma 的结论 1，结论 2 相应的是 $(A, \b{e})^T \b{y} = (0, 0, ..., 0, 1)$，也就是 $A^T \b{y} = \b{0}, \b{e}^T \b{y} = 1$。

    至此也就构造出了上述推论。

### Supporting Hyperplane

<blockquote>
令 $S \neq \emptyset \subset \mathbb{R}^n$，$\b{x}_0$ 为 $S$ 的 boundary point，如果存在 hyperplane $\b{a}^T(\b{x} - \b{x}_0) = 0$ 使得<br/>
1. $S \subseteq H^+$, 即 $\b{a}^T(\b{x} - \b{x}_0) \geq 0 \; \forall \b{x} \in S$ 或者 <br/>
2. $S \subseteq H^-$, 即 $\b{a}^T(\b{x} - \b{x}_0) \leq 0 \; \forall \b{x} \in S$<br/>
则该 hyperplane 称为 $S$ 的 supporting hyperplane
</blockquote>

* 如果 $S$ 是个 convex set，则在 $\b{x}\_0$ 处必然存在 supporting hyperplane。

