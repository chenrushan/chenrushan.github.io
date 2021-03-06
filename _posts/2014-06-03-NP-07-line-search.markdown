---
layout: post
title: 07 - Line Search Technique
categories: nnumop
tags: NPTEL, numerical optimization
---

这一节回答上一节最后提出的几个问题

### Stopping Conditions

前面提到利用 $g(\b{x}^k) = 0$ 只能确定 $\b{x}^k$ 是个 stationary point，必须再根据 $H(\b{x}^k)$ 的性质才能确定 $\b{x}^k$ 是否为真的 local minimum，但在实际中由于计算和判断 $H(\b{x}^k)$ 涉及的计算资源较多，所以通常只利用 $g(\b{x}^k)$ 来作为 stopping condition，并且也不是判断 $g(\b{x}^k)$ 是否等于 $0$，由于计算机的精度问题，通常这个判断是很难成立的。

实际中常用的 stopping condition 包括

* $\Vert g(\b{x}^k) \Vert \leq \varepsilon$

* $\frac{f(\b{x}^k) - f(\b{x}^{k+1})}{|f(\b{x}^k)|} \leq \varepsilon$

其中 $\varepsilon$ 是一个用户指定的很小的数，第一个条件就是 $g(\b{x}^k) = 0$ 的一个近似，第二个条件表示当前轮的迭代是否能使 $f(\b{x}^k)$ 有显著下降，如果没有，则停止迭代

### Speed of Convergence

<blockquote>
假设优化过程对应 sequence $\{\b{x}^k\}_{k \geq 0}$，$\b{x}^*$ 为 local minimum，如果下式成立

$$\lim_{k\rightarrow \infty} \frac{\Vert \b{x}^{k+1} - \b{x}^*\Vert }{\Vert \b{x}^k - \b{x}^*\Vert^p} = \beta \;\; \beta < \infty$$

则 $p$ 表示 order of convergence，$\beta$ 表示 convergence rate
</blockquote>

注意到这里的分子分母都是表示离最优点的距离，所以上面的定义是用距离的比值来表示 convergence 的快慢

* $p = 1, 0 < \beta < 1$ (linear convergence)

    * $\beta = 0.1, \Vert \b{x}^0 - \b{x}^* \Vert = 0.1$

        收敛过程是 $10^{-1}, 10^{-2}, 10^{-3}, 10^{-4}, ...$

    * $\beta = 0.9, \Vert \b{x}^0 - \b{x}^* \Vert = 0.1$

        收敛过程是 $10^{-1}, 0.09, 0.081, 0.0729, ...$

    可以看到 $\beta$ 越小，收敛越快

* $p = 2, \beta > 0$ (quadratic convergence)

    * $\beta = 1, \Vert \b{x}^0 - \b{x}^* \Vert = 0.1$

        收敛过程是 $10^{-1}, 10^{-2}, 10^{-4}, ...$

    可以看出 quadratic 的收敛过程比 linear 要快得多

* superlinear convergence

    如果收敛过程符合如下条件

    $$\lim_{k\rightarrow \infty} \frac{\Vert \b{x}^{k+1} - \b{x}^* \Vert}{\Vert \b{x}^k - \b{x}^\* \Vert} = 0, \lim_{k\rightarrow \infty} \frac{\Vert \b{x}^{k+1} - \b{x}^\* \Vert}{\Vert \b{x}^k - \b{x}^\* \Vert^2} = \infty$$

    这被称为 superlinear convergence，收敛速度介于 linear 和 quadratic 之间
  
由于 linear convergence 收敛得慢，而 quadratic convergence 虽然收敛快但是需要的资源太多，所以大多数算法都是属于 superlinear convergence

另一种表示 convergence rate 的方法是使用 Error function $E: \mathbb{R}^n \rightarrow \mathbb{R}$，然后计算

$$\lim_{k\rightarrow \infty} \frac{E(\b{x}^{k+1}) - E(\b{x}^*)}{(E(\b{x}^k) - E(\b{x}^\*))^p}$$
或者
$$\lim_{k\rightarrow \infty} \frac{E(\b{x}^{k}) - E(\b{x}^{k+1})}{E(\b{x}^k)^p}$$

