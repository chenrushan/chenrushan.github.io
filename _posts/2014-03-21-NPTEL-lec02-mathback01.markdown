---
layout: post
title: Lec02 - Mathematical Background 1
categories: nnumop
tags: NPTEL, numerical optimization
---

#### Supremum and Infimum of a set

* Supremum: The smallest possible real number $y$ satisfying $x \leq y$ for every $x \in A$.
 * $\sup\\{x : x \in A\\}$

* Infimum: The greatest possible real number $y$ satisfying $x \geq y$ for every $x \in A$.
 * $\inf\\{x : x \in A\\}$

Example: $A = \\{x: 1 \leq x \lt 3\\}$

* $\sup\\{x : x \in A\\} = 3 (\notin A)$

* $\inf\\{x : x \in A\\} = 1 (\in A)$

#### Vector Space

A nonempty set $S$ is called a **vector space** if

* For any $\boldsymbol{x}, \boldsymbol{y} \in S$, $\boldsymbol{x} + \boldsymbol{y}$ is defined and is in $S$. Further,

$$\boldsymbol{x} + \boldsymbol{y} = \boldsymbol{y} + \boldsymbol{x} \;\; \text{(commutativity)}$$
$$\boldsymbol{x} + (\boldsymbol{y} + \boldsymbol{z}) = (\boldsymbol{x} + \boldsymbol{y}) + \boldsymbol{z} \;\; \text{(associativity)}$$

* There exists an element in $S$, $\boldsymbol{0}$, such that $\boldsymbol{x} + \boldsymbol{0} = \boldsymbol{0} + \boldsymbol{x}$ for all $\boldsymbol{x}$.

* For any $\boldsymbol{x} \in S$, there exists $\boldsymbol{y} \in S$, such that $\boldsymbol{x} + \boldsymbol{y} = \boldsymbol{0}$.

* For any $\boldsymbol{x} \in S$ and $\alpha \in \mathbb{R}$, $\alpha \boldsymbol{x}$ is defined and is in $S$, Further,

$$\boldsymbol{1}\boldsymbol{x} = \boldsymbol{x} \;\; \forall \boldsymbol{x}$$

* For any $\boldsymbol{x}, \boldsymbol{y} \in S$ and $\alpha, \beta \in \mathbb{R}$,

$$\alpha(\boldsymbol{x} + \boldsymbol{y}) = \alpha \boldsymbol{x} + \alpha \boldsymbol{y}$$
$$(\alpha + \beta)\boldsymbol{x} = \alpha \boldsymbol{x} + \beta \boldsymbol{x}$$
$$\alpha(\beta \boldsymbol{x}) = \alpha \beta \boldsymbol{x}$$

Elements in S are called **vector**.

-----------------------

Notations:

* $\mathbb{R}$: vector space of real numbers
* $\mathbb{R}^n$: vector space of real $n \times 1$ vectors
* n-vector $\boldsymbol{x}$ is an array of n scalars, $x\_1, x\_2, ..., x\_n$
* $\boldsymbol{x} = \begin{pmatrix} x\_1 \\\\ x\_2 \\\\ \vdots \\\\ x\_n \end{pmatrix}$
* $\boldsymbol{x}^T = (x\_1, x\_2, ..., x\_n)$
* $\boldsymbol{0}^T = (0, 0, ..., 0)$
* $\boldsymbol{1}^T = (1, 1, ..., 1)$ (We also use $\boldsymbol{e}$ to denote this vector)

-----------------------

#### Misc

* Difference between two sets A and B: $A \setminus B = \\{x: x \in A \;\; and \;\; x \notin B\\}$

