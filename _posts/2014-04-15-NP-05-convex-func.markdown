---
layout: post
title: 05 - Convex Function
categories: nnumop
tags: NPTEL, numerical optimization
---

### Convex Function

<blockquote>
令 $C \in \mathbb{R}^n$ 为非空 convex set，函数 $f: C \rightarrow \mathbb{R}$，如果 $f$ 满足如下条件

$$ f(\lambda \b{x}_1 + (1 - \lambda) \b{x}_2) \leq \lambda f(\b{x}_1) + (1 - \lambda) f(\b{x}_2) \;\; \forall \lambda \in [0, 1], \b{x}_1,\b{x}_2 \in C $$

则函数 $f$ 称为 convex function
</blockquote>

注意 $C$ 是个 convex set，否则不能保证所有的 $\lambda \b{x}\_1 + (1 - \lambda)\b{x}\_2$ 都在 $C$ 内。

如果条件中 $\leq$ 变成 $<$，同时 $\lambda \in (0, 1)$ 则函数 $f$ 称为 strictly convex function。

Convex function 用下面的图表示最直观了

<object data="/resource/NNP/05-convex-func/convex_func.svg" type="image/svg+xml" class="blkcenter"></object>

Convex function 和 Concave function 是两个相对的概念，$f$ 如果是 concave function，$-f$ 就是 convex function；如果 $f$ 是 strictly concave function，$-f$ 就是 strictly convex function。

### Convex Programming Problem

所谓的 convex programming problem，就是指如下问题

$$
\begin{align\*}
\min f(\b{x}) \\\\
s.t. \b{x} \in C
\end{align\*}
$$

其中 $C$ 是 convex set，$f: C \rightarrow \mathbb{R}$ 为 convex function

<blockquote>
Convex programming 中每个 local minimum 都是 global minimum
</blockquote>

* 证明

    假设 local minimum 为 $\b{x}^\*$，根据 local minimum 的定义我们知道

    $$\b{x}^\* = \underset{\b{x} \in C \cap B(\b{x}^\*, \delta)}{\arg\min} f(\b{x}) $$

    参考下图，其中绿色的圈表示 $C \cap B(\b{x}^\*, \delta)$

    <object data="/resource/NNP/05-convex-func/localisglobal.svg" type="image/svg+xml" class="blkcenter"></object>

    假设 $\b{y} \in C \cap B(\b{x}^\*, \delta)$，$\b{z}$ 为 $LS(\b{x}^\*, \b{y})$ 延长线上任意一点且在 $C$ 内，则 $\b{y}$ 可以表示为 $\lambda \b{x} + (1 - \lambda) \b{z} \; \lambda \in (0, 1)$，则有

    $$
    f(\b{x}^\*) \leq f(\b{y}) = f(\lambda \b{x}^\* + (1 - \lambda) \b{z}) \leq \lambda f(\b{x}^\*) + (1 - \lambda) f(\b{z})
    $$

    这也就推出 $f(\b{x}^\*) \leq f(\b{z})$

<blockquote>
Convex programming 的所有 global minimum 构成一个 convex set
</blockquote>

通俗的讲就是如果一个 convex programming problem 有多个最优解，那这些最优解必然是在一块的，不是分散的，如下图所示

<object data="/resource/NNP/05-convex-func/many_global.svg" type="image/svg+xml" class="blkcenter"></object>

其中最优解是连在一起的。

* 证明

    假设 $\b{x}\_1, \b{x}\_2$ 为 local minimum

    $$
    f(\lambda \b{x}\_1 + (1 - \lambda) \b{x}\_2) \leq \lambda f(\b{x}\_1) + (1 - \lambda) f(\b{x}\_2) = f(\b{x}\_1)
    $$

    这里不等号不能成立，所以 $\forall \lambda \in [0, 1] \; \lambda \b{x}\_1 + (1 - \lambda) \b{x}\_2$ 也都是 local minimum

### Epigraph

给定 $f: X \rightarrow \mathbb{R}$，其对应的 epigraph 是集合 $\\{ (\b{x}, y) : \b{x} \in X, y \geq f(\b{x})\\}$，所以 epigraph 属于 $\mathbb{R}^{n+1}$，参考下图，其中填充的部分就是 epigraph，当然 epigraph 是无限延伸的，这里只给出了其中的一部分而已。

<object data="/resource/NNP/05-convex-func/epigraph.svg" type="image/svg+xml" class="blkcenter"></object>

<blockquote>
给定 $C \in \mathbb{R}^n$ 为 convex set，$f: C \rightarrow \mathbb{R}$ 为 convex function 当且仅当其对应的 epigraph 为 convex set
</blockquote>

* 证明

    * convex function $\Rightarrow$ epigraph 为 convex set

        简单，略过

    * epigraph 为 convex set $\Rightarrow$ convex function

        利用 $(\b{x}\_1, f(\b{x}\_1)), (\b{x}\_2, f(\b{x}\_2)) \in$ epigraph 的性质即可证得

