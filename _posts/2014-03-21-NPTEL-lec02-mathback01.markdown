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

  <object data="/resource/NNP/linfnorm.svg" type="image/svg+xml" class="blkcenter"></object>

In general, $L\_p$ norm is defined as $\Vert \boldsymbol{x} \Vert\_{p} = (\sum\_{i=1}^{n} |x\_i|^p)^{\frac{1}{p}}$.

<blockquote>
If $\Vert \cdot \Vert_p$ and $\Vert \cdot \Vert_q$ are any two norms on $\mathbb{R}^n$, then there exist positive constants $\alpha$ and $\beta$ such that

$$\alpha \Vert \boldsymbol{x} \Vert_p \leq \Vert \boldsymbol{x} \Vert_q \leq \beta \Vert \boldsymbol{x} \Vert_p$$

for any $\boldsymbol{x} \in \mathbb{R}^n$
</blockquote>

So the convergece of an optimization algorithm does not depend on what norm its stopping criterion used.

-----------------------

**Inner Product**

<blockquote>
Let $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$ and $\boldsymbol{x} \neq \boldsymbol{0} \neq \boldsymbol{y}$. The inner or dot product is defined as

$$\boldsymbol{x} \cdot \boldsymbol{y} \equiv \boldsymbol{x}^T \boldsymbol{y} = \sum_{i=1}^{n} x_i \cdot y_i = \Vert \boldsymbol{x} \Vert \cdot \Vert \boldsymbol{y} \Vert \cos \theta$$

where $\theta$ is the angle between $\boldsymbol{x}$ and $\boldsymbol{y}$.
</blockquote>

Note:

* $\boldsymbol{x}^T \boldsymbol{x} = \Vert \boldsymbol{x} \Vert ^2$
* $\boldsymbol{x}^T \boldsymbol{y} = \boldsymbol{y}^T \boldsymbol{x}$
* $|\boldsymbol{x} \cdot \boldsymbol{y}| \leq \Vert \boldsymbol{x}\Vert  \cdot \Vert \boldsymbol{y}\Vert$ (Cauthy-Schwartz inequality)

-----------------------

**Orthogonality**

<blockquote>
Let $\boldsymbol{x} \in \mathbb{R}^n$ and $\boldsymbol{y} \in \mathbb{R}^n$. $\boldsymbol{x}$ and $\boldsymbol{y}$ are said to perpendicular or orthogonal to each other if $\boldsymbol{x}^T \boldsymbol{y} = 0$.

Two subspaces $S$ and $T$ of the same vector space $\mathbb{R}^n$ are orthogonal if every vector $\boldsymbol{x} \in S$ is orthogonal to every vector $\boldsymbol{y} \in T$, i.e. $\boldsymbol{x}^T \boldsymbol{y} = 0 \;\; \forall \boldsymbol{x} \in S, \boldsymbol{y} \in T$.
</blockquote>

-----------------------

**Mutual Orthogonality**

<blockquote>
Vectors $\boldsymbol{x}_1, \boldsymbol{x}_2, \cdots, \boldsymbol{x}_k \in \mathbb{R}^n$ are said to be mutually orthogonal if $\boldsymbol{x}_i \cdot \boldsymbol{x}_j = 0$ for all $i \neq j$.
If, in addition, $\Vert \boldsymbol{x}_i \Vert = 1$ for every $i$, the set $\{ \boldsymbol{x}_1, \cdots, \boldsymbol{x}_k\}$ is said to be orthonormal.
</blockquote>

It's easy to show that if $\boldsymbol{x}\_1, \cdots, \boldsymbol{x}\_k$ are mutually orthogonal nonzero vectors, then they are linearly independent.

-----------------------

**Gram-Schmidt Procedure**

To produce an orthonormal basis with a given basis $\boldsymbol{x}\_1, \boldsymbol{x}\_2, \cdots, \boldsymbol{x}\_k \in \mathbb{R}^n$, we use Gram-Schmidt Procedure.