通常情况下，使不使用 Error function 并不影响 convergence rate，一个 linear convergence 的算法不会因为用 Error function 计算 convergence rate 而变成 quadratic convergence 算法。

### Step Length

假设 $\b{d}^k$ 已经确定，求解 step length $\alpha^k$ 的方法分为两种，分别是 Exact line search 和 Inexact line search。

#### Exact line search

把 $\alpha^k$ 的求解当成是另一个优化问题，即在每一步迭代过程中再求解

$$\alpha^k = \min_{\alpha} f(\b{x}^k + \alpha \b{d}^k)$$

由于 $\alpha$ 是个 scalar，所以这是一个一维优化问题。

#### Inexact line search

Exact line search 有时会带来性能上的问题，这时就需要使用近似的方法，不过在使用近似的方法时需要注意以下几点

* $\alpha^k$ 不能太大，太大函数值反而上升
* $\alpha^k$ 不能太小，太小则函数值的变化太小，收敛也慢
* 函数值下降相对于 $\alpha^k$ 要比较显著，函数值下降不一定要求绝对值很大，但应该相对于 $\alpha^k$ 是显著的，换句话说，就是 rate of decrease 要比较大

为了保证以上 3 点就有了 Armijo's condition, Goldstein's condition 和 Wolfe's condition

假设 $f(\b{x}^k + \alpha \b{d}^k)$ 的函数图像是这样 (其中 $\alpha$ 是变量)

<object data="/resource/NNP/07-line-search/f_alpha.svg" type="image/svg+xml" class="blkcenter"></object>

图中有两条虚线

* 横虚线的函数是 $y = f(\b{x}^k)$，即 $f(\b{x}^k + \alpha \b{d}^k)$ 在 $\alpha  = 0$ 的取值
* 斜虚线的函数是 $y = f(\b{x}^k) + \alpha g^T(\b{x}^k)\b{d}^k$，即 $f(\b{x}^k + \alpha \b{d}^k)$ 在 $\alpha  = 0$ 处的切线

$g^T(\b{x}^k)\b{d}^k < 0$ 所以 $f$ 在 $\alpha = 0$ 处一定是往下走的

下面分别讨论这 3 种 condition

<p style="background-color: #9f9">Armijo's condition</p>

Armijo's condition 给出下面的绿色虚线，由于其斜率介于 $0$ 和 $g^T(\b{x}^k)\b{d}^k$ 之间，所以可以将斜率值定义为 $c_1 g^T(\b{x}^k)\b{d}^k \; c_1 \in (0, 1)$

<object data="/resource/NNP/07-line-search/amijo.svg" type="image/svg+xml" class="blkcenter"></object>

Armijo's condition 要求 $\alpha^k$ 满足 $f(\b{x}^k + \alpha^k \b{d}^k) < f(\b{x}^k) + c_1 \alpha^k g^T(\b{x}^k)\b{d}^k$

这个条件一来保证了 $\alpha^k$ 不会太大，因为上述条件保证了函数值一定是下降的；二来保证了 rate of decrease 不会太小，因为 $\frac{f(\b{x}^k) - f(\b{x}^k + \alpha^k \b{d}^k)}{\alpha^k} > c_1 g^T(\b{x}^k)\b{d}^k$，其中 $g^T(\b{x}^k)\b{d}^k$ 为最大可能的 rate of decrease。

<p style="background-color: #9f9">Goldstein's condition</p>

Goldstein's condition 给出下面的红色虚线，由于其斜率介于 $0$ 和 $g^T(\b{x}^k)\b{d}^k$ 之间，所以可以将斜率值定义为 $c_2 g^T(\b{x}^k)\b{d}^k \; c_2 \in (0, 1)$

<object data="/resource/NNP/07-line-search/goldstein.svg" type="image/svg+xml" class="blkcenter"></object>

Goldstein's condition 要求 $\alpha^k$ 满足 $f(\b{x}^k + \alpha^k \b{d}^k) > f(\b{x}^k) + c_2 \alpha^k g^T(\b{x}^k)\b{d}^k$，这样 $\alpha$ 就必须大于 $\hat{\alpha}$，这个条件保证了 step length 不会太小

