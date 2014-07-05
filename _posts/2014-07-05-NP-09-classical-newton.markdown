---
layout: post
title: 09 - Classical Newton Method
categories: nnumop
tags: NPTEL, numerical optimization, classical newton
---

#### 改进 Steepest Descent

假设要优化的函数是 quadratic function $f(\boldsymbol{x}) = \frac{1}{2} \boldsymbol{x}^T H \boldsymbol{x} - \boldsymbol{c}^T \boldsymbol{x}$，其中 $H$ 是 symmetric positive definite matrix。

在 steepest descent 那篇文章中已经提到 $H$ 的 condition number 对收敛速度的影响非常大，condition number 越小，收敛得越快，当 $H = I$ 时收敛最快。由此产生的一个优化思路是，对原始 function 做空间变换，使其在新空间中的 Hessian matrix 为 $I$，然后在新空间中做优化，再将结果映射回原始空间，这样迭代就可以一步完成。

假设原始空间为 x-space，新空间为 y-space，则我们试图找到的变换是

$$ f(\boldsymbol{x}) = \frac{1}{2} \boldsymbol{x}^T H \boldsymbol{x} - \boldsymbol{c}^T \boldsymbol{x} \; \Rightarrow \; h(\boldsymbol{y}) = \frac{1}{2} \boldsymbol{y}^T \boldsymbol{y} - \boldsymbol{c}\_y^T \boldsymbol{y} $$

参考下图

<object data="/resource/NNP/09-newton/transform.svg" type="image/svg+xml" class="blkcenter"></object>

由于这里 $H$ 是 symmetric positive definite matrix，这个变换可以通过对 $H$ 做 Cholesky decomposition 实现，如下

$$ f(\boldsymbol{x}) = \frac{1}{2} \boldsymbol{x}^T H \boldsymbol{x} - \boldsymbol{c}^T \boldsymbol{x} = \frac{1}{2} \boldsymbol{x}^T L L^T \boldsymbol{x} - \boldsymbol{c}^T \boldsymbol{x} = \frac{1}{2} (L^T \boldsymbol{x})^T (L^T \boldsymbol{x}) - \boldsymbol{c}^T \boldsymbol{x} $$

令 $\boldsymbol{y} = L^T \boldsymbol{x}$，则有

$$ h(\boldsymbol{y}) = \frac{1}{2} \boldsymbol{y}^T \boldsymbol{y} - (L^{-1} \boldsymbol{c})^T \boldsymbol{y} $$

这样我们就实现了通过空间变换得到一个 Hessian matrix 为 $I$ 的 quadratic function。在 $h(\boldsymbol{y})$ 应用 steepest descent 有

$$ \boldsymbol{y}^{k+1} = \boldsymbol{y}^k - \nabla h(\boldsymbol{y}) = \boldsymbol{y}^k - (\boldsymbol{y} - L^{-1}\boldsymbol{c}) = L^{-1}\boldsymbol{c}$$

所以无论你从什么初始点开始，都是一步到达 global minimum，把这个点映射回 x-space，得 
$$\boldsymbol{x}^{k+1} = L^{-T}L^{-1} \boldsymbol{c} = H^{-1}\boldsymbol{c}$$

这就是在 x-space 的最优解。

----------

如果我们将 y-space 的迭代步骤映射到 x-space 的话是这样

$$
\begin{align}
& \boldsymbol{y}^{k+1} = \boldsymbol{y}^k - \nabla\_{\boldsymbol{y}^k} h(\boldsymbol{y}^k) \\\\
\Longleftrightarrow & L^{-T}\boldsymbol{y}^{k+1} = L^{-T}\boldsymbol{y}^k - L^{-T}\nabla\_{\boldsymbol{y}^k} f(L^{-T} \boldsymbol{y}^k) \\\\
\end{align}
$$