Given $\boldsymbol{x}\_1, \boldsymbol{x}\_2, \boldsymbol{x}\_3 \in \mathbb{R}^3$, to produce an orthonormal basis $\boldsymbol{y}\_1, \boldsymbol{y}\_2, \boldsymbol{y}\_3$.

* set $\boldsymbol{y}\_1 = \frac{\boldsymbol{x}\_1}{\Vert \boldsymbol{x}\_1 \Vert}$

* remove $\boldsymbol{x}\_2$'s component in the $\boldsymbol{y}\_1$ direction

  $$\boldsymbol{z}\_2 = \boldsymbol{x}\_2 - (\boldsymbol{x}\_2^T \boldsymbol{y}\_1)\boldsymbol{y}\_1$$

  now $\boldsymbol{z}\_2$ is orthogonal to $\boldsymbol{x}\_1$.

  set $\boldsymbol{y}\_2 = \frac{\boldsymbol{z}\_2}{\Vert \boldsymbol{z}\_2 \Vert}$

* remove $\boldsymbol{x}\_3$'s component in the $\boldsymbol{y}\_1$ and $\boldsymbol{y}\_2$ direction

  $$\boldsymbol{z}\_3 = \boldsymbol{x}\_3 - (\boldsymbol{x}\_3^T \boldsymbol{y}\_2)\boldsymbol{y}\_2 - (\boldsymbol{x}\_3^T \boldsymbol{y}\_1)\boldsymbol{y}\_1$$

  now $\boldsymbol{z}\_3$ is orthogonal to $\boldsymbol{x}\_1$ and $\boldsymbol{x}\_2$.

  set $\boldsymbol{y}\_3 = \frac{\boldsymbol{z}\_3}{\Vert \boldsymbol{z}\_3 \Vert}$

It's easy to extend this procedure to $\mathbb{R}^n$.

-----------------------

**Matrix**

* Diagonal Matrix: A square matrix $\Lambda$ such that $\Lambda\_{ij} = 0 \;\; i \neq j$.
* Identity Matrix: A diagonal matrix $I$ such that $I\_{ii} = 1 \;\; \forall i$.

-----------------------

**Rank**

Let $A \in \mathbb{R}^{m\times n}$.

<blockquote>
The subspace of $\mathbb{R}^m$, spanned by the column vectors of $A$ is called the column space of $A$. The subspace of $\mathbb{R}^n$, spanned by the row vectors of $A$ is called the row space of $A$.
</blockquote>

<blockquote>
Column Rank: The dimension of the column space.<br/>
Row Rank: The dimension of the row space.<br/>
The column rank of a matrix equals its row rank, and its common value is called the rank of $A$.
</blockquote>

* The rank of a matrix is 0 iff it's a zero matrix.

* Matrices with the smallest rank - rank one matrices

  Example:

  $$
  \begin{pmatrix} 3 & 1 & -1 \\\\ -3 & -1 & 1 \\\\ 6 & 2 & -2 \\\\ \end{pmatrix} =
  \begin{pmatrix} 1 \\\\ -1 \\\\ 2 \end{pmatrix} \begin{pmatrix} 3 & 1 & -1 \end{pmatrix} = \boldsymbol{u}\boldsymbol{v}^T
  $$

  Every matrix of rank one has the simplest form $A = \boldsymbol{u}\boldsymbol{v}^T$.

-----------------------

**Invertible**

<blockquote>
A square matrix $A$ is said to be invertible if there exists a matrix $B$ such that $AB = BA = I$. There's at most one such $B$ and is denoted by $A^{-1}$.
</blockquote>

* A product of invertible matrices is invertible and $(AB)^{-1} = B^{-1}A^{-1}$

* If $\det(A) \neq 0$, then $A$ is invertible. ($\det(A)$ denotes the determinant of matrix $A$)

* The matrix $Q$ is orthogonal if $Q^{-1} = Q^T$.