与 epigraph 相对的一个概念是 hypograph，hypograph 是这样的集合 $\\{ (\b{x}, y) : \b{x} \in X, y \leq f(\b{x})\\}$

### Level Set

Level set 是这么一个集合 $C\_{\alpha} = \\{ \b{x} \in C : f(\b{x}) \leq \alpha, \alpha \in \mathbb{R} \\}$

如果 $f(\b{x})$ 是 convex function 则 $C\_{\alpha}$ 是一个 convex set (证明简单)，反之不成立，比如对于 $f(x) = x^3$，它的 level set 就是 convex set，但是函数并不是 convex function。

有了 level set 的定义，就可以进一步细化 convex programming problem 的定义，通常 convex programming problem 都有如下形式

$$
\begin{align\*}
& \min \; f(\b{x}) \\\\
s.t. & h\_i(\b{x}) \leq 0 \;\; i = 1 \rightarrow m \\\\
& \b{a}^T\_j \b{x} + b\_j = 0 \;\; j = 1 \rightarrow l \\\\
\end{align\*}
$$

其中 $f$ 和 $h\_i$ 都是 convex function。这里每个约束都是一个 level set，根据前面性质可知，这些 level set 都是 convex set，而 convex set 的交集也是 convex set。

### Convexity and Gradient

<blockquote>
假设 $C \subset \mathbb{R}^n$ 是 convex set，函数 $f: C \rightarrow \mathbb{R}$ 一阶连续可导，令 $g(\b{x}) = \nabla f(\b{x})$，则 $f$ 是 convex function 当且仅当

$$f(\b{x}_2) \geq f(\b{x}_1) + g^T(\b{x}_1)(\b{x}_2 - \b{x}_1)$$

对于所有 $\b{x}_1, \b{x}_2 \in C$ 都成立。$f$ 是 strictly convex function 当且仅当不等号严格成立
</blockquote>

* 证明

    * Convexity $\Rightarrow$ 不等式成立

        Convexity 意味着 $f(\lambda \b{x}\_2 + (1 - \lambda)\b{x}\_1) \leq \lambda f(\b{x}\_2) + (1 - \lambda)f(\b{x}\_1) \; \lambda \in [0, 1]$，这个不等式等价于

        $$
        \begin{align\*}
        & f(\b{x}\_1 + \lambda (\b{x}\_2 - \b{x}\_1)) \leq f(\b{x}\_1) + \lambda(f(\b{x}\_2) - f(\b{x}\_1)) \\\\
        \Rightarrow & \frac{f(\b{x}\_1 + \lambda (\b{x}\_2 - \b{x}\_1)) - f(\b{x}\_1)}{\lambda} \leq f(\b{x}\_2) - f(\b{x}\_1)
        \end{align\*}
        $$

        取极限 $\lambda \rightarrow 0^+$，左边就是方向导数等于 $g^T(\b{x}\_1) (\b{x}\_2 - \b{x}\_1)$

    * 不等式成立 $\Rightarrow$ Convexity

        令 $\b{x} = \lambda \b{x}\_1 + (1 - \lambda)\b{x}\_2 \; \lambda \in [0, 1]$，不等式成立意味着

        $$
        \begin{align\*}
        f(\b{x}\_1) \geq f(\b{x}) + g^T(\b{x})(\b{x}\_1 - \b{x}) \\\\
        f(\b{x}\_2) \geq f(\b{x}) + g^T(\b{x})(\b{x}\_2 - \b{x})
        \end{align\*}
        $$

        则有

        $$
        \begin{align\*}
        & \lambda f(\b{x}\_1) + (1 - \lambda) f(\b{x}\_2) \\\\
        \geq & f(\b{x}) + \lambda g^T(\b{x})(\b{x}\_1 - \b{x}) + (1 - \lambda) g^T(\b{x})(\b{x}\_2 - \b{x}) \\\\
        = & f(\b{x}) + \lambda g^T(\b{x})(\b{x}\_1 - \b{x}\_2) + g^T(\b{x})(\b{x}\_2 - \b{x}) \\\\
        = & f(\b{x}) + g^T(\b{x})(\lambda \b{x}\_1 + (1 - \lambda)\b{x}\_2 - \b{x}) \\\\
        \end{align\*}
        $$

        由于 $\b{x} = \lambda \b{x}\_1 + (1 - \lambda)\b{x}\_2$，所以最后一个式子就是 $f(\lambda \b{x}\_1 + (1 - \lambda)\b{x}\_2)$

根据这个定理，如果存在 $\b{x}^\* \in C$ 使得 $g(\b{x}^\*) = 0$，则有 $f(\b{x}) \geq f(\b{x}^\*) \; \forall \b{x} \in C$，也就是 $\b{x}^\*$ 就是 minimum。

### Convexity and Hessian Matrix

