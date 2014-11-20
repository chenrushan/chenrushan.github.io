---
layout: post
title: MCMC and Gibbs Sampling
categories: ml
tags: MCMC, Gibbs sampling
---

#### Why Sampling

假设我们要计算如下形式的 expectation

$$ E(f) = \int f(x) p(x) dx $$

有些时候这个积分有 closed-form solution，但很多时候这样的 solution 是不存在的，这时候我们就需要对 $x$ 根据 $p(x)$ 做 sampling，假设我们 sample 出 N 个样本，则可以对 $E(f)$ 做如下近似

$$ E(f) \approx \frac{1}{N} \sum\_{i=1}^{N} f(x\_i) $$

同样的对于离散分布的变量

$$ E(f) = \sum\_{x} f(x)p(x) $$

我们可能由于 $x$ 的空间太大而无法穷举所有可能的 $x$，这时候同样也需要做 sampling

#### How to Sample

通常的编程环境都我们提供了一个随机函数，这个函数可以产生符合 uniform distribution 的 sample，但我们实际中需要对各种各样的 distribution 做 sample，因此我们就需要从这个简单的 uniform 的 sampler 出发构建符合任意 distribution 的 sampler。下面我们先看几个简单的 distribution

##### Sampling from Discrete Distribution

假设 random variable $X$ 的取值范围为 $\\{x^1, x^2, \cdots, x^k\\}$，$P(x^i) = \theta\_i$，$\sum\_i \theta\_i = 1$

对这样的 distribution 可以这么 sample，对 $[0, 1]$ 区间进行如下划分

<object data="/resource/gibbs/disc.svg" type="image/svg+xml" class="blkcenter"></object>

然后利用前面提到的 uniform sampler 得到一个 $[0, 1]$ 间的随机值 $r$，如果 $r \in [\sum\_{i=0}^{k}\theta\_i, \sum\_{i=0}^{k+1}\theta\_i]$ (令 $\theta\_0 = 0$)，则我们得到的 sample 就是 $X = x^{k+1}$

##### Forward Sampling from a Bayesian Network

考虑如下图所示的 Bayesian Network

<object data="/resource/gibbs/BN.svg" type="image/svg+xml" class="blkcenter"></object>

其中每个变量都是离散变量

对这样的 Bayesian Network，sample 可以按照 topological order 进行

* 首先对 $A$ 按 $P(A)$ 进行 sample

* 然后对 $B$ 按 $P(B)$ 进行 sample

* 然后对 $C$ 按 $P(C|A, B)$ 进行 sample

* 然后对 $D$ 按 $P(D|B)$ 进行 sample

* 然后对 $E$ 按 $P(E|C)$ 进行 sample

这样我们就得到了一个完整的对应于这个 Bayesian Network Distribution 的 sample。由于这里每个分布都是 discrete distribution，所以上述每一个步骤都可以按前面给出的 Sampling from Discrete Distribution 的方式进行

有了这个 sample 算法，我们就可以预测比如 $P(B = b)$

* 首先根据上述算法 sample 出 N 个样本

* 然后计算 $P(B = b) \approx N\_{B = b}/N$

----------

上面我们看到了两种简单的 sample 方式，但有很多分布没法用这样的简单方式进行，或者用这样的方式做不好，比如

* BN 中某些变量为 observed variable 的情况下的分布

    针对上面的 Bayesian Netwrok，假设我们要预测是个条件概率，如 $P(B = b | A = a)$，等价于限定 $A$ 为 observed variable，针对这种情况，一种做法是还按 Forward Sampling 的方式 sample 出 N 个样本，然后丢弃掉其中不包含 $A = a$ 的样本 (这样的 sampling 也被称为 Rejection Sampling)，然后计算

    $$ P(B = b | A = a) = \frac{N\_{B = b, A = a}}{N\_{A = a}} $$

    这样做的问题是所有 sample 出的 N 个样本，只留下了其中的 ${N\_{A = a}}$ 个，为了使 ${N\_{A = a}}$ 足够大，我们就需要扩大 $N$，也就是 sample 更多的样本。如果我们进一步扩大 observed variables 的个数，比如要预测的是 $P(B = b | A = a, C = c, D = d, E = e, F = f)$，问题会越发严重，你可能已经 sample 了一大堆的样本，却没有一个包含 $A = a, C = c, D = d, E = e, F = f$

    因此对于包含 observed variable 的 BN Distribution，Forward Sampling 不是一个很好的 sample 算法

* Markov Network Distribution

    Markov Network 没法用 Forward Sampling 的方式 sample，因为 Markov Network 是 undirected graph，你没法定义所谓 topological order

* Intractable Distribution

    通常一个 Markov Network Distribution 可以表示为

    $$p(\boldsymbol{x}) = \frac{e^{-E(\boldsymbol{x})}}{Z}$$

    其中 $Z$ 为 normalization constant，有时候这个 $Z$ 没有一个高效的方法去求解，或者压根没法求解，这时候你也没法用一个简单的方法去 sample

针对上面 3 种情况，我们需要用稍微复杂点的 sample 算法，MCMC 就是其中一种

