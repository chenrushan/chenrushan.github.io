---
layout: post
title: 04 - Convex Set
categories: nnumop
tags: NPTEL, numerical optimization
---

这篇文章主要介绍各种和 Convex Set 相关的概念和性质。

#### Line and Line Segment

<blockquote>
给定两个点 $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathbb{R}^n$，line 可以被定义为

$$(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2 \;\; \forall \lambda \in \mathbb{R} $$
</blockquote>

参考下面这个图

<object data="/resource/NNP/04-convex/line.svg" type="image/svg+xml" class="blkcenter"></object>

根据向量相加的原则可知虚线上的点都可以表示成 $\boldsymbol{x}\_1 + \lambda (\boldsymbol{x}\_2 - \boldsymbol{x}\_1) \; \forall \lambda \in \mathbb{R}$，也就是 $(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2$。

对于 line segment，只要限定 $\lambda$ 在 $[0, 1]$ 之间即可，即

<blockquote>
给定两个点 $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathbb{R}^n$，line segment 可以被定义为

$$(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2 \;\; \forall \lambda \in [0, 1] $$

Line segment 也被记为 $LS[\boldsymbol{x}_1, \boldsymbol{x}_2]$
</blockquote>

#### Affine Set

<blockquote>
给定集合 $A \in \mathbb{R}^n$，如果 $\forall \boldsymbol{x}_1, \boldsymbol{x}_2 \in A, \lambda \in \mathbb{R}$ 有 $(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2 \in A$，则 $A$ 被称为 Affine Set/Affine Space.
</blockquote>

这里给出一个推论，如果 $A$ 是 affine set，$\boldsymbol{x}\_1, \boldsymbol{x}\_2, \boldsymbol{x}\_3 \in A$，则 $\boldsymbol{x}\_1 + \lambda(\boldsymbol{x}\_2 - \boldsymbol{x}\_3) \in A$ (之所以给这个推论是为了下面定理的证明)。

* 证明

  $$
  \begin{align}
  & \boldsymbol{x}\_1, \boldsymbol{x}\_2, \boldsymbol{x}\_3 \in A \\\\
  \Rightarrow & (1-\alpha) \boldsymbol{x}\_1 + \alpha \boldsymbol{x}\_2,\; (1-\beta)\boldsymbol{x}\_2 + \beta \boldsymbol{x}\_3 \in A \\\\
  \Rightarrow & (1-\gamma)((1-\alpha) \boldsymbol{x}\_1 + \alpha \boldsymbol{x}\_2) + \gamma ((1-\beta)\boldsymbol{x}\_2 + \beta \boldsymbol{x}\_3) \in A \\\\
  \equiv & (1-\gamma)(1-\alpha) \boldsymbol{x}\_1 + (\alpha - \alpha \gamma + \gamma) \boldsymbol{x}\_2 - \beta\gamma (\boldsymbol{x}\_2 - \boldsymbol{x}\_3) \in A
  \end{align}
  $$

  特别的，令 $(\alpha - \alpha \gamma + \gamma) = 0$，即 $\alpha = \frac{\gamma}{\gamma - 1}$，上面最后一个式子就简化为 $\boldsymbol{x}\_1 - \beta\gamma (\boldsymbol{x}\_2 - \boldsymbol{x}\_3) \in A$，令 $\lambda = -\beta\gamma$，即 $\boldsymbol{x}\_1 + \lambda(\boldsymbol{x}\_2 - \boldsymbol{x}\_3) \in A$。

<blockquote>
如果 $A$ 是 affine space，$\boldsymbol{x}_1, \boldsymbol{x}_2, \cdots, \boldsymbol{x}_n \in A$ 且 $\sum_{i=1}^n \lambda_i = 1$，则 $\sum_{i=1}^n \lambda_i \boldsymbol{x}_i \in A$
</blockquote>

* 证明 (Induction)

  * 当 $n = 1$ 时，上面的理论显然成立

  * 假设当 $n = k - 1$ 是，上述结论成立，当 $n = k$ 时有

     $$
     \begin{align}
     \sum\_{i = 1}^{k} \lambda\_i \boldsymbol{x}\_i = & \lambda\_1 \boldsymbol{x}\_1 + \lambda\_2 \boldsymbol{x}\_2 + \cdots + (1 - \sum\_{i = 1}^{k - 1} \lambda\_i) \boldsymbol{x}\_k \;\; (\because \sum\_{i=1}^{k} \lambda\_i = 1) \\\\
     = & (\lambda\_1 \boldsymbol{x}\_1 + \lambda\_2 \boldsymbol{x}\_2 + \cdots + \lambda\_{k-2} \boldsymbol{x}\_{k-2} + (1 - \sum\_{i = 1}^{k - 2} \lambda\_i) \boldsymbol{x}\_k) + \lambda\_{k-1}(\boldsymbol{x}\_{k-1} - \boldsymbol{x}\_{k}) \\\\
     = & \boldsymbol{y} + \lambda\_{k-1}(\boldsymbol{x}\_{k-1} - \boldsymbol{x}\_{k}) \;\; (\boldsymbol{y} \in A) \\\\
     \end{align}
     $$

     根据上面的推论 $\boldsymbol{y} + \lambda\_{k-1}(\boldsymbol{x}\_{k-1} - \boldsymbol{x}\_{k}) \in A$，所以对于 $n = k$ 上述结论也成立。

----------

注意 affine space 和 vector space 的区别 (视频里一直用 vector subspace，但我觉得用 space 就可以了，因为 vector subspace 我觉得是个相对的概念，而且 vector subspace 本身也是 vector space)，vector space 要求如果 $\boldsymbol{x}\_1, \boldsymbol{x}\_2 \in A$ 则 $\alpha \boldsymbol{x}\_1 + \beta \boldsymbol{x}\_2 \in A \;\; \forall \alpha, \beta \in \mathbb{R}$，它要求任意的 linear combination 都属于 $A$，比 affine space 更严格。所以，$\boldsymbol{0}$ 必须是 vector space 的一个元素，而对于 affine space 则没有这个要求，如下图所示

<object data="/resource/NNP/04-convex/affine_vector.svg" type="image/svg+xml" class="blkcenter"></object>

<blockquote>
如果 A 为 affine space，$\boldsymbol{x}_0 \in A$，则 $\{\boldsymbol{x} - \boldsymbol{x}_0: \boldsymbol{x} \in A\}$ 为 vector space
</blockquote>

* 证明

  令 $V = \\{\boldsymbol{x} - \boldsymbol{x}\_0: \boldsymbol{x} \in A\\}, \;\; \boldsymbol{x}\_1, \boldsymbol{x}\_2 \in A$，则 $\boldsymbol{x}\_1 - \boldsymbol{x}\_0, \boldsymbol{x}\_2 - \boldsymbol{x}\_0 \in V$

  $$
  \begin{align}
  & \alpha(\boldsymbol{x}\_1 - \boldsymbol{x}\_0) + \beta(\boldsymbol{x}\_2 - \boldsymbol{x}\_0) \;\; (\forall \alpha, \beta \in \mathbb{R})\\\\
  = & \alpha \boldsymbol{x}\_1 + \beta \boldsymbol{x}\_2 + (1 - \alpha - \beta) \boldsymbol{x}\_0 - \boldsymbol{x}\_0 \\\\
  = & \boldsymbol{y} - \boldsymbol{x}\_0
  \end{align}
  $$

  根据前面定理可知，$\boldsymbol{y} \in A$，所以 $\boldsymbol{y} - \boldsymbol{x}\_0 \in V$，因此 $V$ 是一个 vector space。

----------

$A\boldsymbol{x} = \boldsymbol{b}$ 的解集属于 affine set

<blockquote>
令 $X = \{ \boldsymbol{x}_1, \boldsymbol{x}_2, \cdots, \boldsymbol{x}_k \}$，如果一个点 

$$\boldsymbol{x} = \sum_{i=1}^{k} \lambda_i \boldsymbol{x}_i, \;\; \sum_{i=1}^{k} \lambda_i = 1$$

则这个点被称为 affine combination of points in $X$。所有可能的 affine combination 构成的集合被称为 affine hull 

$$aff(X) = \{\sum_{i=1}^{k} \lambda_i \boldsymbol{x}_i: \boldsymbol{x}_1, \cdots, \boldsymbol{x}_k \in X, \sum_{i=1}^{k} \lambda_i = 1\}$$
</blockquote>

#### Convex Set

<blockquote>
给定集合 $C \in \mathbb{R}^n$，如果 $\forall \boldsymbol{x}_1, \boldsymbol{x}_2 \in C, \lambda \in [0, 1]$ 有 $(1 - \lambda) \boldsymbol{x}_1 + \lambda \boldsymbol{x}_2 \in C$，则 $C$ 被称为 Convex Set.
</blockquote>

注意到这里的定义和 affine set 的极为相似，区别只在 $\lambda$ 的范围。对于 affine set，它要求经过 $\boldsymbol{x}\_1, \boldsymbol{x}\_2$ 的整个 line 都在集合中，而 convex set 只要求连接 $\boldsymbol{x}\_1, \boldsymbol{x}\_2$ 的 line segment 在集合中即可，所以 convex set 的要求要松很多，所有的 affine set 都同时是 convex set。

下图左边是一个 convex set，右边不是

<object data="/resource/NNP/04-convex/convex_example.svg" type="image/svg+xml" class="blkcenter"></object>

Convex set 的例子包括 empty set, singleton set, $\mathbb{R}$ 等等。

在 convex set 的基础上我们可以构造新的 convex set，常见操作包括

* Scalar multiple $\alpha C = \\{\alpha \boldsymbol{x}: \boldsymbol{x} \in C\\}$

* Sum of two sets $C = \\{\boldsymbol{x}\_1 + \boldsymbol{x}\_2: \boldsymbol{x}\_1 \in C\_1, \boldsymbol{x}\_2 \in C\_2\\}$

* Intersection $C = \cap\_i C\_i$

上述操作得到的 set 依然是 convex set，证明比较简单，就略过了。

<blockquote>
给定集合 $S$，所有包含 $S$ 的 convex set 的交集被称为 $S$ 对应的 convex hull
</blockquote>

Convex hull 是包含 $S$ 的最小的 convex set。

#### Hyperplane

<blockquote>
令 $\boldsymbol{a} \in \mathbb{R}^n, \boldsymbol{a} \neq 0, b \in \mathbb{R}$, 集合 $H = \{\boldsymbol{x}: \boldsymbol{a}^T \boldsymbol{x} = b\}$ 被称为 hyperplane，其中 $\boldsymbol{a}$ 被称为 normal vector
</blockquote>

另一种定义 hyperplane 的方法是，如果已知一个点 $\boldsymbol{x}\_0 \in H$，则 hyperplane 可以表示为 $\boldsymbol{a}^T (\boldsymbol{x} - \boldsymbol{x}\_0) = 0$

* 如果 $\Vert \boldsymbol{a} \Vert = 1$，则 $b$ 就是原点到 $H$ 的距离

* Closed positive half-space: $\boldsymbol{a}^T\boldsymbol{x} \geq b$

* Closed negative half-space: $\boldsymbol{a}^T\boldsymbol{x} \leq b$

下图给出了一个对 $f(\boldsymbol{x})$ 的 contour 的一阶近似的 hyperplane，其中 $g(\boldsymbol{x}\_0)$ 是 gradient

<object data="/resource/NNP/04-convex/contour_app.svg" type="image/svg+xml" class="blkcenter"></object>

Hyperplane 是一个 convex set，所以 $A\boldsymbol{x} = \boldsymbol{b}$ 的解集也是一个 convex set，因为 $A\boldsymbol{x} = \boldsymbol{b}$ 可以被看成是一堆 $\boldsymbol{a}^T\boldsymbol{x} = b$ 的交集。

#### Convex Set 相关定理

<blockquote>
给定 $S \in \mathbb{R}^n$ 为 closed convex set，$\boldsymbol{y} \notin S$，则存在唯一的一个点 $\boldsymbol{x}_0 \in S$ 满足 $\boldsymbol{x}_0 = \arg\min_{\boldsymbol{x} \in S} \Vert \boldsymbol{y} - \boldsymbol{x} \Vert$
</blockquote>

* 证明

  * 首先证明存在这样的 $\boldsymbol{x}\_0$

     由于 $\Vert \boldsymbol{y} - \boldsymbol{x} \Vert$ 是 continuous function，所以如果 $S$ 是 compact set，则根据 Weiestrass' therom，$S$ 中必存在一个点 $\boldsymbol{x}\_0$ 使得 $\Vert \boldsymbol{y} - \boldsymbol{x} \Vert$ 最小。不过 $S$ 只是个 closed set，不是 bounded set，因此 Weiestrass' therom 不能直接应用。

     假设 $\boldsymbol{x}\_1 \in S, \; \delta = \Vert \boldsymbol{y} - \boldsymbol{x}\_1 \Vert$，令 $C = \\{ \boldsymbol{x}: \Vert \boldsymbol{y} - \boldsymbol{x} \Vert \leq 2\delta \\}$，如下图所示

     <object data="/resource/NNP/04-convex/convex_therom_1.svg" type="image/svg+xml" class="blkcenter"></object>

     易知 $S \cap C$ 一个 compact set，因此在 $S\cap C$ 中必存在一个点 $\boldsymbol{x}\_0$ 满足 $\boldsymbol{x}_0 = \arg\min_{\boldsymbol{x} \in S \cap C} \Vert \boldsymbol{y} - \boldsymbol{x} \Vert$，而 $\Vert \boldsymbol{y} - \boldsymbol{x} \Vert > 2\delta \;\; \forall\boldsymbol{x} \in S \setminus C$，因此 $\boldsymbol{x}\_0$ 同样满足 $\boldsymbol{x}_0 = \arg\min_{\boldsymbol{x} \in S} \Vert \boldsymbol{y} - \boldsymbol{x} \Vert$。

  * 然后证明这个点唯一

     假设这个点不唯一，存在另一个点 $\boldsymbol{x}\_1 \in S$ 满足条件，则有 $\Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert = \Vert \boldsymbol{y} - \boldsymbol{x}\_1 \Vert$，而 $S$ 是个 convex set，所以 $\frac{\boldsymbol{x}\_0 + \boldsymbol{x}\_1}{2} \in S$。
     
     如果 $\boldsymbol{x}\_0$ 和 $\boldsymbol{x}\_1$ 不是一个点的话，根据三角不等式有 

     $$2\Vert \boldsymbol{y} - \frac{\boldsymbol{x}\_0 + \boldsymbol{x}\_1}{2} \Vert < \Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert + \Vert \boldsymbol{y} - \boldsymbol{x}\_1 \Vert = 2\Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert$$

     也就是 $\Vert \boldsymbol{y} - \frac{\boldsymbol{x}\_0 + \boldsymbol{x}\_1}{2} \Vert < \Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert$，这与 $\boldsymbol{x}\_0$ 是最小值点矛盾，所以 $\boldsymbol{x}\_0$ 和 $\boldsymbol{x}\_1$ 必是同一个点。

----------

<blockquote>
给定 $S \in \mathbb{R}^n$ 为 closed convex set，$\boldsymbol{y} \notin S$ <br/>
$\boldsymbol{x}_0 = \arg\min_{\boldsymbol{x} \in S} \Vert \boldsymbol{y} - \boldsymbol{x} \Vert$ 当且仅当 $(\boldsymbol{y} - \boldsymbol{x}_0)^T(\boldsymbol{x} - \boldsymbol{x}_0) \leq 0 \;\; \forall \boldsymbol{x} \in S$
</blockquote>

这个定理通俗一点讲，就是如果 $\boldsymbol{x}\_0$ 是 $S$ 中与 $\boldsymbol{y}$ 距离最近的点，则所有其他 $S$ 中的点和 $\boldsymbol{x}\_0$ 的连线与 $\boldsymbol{y}$ 和 $\boldsymbol{x}\_0$ 的连线都构成钝角，如下图所示

<object data="/resource/NNP/04-convex/convex_therom_2.svg" type="image/svg+xml" class="blkcenter"></object>

* 证明
  
  * $\boldsymbol{x}_0 = \arg\min_{\boldsymbol{x} \in S} \Vert \boldsymbol{y} - \boldsymbol{x} \Vert \Rightarrow (\boldsymbol{y} - \boldsymbol{x}_0)^T(\boldsymbol{x} - \boldsymbol{x}_0) \leq 0 \;\; \forall \boldsymbol{x} \in S$

     由于 $\boldsymbol{x}\_0$ 是最小值点，所以 $\forall \boldsymbol{x} \in S$，我们都有 $\Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert^2 \leq \Vert \boldsymbol{y} - (\boldsymbol{x}\_0 + \lambda(\boldsymbol{x} - \boldsymbol{x}\_0))\Vert^2\;\; \lambda \in [0, 1]$，把左边式子展开有

     $$
     \begin{align}
     \Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert^2 & \leq \Vert \boldsymbol{y} - (\boldsymbol{x}\_0 + \lambda(\boldsymbol{x} - \boldsymbol{x}\_0))\Vert^2 \\\\
     & = \Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert^2 - 2 \lambda \Vert  \boldsymbol{y} - \boldsymbol{x}\_0 \Vert \Vert \boldsymbol{x} - \boldsymbol{x}\_0\Vert + \lambda^2 \Vert \boldsymbol{x} - \boldsymbol{x}\_0\Vert \\\\
     \end{align}
     $$

     由此推出 $2 \Vert  \boldsymbol{y} - \boldsymbol{x}\_0 \Vert \Vert \boldsymbol{x} - \boldsymbol{x}\_0\Vert \leq \lambda \Vert \boldsymbol{x} - \boldsymbol{x}\_0\Vert$，不等式两边对 $\lambda$ 取极限 $\lambda \rightarrow 0^+$，有 $(\boldsymbol{y} - \boldsymbol{x}_0)^T(\boldsymbol{x} - \boldsymbol{x}_0) \leq 0$

  * $(\boldsymbol{y} - \boldsymbol{x}_0)^T(\boldsymbol{x} - \boldsymbol{x}_0) \leq 0 \;\; \forall \boldsymbol{x} \in S \Rightarrow \boldsymbol{x}_0 = \arg\min_{\boldsymbol{x} \in S} \Vert \boldsymbol{y} - \boldsymbol{x} \Vert$

     $$
     \begin{align}
     \Vert \boldsymbol{y} - \boldsymbol{x} \Vert^2 = & \Vert (\boldsymbol{y} - \boldsymbol{x}\_0) - (\boldsymbol{x} - \boldsymbol{x}\_0) \Vert^2 \\\\
     = & \Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert^2 - 2 \Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert\Vert \boldsymbol{x} - \boldsymbol{x}\_0 \Vert + \Vert \boldsymbol{x} - \boldsymbol{x}\_0 \Vert^2
     \end{align}
     $$

     所以如果 $(\boldsymbol{y} - \boldsymbol{x}_0)^T(\boldsymbol{x} - \boldsymbol{x}_0) \leq 0$ 则 $\Vert \boldsymbol{y} - \boldsymbol{x} \Vert^2 \geq \Vert \boldsymbol{y} - \boldsymbol{x}\_0 \Vert^2\;\; \forall \boldsymbol{x} \in S$

#### Seperating Hyperplane

<blockquote>
给定集合 $S_1, S_2$，如果存在 hyperplane $\boldsymbol{a}^T\boldsymbol{x} = b$ 满足 $\boldsymbol{a}^T\boldsymbol{x} \geq b \; \forall x \in S_1,\;\boldsymbol{a}^T\boldsymbol{x} \leq b \; \forall x \in S_2$，则 $\boldsymbol{a}^T\boldsymbol{x} = b$ 称为 $S_1, S_2$ 的 seperating hyperplane。
</blockquote>

* 如果条件变为 $\boldsymbol{a}^T\boldsymbol{x} > b \; \forall x \in S_1,\;\boldsymbol{a}^T\boldsymbol{x} < b \; \forall x \in S_2$，则称为 strictly seperate

* 如果条件变为 $\boldsymbol{a}^T\boldsymbol{x} > b + \varepsilon \; \forall x \in S_1 \; \forall \varepsilon \geq 0,\;\boldsymbol{a}^T\boldsymbol{x} \leq b \; \forall x \in S_2$，则称为 strongly seperate

另外，根据上面给出的两个 convex set 定理，给定一个 closed convex set $S$ 和点 $\boldsymbol{y} \notin S$，一定存在一个 hyperplane $\boldsymbol{a}^T\boldsymbol{x} = b$ 能 seperate $\boldsymbol{y}$ 和 $S$。因为 $(\boldsymbol{y} - \boldsymbol{x}_0)^T(\boldsymbol{x} - \boldsymbol{x}_0) \leq 0 \;\; \forall \boldsymbol{x} \in S$，所以只要令 $\boldsymbol{a} = \boldsymbol{y} - \boldsymbol{x}_0, b = \boldsymbol{a}^T \boldsymbol{x}\_0$，就能使得 $\boldsymbol{a}^T\boldsymbol{x} \leq b \; \forall \boldsymbol{x} \in S$ 同时 $\boldsymbol{a}^T \boldsymbol{y} \geq b$。

#### Cone

<blockquote>
给定集合 $C$，如果给定任一 $\boldsymbol{x} \in C$ 都有 $\lambda \boldsymbol{x} \in C \; \forall \lambda \in \mathbb{R}$，则 $C$ 被称为 Cone
</blockquote>

* Example. 一条直线是一个 cone，两条相交的直线也是一个 cone

#### Farkas' Lemma

<blockquote>
令 $A \in \mathbb{R}^{m\times n}, \boldsymbol{c} \in \mathbb{R}^n$，则下面两个结论有且只有一个是成立的 <br/>
1. $\exists \boldsymbol{x} \in \mathbb{R}^n \;\;s.t.\;\; A\boldsymbol{x} \leq \boldsymbol{0}, \boldsymbol{c}^T \boldsymbol{x} > 0$<br/>
2. $\exists \boldsymbol{y} \in \mathbb{R}^m \;\;s.t.\;\; A^T\boldsymbol{y} = \boldsymbol{c}, \boldsymbol{y} \geq \boldsymbol{0}$
</blockquote>

