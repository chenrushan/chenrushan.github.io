---
layout: post
title: Gradient for Neural Network
categories: ml
tags: backpropagation, neural network
---

这篇笔记给出利用 backpropagation 算法计算 neural network 的 gradient，主要包含 3 个部分的内容

1. Single training sample 情况下 nerual network 的 gradient 求解
2. Batch 情况下 nerual network 的 gradient 求解
3. 考虑了 Softmax Output + Cross Entroy Loss 情况下公式的推导

### Gradient for Single Training Sample

Single Training Sample 情况下 nerual network 的 graident 可用如下 4 个公式计算

$$ \delta^L = \nabla\_a C \odot \sigma'(z^L) \tag{BP1} $$
$$ \delta^l = (w^{l+1} \delta^{l+1}) \odot \sigma'(z^l) \tag{BP2} $$
$$ \frac{\partial C}{\partial b^l} = \delta^l \tag{BP3} $$
$$ \frac{\partial C}{\partial w^l} = a^{l-1} {\delta^l}^T \tag{BP4} $$

(BP4) 应用于第一个 hidden layer 时，$a^{l-1}$ 等于 neural network 的输入

其中 $\odot$ 表示两个向量或矩阵间的 elementwise product。$z^l, a^l, \sigma'(z^l), \nabla\_a C, \delta^l, b^l$ 都是 (column) vector，每个元素对应当前 layer 的一个 neuron，$w^l$ 是个 matrix。这些 vector, maxtix 中的元素的意义分别是

