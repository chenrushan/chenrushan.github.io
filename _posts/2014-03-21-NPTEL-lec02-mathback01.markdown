---
layout: post
title: Lec02 - Mathematical Background 1
categories: nnumop
tags: NPTEL, numerical optimization
---

------------------------

Difference between two sets A and B: $A \setminus B = \\{x: x \in A \;\; and \;\; x \notin B\\}$

------------------------

**Supremum**

<blockquote>
The smallest possible real number $y$ satisfying $x \leq y$ for every $x \in A$. Denoted as $\sup \{x : x \in A\}$.
</blockquote>

**Infimum**
<blockquote>
The greatest possible real number $y$ satisfying $x \geq y$ for every $x \in A$. Denoted as $\inf \\{x : x \in A\\}$.
</blockquote>

For example:

$A = \\{x: 1 \leq x \lt 3\\}$

* $\sup\\{x : x \in A\\} = 3 (\notin A)$

* $\inf\\{x : x \in A\\} = 1 (\in A)$

------------------------

**Vector Space**:

<blockquote>
A nonempty set $S$ is called a vector space if

<ul>
<li>For any $\boldsymbol{x}, \boldsymbol{y} \in S$, $\boldsymbol{x} + \boldsymbol{y}$ is defined and is in $S$. Further,</li>

$$\boldsymbol{x} + \boldsymbol{y} = \boldsymbol{y} + \boldsymbol{x} \;\; \text{(commutativity)}$$
$$\boldsymbol{x} + (\boldsymbol{y} + \boldsymbol{z}) = (\boldsymbol{x} + \boldsymbol{y}) + \boldsymbol{z} \;\; \text{(associativity)}$$

<li>There exists an element in $S$, $\boldsymbol{0}$, such that $\boldsymbol{x} + \boldsymbol{0} = \boldsymbol{0} + \boldsymbol{x}$ for all $\boldsymbol{x}$.</li>

<li>For any $\boldsymbol{x} \in S$, there exists $\boldsymbol{y} \in S$, such that $\boldsymbol{x} + \boldsymbol{y} = \boldsymbol{0}$.</li>

<li>For any $\boldsymbol{x} \in S$ and $\alpha \in \mathbb{R}$, $\alpha \boldsymbol{x}$ is defined and is in $S$, Further,</li>

$$\boldsymbol{1}\boldsymbol{x} = \boldsymbol{x} \;\; \forall \boldsymbol{x}$$

<li>For any $\boldsymbol{x}, \boldsymbol{y} \in S$ and $\alpha, \beta \in \mathbb{R}$,</li>

$$\alpha(\boldsymbol{x} + \boldsymbol{y}) = \alpha \boldsymbol{x} + \alpha \boldsymbol{y}$$
$$(\alpha + \beta)\boldsymbol{x} = \alpha \boldsymbol{x} + \beta \boldsymbol{x}$$
$$\alpha(\beta \boldsymbol{x}) = \alpha \beta \boldsymbol{x}$$
</ul>
</blockquote>

Elements in S are called **vector**.

-----------------------

**Notations**:

<blockquote>
<li> $\mathbb{R}$: vector space of real numbers</li>
<li> $\mathbb{R}^n$: vector space of real $n \times 1$ vectors</li>
<li> n-vector $\boldsymbol{x}$ is an array of n scalars, $x_1, x_2, ..., x_n$</li>
<li> $\boldsymbol{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$</li>
<li> $\boldsymbol{x}^T = (x_1, x_2, ..., x_n)$</li>
<li> $\boldsymbol{0}^T = (0, 0, ..., 0)$</li>
<li> $\boldsymbol{1}^T = (1, 1, ..., 1)$ (We also use $\boldsymbol{e}$ to denote this vector)</li>
</blockquote>

-----------------------

**Vector Subspace**:

<blockquote>
If $S$ and $T$ are vector spaces such that $S \subseteq T$, then $S$ is called a subspace of $T$.
</blockquote>

All possible subspaces of $\mathbb{R}^2$ are $\mathbb{R}^2$, $\\{(0, 0)\\}$, and $\\{(x\_1, x\_2): a x\_1 + b x\_2 = 0, a \in \mathbb{R}, b \in \mathbb{R}, a^2 + b^2 \neq 0\\}$ (which means all lines going through $(0, 0)$).

$\\{(x\_1, x\_2): a x\_1 + b x\_2 = c, a \in \mathbb{R}, b \in \mathbb{R}, a^2 + b^2 \neq 0, c \neq 0\\}$ is called affine space.

-----------------------

**Spanning Set**:

<blockquote>
A set of vectors $\boldsymbol{x}_1, \boldsymbol{x}_2, ..., \boldsymbol{x}_k$ is said to span the vector space $S$ if any vector $\boldsymbol{x} \in S$ can be represented as:
$$\boldsymbol{x} = \sum_{i=1}^{k}\alpha_i \boldsymbol{x}_i \;\; \alpha_i \in \mathbb{R}$$
</blockquote>

-----------------------

**Linear Independence**:

<blockquote>
A set of vectors $\boldsymbol{x}_1, \boldsymbol{x}_2, ..., \boldsymbol{x}_k$ is said to linearly independent if
$$\sum_{i=1}^{k} \alpha_i \boldsymbol{x}_i = 0 \Rightarrow \alpha_i = 0 \;\; \forall i$$
Otherwise, they are linearly dependent, and one of them is linear combination of the others.
</blockquote>

For example, $(1, 0)$ and $(1, 1)$ are linearly independent, while $(1, 0)$ and $((-1, 0))$ are not.

-----------------------

**Basis**

<blockquote>
A set of vectors is said to be a basis for the vector space $S$ if it is linearly independent and spans $S$.
</blockquote>

For example, $\\{(1, 0), (1, 1)\\}$ spans $\mathbb{R}^2$.

Properties of basis:

1. A vector space does not have a unique basis.
2. If $\boldsymbol{x}\_1, \boldsymbol{x}\_2, ..., \boldsymbol{x}\_k$ is a basis for $S$, then any $\boldsymbol{x} \in S$ can be uniquely represented using $\boldsymbol{x}\_1, \boldsymbol{x}\_2, ..., \boldsymbol{x}\_k$.
3. Any two basis of a vector space have the same cardinality.
4. Let $\boldsymbol{e}\_i$ denote an n-dimensional vector whose i-th element is 1 and the remaining elements are 0's. Then, the set $\boldsymbol{e}\_1, \boldsymbol{e}\_2, ..., \boldsymbol{e}\_n$ forms a standard basis for $\mathbb{R}^n$.
5. A basis for the vector space $S$ is a maximal independent set of vectors which spans the space $S$.
6. A basis for the vector space $S$ is a minimum spanning set of vectors which spans the space $S$.

Property 2 can be easily proved by contradiction.

**Dimension of Vector Space**

<blockquote>
The dimension of the vector space $S$ is the cardinality of a basis of $S$.
</blockquote>

The dimension of $\mathbb{R}^n$ is $n$.

-----------------------

**Function**

<blockquote>
A function $f$ from a set $A$ to a set $B$ is a rule that assigns to each $x$ in $A$ a unique element $f(x)$ in $B$. This function can be represented by
$$f:A\rightarrow B$$
</blockquote>

Note:

* $A$: Domain of $f$
* $\\{y \in B: \exists x[y = f(x)] \\}$: Range of f
* Range of $f \subseteq B$

-----------------------

**Norm**

<blockquote>
A norm on $\mathbb{R}^n$ is real-value function $\Vert \cdot \Vert: \mathbb{R}^n \rightarrow \mathbb{R}$ which obeys
<ul>
<li>$\Vert \boldsymbol{x} \Vert \geq 0$ for every $\boldsymbol{x} \in \mathbb{R}^n$, and $\Vert \boldsymbol{x} \Vert = 0$ iff $\boldsymbol{x} = 0$.</li>
<li>$\Vert \alpha \boldsymbol{x} \Vert = |\alpha|\Vert \boldsymbol{x} \Vert$ for every $\boldsymbol{x} \in \mathbb{R}^n$ and $\alpha \in \mathbb{R}$.</li>
<li>$\Vert \boldsymbol{x} + y\Vert \leq \Vert \boldsymbol{x} \Vert + \Vert y \Vert$ for every $\boldsymbol{x} \in \mathbb{R}^n$ and $y \in \mathbb{R}^n$.</li>
</ul>
</blockquote>

<object data="/resource/NNP/norm.svg" type="image/svg+xml" class="blkcenter"></object>

Let $\boldsymbol{x} \in \mathbb{R}^n$. Some popular norms:

* $L\_2$ or Euclidean norm: $\Vert \boldsymbol{x} \Vert\_2 = (\sum\_{i=1}^{n} (x\_i)^2)^{\frac{1}{2}}$

  <object data="/resource/NNP/l2norm.svg" type="image/svg+xml" class="blkcenter"></object>

* $L\_1$ norm: $\Vert \boldsymbol{x} \Vert\_1 = \sum\_{i=1}^{n} |x\_i|$

  <object data="/resource/NNP/l1norm.svg" type="image/svg+xml" class="blkcenter"></object>

* $L\_{\infty}$ norm: $\Vert \boldsymbol{x} \Vert\_{\infty} = \underset{i=1,\cdots,n}{\max} |x\_i|$