#### Markov Chain Monte Carlo (MCMC)

<blockquote>
MCMC 的基本思想是，既然有些 distribution 不好直接进行 sample，那我就构造一个逼近这个 target distribution 的 Markov Chain，利用这个 Markov Chain 进行 sample
</blockquote>

以下定义几个 Markov Chain 相关的变量

* 令 $x^{(t)}$ 表示 Markov Chain 第 $t$ 步状态，$x^{(t)} \in \\{x\_1, x\_2, \cdots, x\_n\\}$

* 令 $P$ 表示 transition matrix，$P\_{ij} = P(x\_j | x\_i)$

* 令 $\mu^{(t)}$ 表示 $x^{(t)}$ 对应的 distribution，$\mu^{(t)}$ 是个 vector，其元素之和为 1，如 $\mu^{(t)} = (0.2, 0.6, 0.2)^T$

    给定初始状态 $\mu^{(1)}$，$\mu^{(t)}$ 可以表示为

    $$ {\mu^{(t)}}^T = {\mu^{(1)}}^T P^t$$

* 令 $\mu$ 表示 Markov Chain 的 stationary distribution

* 令 $\pi$ 表示我们要 sample 的 target distribution

其中指定了 $x^{(t)}$ 的状态空间和 $P$ 也就确定了一个 Markov Chain，为了能用某一 Markov Chain 进行 sample，这一 Markov Chain 必须要能收敛，并且收敛的 stationary distribution 要等于 target distribution

##### Markov Chain 收敛条件

当 $P$ 满足以下两个性质时，$\mu^{(t)}$ 会收敛到 $\mu$

1. Irreducibility. 也就是从任何一个状态开始都能以某一不为零的概率到达任何一个其他状态