通常 Goldstein's condition 和 Armijo's condition 一起使用，这样就同时满足了前面提出的 3 个要求，在这种情况下，$c_2$ 的取值范围是 $(c_1, 1)$

<p style="background-color: #9f9">Wolfe's condition</p>

Wolfe's condition 的作用和 Goldstein's condition 是一样的，都是要保证 step length 不会太小，只是用的方法不一样，Wolfe's condition 通过限制 $\alpha^k$ 处的函数斜率来保证的。如下图中给出的斜虚线，假设其斜率有 $c g^T(\b{x}^k)\b{d}^k \; c\in (0, 1)$

<object data="/resource/NNP/07-line-search/wolfe.svg" type="image/svg+xml" class="blkcenter"></object>

Wolfe's condition 要求 $\alpha^k$ 满足 $f'(\b{x}^k + \alpha^k \b{d}^k) > c g^T(\b{x}^k) \b{d}^k$，这样符合条件的 $\alpha$ 就只能是 $(\hat{\alpha}_1, \hat{\alpha}_2) \cup (\hat{\alpha}_3, +\infty)$，也就保证了 step length 不会太小
    
Wolfe's condition 的含义是这样的，$f'(\b{x}^k + \alpha^k \b{d}^k)$ 表示的是 $f(\b{x}^k + \alpha^k \b{d}^k)$ 在 $\alpha^k$ 处的 gradient，如果 gradient 是个很大的 negative number，则我们可以推测 $f$ 在这个 $\alpha^k$ 处还有很大的下降空间，因此我们不能满足于停留在这样的 $\alpha^k$ 上，可以继续扩大 $\alpha^k$。相反，如果 gradient 是个很小的 negative number 或者是个正数，那我们的 line search 就要停止了，上面的不等式中 $c g^T(\b{x}^k) \b{d}^k$ 就是表示我们可以接受的某个比较小的 negative number

同样 Wolfe's condition 也通常和 Armijo's condition 一起使用

#### Backtrack line search

Backtrack line search 虽然独立一小节出来，但它本质也是一种 inexact line search，它是 inexact line search 在具体实现上的一种 trick，它通过 Armijo condition 来保证 rate of decrease，然后以 backtract 的方式来保证 step length 不会太小，参考如下伪代码

<blockquote>
INPUT: $\hat{\alpha} \in (0, +\infty), c_1 \in (0, 1), \lambda \in (0, 1)$<br/><br/>

$\alpha^k = \hat{\alpha}$ <br/>
WHILE $f(\b{x}^k + \alpha^k \b{d}^k) > f(\b{x}^k) + c_1 \alpha^k g^k \b{d}^k$ <br/>
&nbsp;&nbsp;&nbsp;&nbsp;$\alpha^k = \lambda \alpha^k$<br/><br/>

OUTPUT: $\alpha^k$
</blockquote>

可以看到，代码其实是非常简单的，每一轮迭代都按固定的比例缩减 step length，直到满足 Armijo condition 为止，所以等于说它找到了一个尽可能最大的满足 Armijo condition 的 step length。

### Proof of Convergence

在证明前先做几个假设，令 $f^k = f(\b{x}^k), g^k = f'(\b{x}^k)$，假设

* $f$ is bounded below，否则优化就没有结果了
* 确定 step length 用的是 Armijo-Wolfe condition
* $g^k$ is lipschitz continuous
* $g^k$ 和 $\b{d}^k$ 严格成钝角

----------------