<blockquote>
假设 $C \subset \mathbb{R}^n$ 是 open convex set，函数 $f: C \rightarrow \mathbb{R}$ 二阶连续可导，则 $f$ 是 convex function 当且仅当 $f$ 对应的 Hessian matrix 是 positive semi-definite matrix
</blockquote>

* 证明

    记 Hessian matrix 为 $H(\b{x})$

    * $H(\b{x})$ PSD $\Rightarrow$ $f$ is convex function 

        给定 $\b{x}\_1, \b{x}\_2 \in C$，根据 Truncated Taylor Series 有

        $$f(\b{x}\_2) = f(\b{x}\_1) + f'(\b{x}\_1)(\b{x}\_2 - \b{x}\_1) + \frac{1}{2} (\b{x}\_2 - \b{x}\_1)^T H(\b{x}) (\b{x}\_2 - \b{x}\_1)$$

        其中 $\b{x}$ 为 $\b{x}\_1, \b{x}\_2$ 之间的任意一点

        由于 $H(\b{x})$ PSD，所以 $(\b{x}\_2 - \b{x}\_1)^T H(\b{x}) (\b{x}\_2 - \b{x}\_1) \geq 0$，所以

        $$f(\b{x}\_2) \geq f(\b{x}\_1) + f'(\b{x}\_1)(\b{x}\_2 - \b{x}\_1)$$

        根据前面的定理可知，$f$ 为 convex function

    * $H(\b{x})$ is not PSD $\Ra$ $f$ is not convex

        假设 $H$ 在点 $\b{x}\_1$ 处为 negative definite，由于 $f \in \mathcal{C}^2$，
        所以存在某个区域 $B(\b{x}\_1, \delta)$，$\forall \b{x} \in B(\b{x}\_1, \delta)$，
        $H$ 为 negative definite，令 $\b{x}\_2 \in B(\b{x}\_1, \delta)$

        根据 Truncated Taylor Series 有

        $$f(\b{x}\_2) = f(\b{x}\_1) + f'(\b{x}\_1)(\b{x}\_2 - \b{x}\_1) + \frac{1}{2} (\b{x}\_2 - \b{x}\_1)^T H(\b{x}) (\b{x}\_2 - \b{x}\_1)$$

        其中 $\b{x}$ 为 $\b{x}\_1, \b{x}\_2$ 之间的任意一点，因此 $\b{x} \in
        B(\b{x}\_1, \delta)$，所以 $(\b{x}\_2 - \b{x}\_1)^T H(\b{x}) (\b{x}\_2 -
        \b{x}\_1) < 0$，这样

        $$f(\b{x}\_2) < f(\b{x}\_1) + f'(\b{x}\_1)(\b{x}\_2 - \b{x}\_1)$$

        因此 $f$ 不是 convex function $\EOP$

### Jensen's Inequality

<blockquote>
如果 $C \subseteq \mathbb{R}^n$ 是 convex set，$f: C \rightarrow \mathbb{R}$，则 $f$ 是 convex function 当且仅当

$$f(\sum_{i=1}^{k} \lambda_i \b{x}_i) \leq \sum_{i=1}^{k} \lambda_if(\b{x}_i)$$

其中 $\b{x}_1, ..., \b{x}_k \in C, \; \lambda_i \geq 0, \; \sum_i \lambda_i = 1$
</blockquote>

* 证明

    * 不等式成立 $\Rightarrow$ convexity

        这个简单，令 $k = 2$ 就是 convex function 的定义

    * Convexity $\Rightarrow$ 不等式成立 (用 Induction 的方式证明)

        $k \leq 2$ 时显然成立，就是 convex function 的定义，假设对于 $k - 1$ 的情况成立，对于 $k$ 的情况

        $$
        \begin{align\*}
        & f(\sum\_{i = 1}^k \lambda\_i \b{x}\_i) \\\\
        = & f(\sum\_{i = 1}^{k-1} \lambda\_i \b{x}\_i + \lambda\_k \b{x}\_k) \\\\
        = & f((1 - \lambda\_k)\sum\_{i = 1}^{k-1} \frac{\lambda\_i}{1 - \lambda\_k} \b{x}\_i + \lambda\_k \b{x}\_k) \\\\
        \leq & (1 - \lambda\_k)f(\sum\_{i = 1}^{k-1} \frac{\lambda\_i}{1 - \lambda\_k} \b{x}\_i) + \lambda\_k f(\b{x}\_k)
        \end{align\*}
        $$

        后面的推导简单就不写了

### Operations Preserving Convexity

假设 $f$ 是 convex function，则下面的操作依然能得到 convex function

1. $\alpha f \;\;\; \forall\alpha > 0$
2. $\sum\_i \alpha\_i f\_i \;\;\; \forall\alpha\_i > 0$

### Function Maximum 

<blockquote>
令 $C \subset \mathbb{R}^n$ 为一个 compact convex set，$f: C \rightarrow \mathbb{R}$ 为 convex function，则 $f$ 的最大值一定是出现在 C 的某一 boundary point
</blockquote>