2. Aperiodicity. 定义参考 [wikipedia](http://en.wikipedia.org/wiki/Markov_chain#Periodicity)

举个例子，假设一个 Markov Chain 包含 3 个状态 $\\{x\_1, x\_2, x\_3\\}$，其 transition matrix 为

$$P = \begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0.1 & 0.9 \\\\ 0.6 & 0.4 & 0 \end{pmatrix}$$

(Example from [1])，假设初始分布为 $(0.5, 0.2, 0.3)^T$，则每一步 distribution 的变化如下图所示

<object data="/resource/gibbs/tran.svg" type="image/svg+xml" class="blkcenter"></object>

最后分布会收敛到 $(0.22, 0.41, 0.37)^T$，(文章 [1] 中说收敛到 $(0.2, 0.4, 0.4)^T$，我自己写了个程序跑了一下是 $(0.22, 0.41, 0.37)^T$)，其实无论你以什么分布做为初始分布，最后都会收敛这个分布

##### Detailed Balance Condition

上面给出 Markov Chain 收敛的条件，这里给出 Markov Chain 收敛到 $\pi$ 的条件

如果 Markov Chain 满足

$$ \pi(x\_i)P\_{ij} = \pi(x\_j)P\_{ji} $$

则 Markov Chain 会收敛到 $\pi$，注意这个条件是 sufficient condition

##### Sampling

假设我们现在有了一个收敛到 target distribution 的 Markov Chain，做 sampling 的过程是这样，以 $S^{(t)}$ 表示第 t 步得到的样本，$S^{(t)} \in \\{x\_1, x\_2, \cdots, x\_n\\}$

<blockquote class="blkcode">
Sample $S^{(1)}$ according to $u^{(1)}$<br/>
Sample $S^{(2)}$ according to $P(\cdot | S^{(1)})$<br/>
... ...<br/>
Sample $S^{(t)}$ according to $P(\cdot | S^{(t - 1)})$<br/>
... ...<br/>
</blockquote>

但不是所有得到的样本都是可用的，因为一开始样本服从的分布与 target distribution 通常相差较大，因此只有迭代了一段时间后得到的样本才是可用的，下面的小节介绍怎样判断当前样本是否可用

##### Mixing

如果当前状态服从的分布和 target distribution 足够接近，我们就称这个 Markov Chain 已经 mix 了。Markov Chain mix 之后，当前及后续 sample 得到的样本就可以当成是来自 target distribution 的样本加以使用

不幸的是，直接判断当前状态的分布是否和 target distribution 足够接近并不容易。退而求其次，我们去判断 Markov Chain 是否已经收敛，如果收敛，我们就认为当前状态的分布与 target distribution 已经比较接近。判断的方法是选取连续的多个 window，看看在这些 window 中 sample 的分布是否比较接近，如果比较接近，则认为 Markov Chain 已经收敛，否则继续迭代。下图给出根据 Markov Chain sample 出的 N 个样本以及两个 window，window 的 size 为 $t$

<object data="/resource/gibbs/converge.svg" type="image/svg+xml" class="blkcenter"></object>

但这种判断是有缺点的，因为 Markov Chain 可能是在状态空间的一个局部游走，通过判断连续的几个 window 也会得出分布比较相近的结论，但这时 Markov Chain 可能远没有收敛。一种解决办法是，使用多个 Markov Chain，每个 Markov Chain 用不同的初始分布，这样如果多个 Markov Chain 的最后一个 window 对应的 sample distribution 比较接近，则可以认为 Markov Chain 收敛了，并且其分布接近于 target distribution


#### Gibbs Sampling

在上一节中，我们讨论了如何利用 Markov Chain 做 sample，但并没有说到如何构建这样的 Markov Chain。这一节中要说的 Gibbs Sampling 就是具体构造 Markov Chain 的一个例子，其应用主要针对 PGM (Probabilistic Graphical Model) Distribution

首先定义几个变量

* 令 $\boldsymbol{X} = (X\_1, X\_2, \cdots, X\_N)$ 表示对应某个 Graph 的随机变量序列，其中 $X\_i$ 对应 Graph 中不同的 node，$X\_i \in \Lambda$，$\boldsymbol{X} \in \Lambda^N$

* 令 $\boldsymbol{X}\_{-i}$ 表示 $\boldsymbol{X}$ 中除了 $X\_i$ 以外的其他变量，即 $\boldsymbol{X}\_{-i} = \\{X\_j | j \neq i\\}$

* 令 $\pi(\boldsymbol{X})$ 表示 $X$ 的 joint distribution

----------

Gibbs Sampling 这么定义 Markov Chain

* 每个状态表示一个完整的 Graph 的取值，因此每个状态是个向量，状态空间为 $\Lambda^N$

* 如果 $\boldsymbol{x}, \boldsymbol{y}$ 为两个不同的状态，则由 $\boldsymbol{x}$ 向 $\boldsymbol{y}$ 转移的概率 $P\_{\boldsymbol{xy}}$ 按如下方式定义

    * 如果 $\boldsymbol{x}, \boldsymbol{y}$ 中有两个或两个以上节点不同，则
        
        $$P\_{\boldsymbol{xy}} = 0$$

    * 如果 $\boldsymbol{x}, \boldsymbol{y}$ 中仅有一个节点不同，则 
        $$P\_{\boldsymbol{xy}} = q(i) \pi(y\_i | \boldsymbol{x}\_{-i})$$
        
        其中 $q(i)$ 表示 node $X\_i$ 被选择的概率，$\pi(y\_i | \boldsymbol{x}\_{-i})$ 表示选中 $X\_i$ 后，其值变为 $y\_i$ 的概率

    * 如果 $\boldsymbol{x} = \boldsymbol{y}$，则
    
        $$P\_{\boldsymbol{xy}} = \sum\_{i=1}^{N} q(i) \pi(x\_i | \boldsymbol{x}\_{-i})$$

    可以验证，按照上述方式定义 $P\_{\boldsymbol{xy}}$，则有 $\sum\_{\boldsymbol{y}} P\_{\boldsymbol{xy}} = 1$

----------

易于证明这样定义的 Markov Chain 满足 Irreducibility 和 Aperiodicity 两个性质，同时通过证明 $\pi(x) P\_{\boldsymbol{xy}} = \pi(y) P\_{\boldsymbol{yx}}$ (按上面的定义分 3 种情况证明，参考 [2]) 可以知道该 Markov Chain 会收敛到 joint distribution $\pi(\boldsymbol{X})$

实际使用的时候，通常不定义分布 $q(i)$，而是按照一个固定的顺序去选择每次 update 的 node，比如每次都从 $X\_1$ 按顺序 update 到 $X\_N$，sample 一个样本包含 N 次状态转换，比如我们要 sample k 个样本，可以这么做

<blockquote class="blkcode">
initialize $\boldsymbol{x}^{(0)}$<br/>

for t = 0 to k-1:<br/>
&nbsp;&nbsp;sample $\boldsymbol{x}^{(t+1)}_1$ according to $\pi(x_1|x^{(t)}_2, \cdots, x^{(t)}_N)$<br/>
&nbsp;&nbsp;sample $\boldsymbol{x}^{(t+1)}_2$ according to $\pi(x_2|x^{(t+1)}_1, x^{(t)}_3, \cdots, x^{(t)}_N)$<br/>
&nbsp;&nbsp;... ...<br/>
&nbsp;&nbsp;sample $\boldsymbol{x}^{(t+1)}_N$ according to $\pi(x_N|x^{(t+1)}_1, x^{(t+1)}_2, \cdots, x^{(t+1)}_{N-1})$<br/>
&nbsp;&nbsp;collect new sample $\boldsymbol{x}^{(t+1)}$
</blockquote>

可以看到，Gibbs Sampling 每次迭代根据条件概率做 sample，因此这个条件概率肯定不能是 intractable distribution

#### Reference

1. [An Introductio to MCMC for Machine Learning](http://www.cs.princeton.edu/courses/archive/spr06/cos598C/papers/AndrieuFreitasDoucetJordan2003.pdf)
2. [An Introductio to Restricted Boltzman Machine](http://image.diku.dk/igel/paper/AItRBM-proof.pdf)
3. [Sampling Methods](https://class.coursera.org/pgm/lecture)