* 证明

    <p style="background-color: #9f9">首先每一步迭代符合 Armijo condition 所以有</p>

    $$
    \begin{align*}
    f^k < & f^{k-1} + c_1 \alpha^{k-1} {g^{k-1}}^T \b{d}^{k-1} \;\; c_1 \in (0, 1) \\\\
    < & f^0 + \sum_{i=0}^{k-1} c_1 \alpha^i {g^i}^T \b{d}^i \\\\
    \end{align*}
    $$

    上式等价于 $ - \sum_{i=0}^{k-1} c_1 \alpha^i {g^i}^T \b{d}^i < f^0 - f^k$，由于 $f$ bounded below，所以有 $f^0 - f^\infty < \infty$，因此有

    $$ - \sum_{i=0}^{\infty} c_1 \alpha^i {g^i}^T \b{d}^i < \infty$$

    首先明确不等式左边是个正数，因为 $c_1 > 0, \alpha_i > 0, -{g^i}^T \b{d}^i >= 0$，所以 sum 的每个元素都大于等于 0，而无限个这样的数相加能 $< \infty$，唯一的可能就是当 $i$ 大于某个数后，$c_1 \alpha^i g^i \b{d}^i = 0$

    <p style="background-color: #9f9">由于 $g^k$ lipschitz continuous，所以有</p>

    $$ \Vert g^k - g^{k-1} \Vert \leq L \Vert \b{x}^k - \b{x}^{k-1} \Vert  = L \alpha^{k-1} \Vert \b{d}^{k-1} \Vert \;\; L \geq 0 $$

    不等式两边同乘以 $\Vert \b{d}^{k-1} \Vert$ 有

    $$ (g^k - g^{k-1})^T \b{d}^{k-1} \leq \Vert g^k - g^{k-1} \Vert \Vert \b{d}^{k-1} \Vert \leq L \alpha^{k-1} {\b{d}^{k-1}}^T \b{d}^{k-1}$$

    因此有

    $$\alpha^{k-1} \geq \frac{(g^k - g^{k-1})^T \b{d}^{k-1}}{L {\b{d}^{k-1}}^T \b{d}^{k-1}}$$

    <p style="background-color: #9f9">由于每一步迭代又满足 Wolfe condition，所以有</p>

    $${g^{k}}^T \b{d}^{k-1} \geq c_2 {g^{k-1}}^T \b{d}^{k-1} \;\; c_2 \in (c_1, 1)$$

    两边同减去 ${g^{k-1}}^T\b{d}^{k-1}$ 得 $(g^k - g^{k-1})^T \b{d}^{k-1} \geq (c_2 - 1) {g^{k-1}}^T \b{d}^{k-1}$

    结合第二步推导得到的不等式，有

    $$\alpha^{k-1} \geq \frac{(c_2 - 1) {g^{k-1}}^T \b{d}^{k-1}}{L {\b{d}^{k-1}}^T \b{d}^{k-1}}$$

    不等式两边同乘以 $-c_1 {g^{k-1}}^T \b{d}^{k-1}$ 有

    $$-c_1 \alpha^{k-1} {g^{k-1}}^T \b{d}^{k-1} \geq \frac{c_1(1 - c_2) ({g^{k-1}}^T \b{d}^{k-1})^2}{L {\b{d}^{k-1}}^T \b{d}^{k-1}} = \frac{c_1(1 - c_2)}{L} \Vert g^{k-1} \Vert^2 \cos^2\theta$$

    结合第一步得到的不等式有

    $$\sum_i \frac{c_1(1 - c_2)}{L} \Vert g^i \Vert^2 \cos^2\theta < \infty$$ 

    其中 $\frac{c_1(1 - c_2)}{L} > 0, \cos^2\theta > 0$，因此 $\lim_{i\rightarrow \infty} \Vert g^i \Vert = 0$

因此在上述假设成立的情况下，算法是收敛的，当然上述假设不是必要条件了，这里只是给出一个证明的例子

### Descent Direction

所有的 descent direction 都可以表示为 $\b{d}^k = -A^k g^k$，因为 $\b{d}^k$ 和 $g^k$ 是一个空间内的向量，给定一个，另一个总可以通过旋转伸缩来得到，也就是矩阵乘的方式 (不要纠结于那个负号)。

之前我们提到所有满足 ${g^k}^T \b{d}^k < 0$ 的方向都是 descent direction，把 $\b{d}^k$ 的表示代入有 $-{g^k}^T A^k g^k < 0$，即要求 $A^k$ 是 positive definite matrix。

所有的优化算法最核心的不同就在于如何构建 matrix $A^k$，详情请见后续章节。