* $z\_j^l = \sum\_k w\_{kj}^l a\_k^{l - 1} + b\_j^l$: 第 $l$ 层第 $j$ 个 neuron 的 pre-activation
* $a\_j^l = \sigma(z^l\_j)$: 第 $l$ 层第 $j$ 个 neuron 的 activation，$\sigma$ 是 activation function
* $(\sigma'(z^l))\_j$: 第 $l$ 层第 $j$ 个 neuron 的 activation 相对于 pre-activation 的导数
* $(\nabla\_a C)\_j$: Cost function 相对 output layer 第 $j$ 个 neuron 的 activation 的导数
* $\delta^l\_j = \frac{\partial C}{\partial z\_j^l}$: Cost function 相对于 $z\_j^l$ 的导数
* $b\_j^l$: 第 $l$ 层第 $j$ 个 neuron 的 bias
* $w\_{kj}^l$: 第 $l-1$ 层的第 $k$ 个 neuron 到第 $l$ 层的第 $j$ 个 neuron 的边的 weight

<blockquote>
有些人用 $w^l_{jk}$ 表示第 $l-1$ 层的第 $k$ 个 neuron 到第 $l$ 层的第 $j$ 个 neuron 的边的 weight，其实两种表示方法区别只是在用 $w$ 矩阵时是否 transpose
</blockquote>

----------

下面给出这 4 个公式的推导

* BP1

    BP1 的推导非常简单，就是简单复合函数的求导

    $$ \delta\_j^L = \frac{\partial C}{\partial z\_j^L} = \frac{\partial C}{\partial a\_j^L} \frac{\partial a\_j^L}{\partial z\_j^L}$$

    <blockquote>
    这里有个地方值得注意，就是如果 output layer 用了 Softmax activation，那计算 $\delta_j$ 其实需要 sum 所有的 $a_j$。所以其实我一直有个疑问，Softmax 到底能不能算 activation function，因为通常我们看到 activation function 都只依赖与当前 neuron 的 pre-activation 输出，而 Softmax 却要依赖所有的。一种对待这个问题的方法是，如果 output layer 用了 Softmax，那我可以认为 activation function 是空，也就是 activation 的结果等于 pre-activation (${\partial a_j^l}/{\partial z_j^l} = 1$)，而 Softmax 是 cost function 的一部分，这样上面这个计算 $\delta_j^L$ 的式子依然成立，同时这样实现程序也简单一些
    </blockquote>

* BP2

    首先 $C$ 是 $z^{l+1}$ 的函数 $C = f(\cdots, z\_{j}^{l+1}, \cdots)$，而 $z^{l+1}$ 又是 $a^l$ 的函数 $z\_j^{l+1} = g(\cdots, a\_k^{l}, \cdots)$，因此

    $$ \frac{\partial C}{\partial z\_k^l} = \frac{\partial C}{\partial a\_k^l} \frac{\partial a\_k^l}{\partial z\_k^l} = (\sum\_j \frac{\partial C}{\partial z\_j^{l+1}} \frac{\partial z\_j^{l+1}}{\partial z\_k^{l}}) \sigma'(z\_k^l) = (\sum\_j \delta^{l+1}\_j w^{l+1}\_{kj}) \sigma'(z\_k^l) $$

    如果你按矩阵的形式组织一下这个式子就是上面的 BP2 了

* BP3

    $$ \frac{\partial C}{\partial b\_j^l} = \frac{\partial C}{\partial z\_j^l} \frac{\partial z\_j^l}{\partial b\_j^l} = \delta^l\_j $$

    用矩阵表示即为 (BP3)

* BP4

    $$ \frac{\partial C}{\partial w\_{kj}^l} = \frac{\partial C}{\partial z\_j^l} \frac{\partial z\_j^l}{\partial w\_{kj}^l} = \delta^l\_j a^{l-1}\_k $$

    用矩阵表示即为 (BP4)

----------

上面这些公式的核心，我觉得就是 $\delta^l$ 这个变量的定义，因为这个变量，整个 backpropagation 算法相关的公式变得十分的简洁

### Batch Gradient

上面给出的 4 个公式用于求解一个 training sample 的 gradient，对于不同的 sample，其对应的 $C$ 是不一样的，它们 share 相同的 $w$ 和 $b$，但由于 sample 不同，所以每个 sample 对应的 $C, z^l\_j, a^l\_j$ 等形式都不一样，下面我们看看当给定一个 batch 时，gradient 怎么求。以下以 $C\_x, z^l\_{x,j}, a^l\_{x,j}$ 分别表示 sample $x$ 对应的 cost, pre-activation, activation，则有

$$ C = \frac{1}{m}\sum\_{x \in batch} C\_x$$

其中 $m$ 表示 batch 中 sample 的个数。所以你可以把 $C$ 看成是一个复合函数，它是 $C\_x$ 的复合函数，也是 $z\_{x,j}^l, a\_{x,j}^l$ 的复合函数，这样就有

$$ \frac{\partial C}{\partial b^l\_j} = \sum\_x \frac{\partial C}{\partial z\_{x,j}^l} \frac{\partial z\_{x,j}^l}{\partial b\_j^l} = \frac{1}{m}\sum\_x \delta^l\_{x,j} \boldsymbol{\Longrightarrow} \frac{\partial C}{\partial b^l} = \frac{1}{m}\sum\_x \delta^l\_x $$

$$ \frac{\partial C}{\partial w\_{kj}^l} = \sum\_x \frac{\partial C}{\partial z\_{x,j}^l} \frac{\partial z\_{x,j}^l}{\partial w\_{kj}^l} = \frac{1}{m}\sum\_x \delta^l\_{x,j} a^{l-1}\_{x,k} \boldsymbol{\Longrightarrow} \frac{\partial C}{\partial w^l} = \frac{1}{m}\sum\_x a^{l-1}\_x {\delta^l\_x}^T $$

因此为了计算 gradient，我们就需要 batch 中所有 sample 的 $a^l$ 和 $\delta^l$，实际实现中，我们不会针对 batch 中的每个 sample 挨个去算，而是将所有的 sample 放到一个 matrix 中，直接对整个 batch 做计算

直接对 batch 做计算和对一个 sample 做计算其实是一样的，一个 sample 是一个 column vector，一个 batch 不过就是多个 column vector 而已，所以改为 batch 后，那 4 个 BP 公式几乎都还是一样的，如下

$$ \boldsymbol{\delta^L} = \boldsymbol{\nabla\_a C} \odot \boldsymbol{\sigma'(z^L)} \tag{BP1b} $$
$$ \boldsymbol{\delta^l} = (w^{l+1} \boldsymbol{\delta^{l+1}}) \odot \boldsymbol{\sigma'(z^l)} \tag{BP2b} $$
$$ \frac{\partial C}{\partial b^l} = \frac{1}{m}\boldsymbol{\delta^l}\boldsymbol{1} \tag{BP3b} $$
$$ \frac{\partial C}{\partial w^l} = \frac{1}{m}\boldsymbol{a^{l-1}} {\boldsymbol{\delta^l}}^T \tag{BP4b} $$

这里用粗体标识出那些本来是 column vector 现在变成 matrix 的变量，可以看出来公式的形式并没有多大变化，不同的就两个地方，一个是 (BP3b) 中有个 $\boldsymbol{1}$，表示所有元素都为 1 的 vector，一个是多了 $1/m$ (这个 $1/m$ 在具体实现的时候再 $\nabla\_a C$ 这个阶段做，这样可以不用每层都做这个计算，同时也可以让你的 nerual network 的实现不用和具体的 batch size 有关)

所以输入从一个 column vector 变为 n 个 column vector 后，你也只要将迭代中相关的本来是一个 column 的变为 n 个 column 即可

总结一下这里面涉及的矩阵和向量行列的意义

<blockquote>
<ul>
<li>$\boldsymbol{\delta^L, \; \nabla_a C, \; \sigma'(z^L), \; \delta^l, \; a^{l-1}}$ 这几个 matrix 的一个 column 对应 batch 中的一个 sample，column 中的每个元素对应 layer 中的一个 neuron，所以 number of rows 等于 layer size，number of columns 等于 batch size</li>
<li>$w^l$ 这个 matrix 对应第 $l-1$ 层到第 $l$ 层之间的链接的权重，row index 对应输入，column index 对应输出</li>
<li>$b^l$ 这个 vector 对应第 $l$ 层的 bias</li>
<li>$\boldsymbol{1}$ 这个 vector 行数等于 batch 中的 sample 个数</li>
</ul>
</blockquote>

### $\delta^L$ for Softmax Output + Cross Entroy Loss

下面给出当 output layer 的 activation function 为 softmax，同时 lost function 为 cross entropy 情况下 $\delta^L$ 的表达式，这种搭配在分类任务中很常见

* cross entropy 表示为 (这里只考虑一个 training sample 的情况)

    $$ C = - \sum\_{j = 1}^n t\_j \log a^L\_j $$

    其中 $n$ 表示 output neuron 个数，$t\_j$ 表示 true label，对于 1-of-n 编码，$t\_j$ 只有一个为 1，其余都为 0

* softmax 的表达式为

    $$ a^L\_i = \frac{\exp(z^L\_i)}{\sum\_{j = 1}^n \exp(z^L\_j)} $$

    其导数有很好的形式

    $$ \frac{\partial a^L\_i}{\partial z^L\_j} = a^L\_i(I\_{ij} - a^L\_j) $$

    其中 $I$ 为 identity matrix，所有 off-diagonal 项都为 0，diagonal 项都为 1

综合上述两个公式有

$$
\begin{align}
\frac{\partial C}{\partial z^L\_i} = & \sum\_{j = 1}^n \frac{\partial C}{\partial a^L\_j} \frac{\partial a^L\_j}{\partial z^L\_i} \\\\
= & \sum\_{j = 1}^n \frac{t\_j}{a^L\_j} a^L\_j(I\_{ji} - a^L\_i) \\\\
= & \sum\_{j = 1}^n t\_j (I\_{ji} - a^L\_i) \\\\
= & a^L\_i - t\_i
\end{align}
$$

最后一个式子是因为对于所有的 $I\_{ij}$ 只有 $i = j$ 时 $I\_{ij} = 1$，所以 $\sum\_j t\_j I\_{ji} = t\_i$，而对于另一部分 $\sum\_j t\_j a^L\_i = a^L\_i \sum\_j t\_j = a^L\_i$

这样就有

$$ \delta^L = a^L - t $$

最终形式非常简洁，而且很好理解，相当于当前输出与目标之间的差异。对于 batch 的输入，改变也很简单，就是将 $a^L, t$ 都变成包含 m 个 column 的 matrix 即可，$m$ 表示 batch size

### References

1. [How the backpropagation algorithm works](http://neuralnetworksanddeeplearning.com/chap2.html)
