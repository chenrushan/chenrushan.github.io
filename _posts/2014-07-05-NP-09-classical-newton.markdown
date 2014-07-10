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

这样我们就实现了通过空间变换得到一个 Hessian matrix 为 $I$ 的 quadratic function。在 $h(\boldsymbol{y})$ 应用 steepest descent 有 (令 $\alpha = 1$)

$$ \boldsymbol{y}^{k+1} = \boldsymbol{y}^k - \nabla h(\boldsymbol{y}^k) = \boldsymbol{y}^k - (\boldsymbol{y}^k - L^{-1}\boldsymbol{c}) = L^{-1}\boldsymbol{c}$$

所以无论你从什么初始点开始，都是一步到达 global minimum，把这个点映射回 x-space，得 
$$\boldsymbol{x}^{k+1} = L^{-T}L^{-1} \boldsymbol{c} = H^{-1}\boldsymbol{c}$$

这就是在 x-space 的最优解。

----------

如果我们将 y-space 的迭代步骤映射到 x-space 的话是这样

$$
\begin{align}
& \boldsymbol{y}^{k+1} = \boldsymbol{y}^k - \nabla\_{\boldsymbol{y}^k} h(\boldsymbol{y}^k) \\\\
\Longleftrightarrow & L^{-T}\boldsymbol{y}^{k+1} = L^{-T}\boldsymbol{y}^k - L^{-T}\nabla\_{\boldsymbol{y}^k} f(L^{-T} \boldsymbol{y}^k) \\\\
\Longleftrightarrow & \boldsymbol{x}^{k+1} = \boldsymbol{x}^k - L^{-T} L^{-1} \nabla f(\boldsymbol{x}^k) \\\\
\Longleftrightarrow & \boldsymbol{x}^{k+1} = \boldsymbol{x}^k - H^{-1} \nabla f(\boldsymbol{x}^k) \\\\
\end{align}
$$

这最后一步实际上就是 Classical Newton 的迭代步骤。这里说的好像 Classical Newton 是由 Steepest Descent 演化过来似的，实际上，二者的发明并没有什么联系，并且 Classical Newton 出现比 Steepest Descent 还要早得多，下面一节我们看看 Classical Newton 是基于什么思想得到的。

#### Classical Newton Method

Classical Newton 真正基于的思想是在每步迭代的过程中对函数做 quadratic approximation，也就是用二阶 taylor series 去近似 $f(\boldsymbol{x})$

$$f(\boldsymbol{x}) \approx f(\boldsymbol{x}^k) + g^T(\boldsymbol{x}^k)(\boldsymbol{x} - \boldsymbol{x}^k) + \frac{1}{2} (\boldsymbol{x} - \boldsymbol{x}^k)^T H(\boldsymbol{x}^k) (\boldsymbol{x} - \boldsymbol{x}^k)$$

然后通过优化这个近似函数去得到 $\boldsymbol{x}^{k+1}$，为了方便，后面以 $\boldsymbol{g}^k$ 表示 $g(\boldsymbol{x}^k)$，以 $H^k$ 表示 $H(\boldsymbol{x}^k)$。

优化这个 quadratic approximation 并不复杂，令其导数为 0 即 $\boldsymbol{g}^k + H^k (\boldsymbol{x} - \boldsymbol{x}^k) = 0$ 可得

$$\boldsymbol{x}^{k+1} = \boldsymbol{x}^k - {H^{k}}^{-1} \boldsymbol{g}^k$$

之前已经说过每步迭代的 descent direction 可以表示为 $\boldsymbol{d}^k = -A^k \boldsymbol{g}^k$，对于 Classical Newton，$A^k = {H^{k}}^{-1}$，另外注意到，传统的 Classical Newton 并不设 step length，也就是 step length 统一设为 1，当然你也可以在每步做 line search。

下图给出 Rosenbrock function $f(\boldsymbol{x}) = 100(\boldsymbol{x}\_2 - \boldsymbol{x}\_1^2)^2 + (1 - \boldsymbol{x}\_1)^2$ 在点 $(-0.5, 0)$ 处的 quadratic approximation，其中红点表示 $(-0.5, 0)$，绿色的 contour 就是 quadratic approximation 对应的 contour

  <img style="width:60%" src="/resource/NNP/09-newton/rosen3.png" />

#### Examples

还用 steepest descent 中给出的例子

##### $f(\boldsymbol{x}) = (\boldsymbol{x}\_1 - 7)^2 + (\boldsymbol{x}\_2 - 2)^2$ 和 $f(\boldsymbol{x}) = 4\boldsymbol{x}\_1^2 + \boldsymbol{x}\_2^2 -2\boldsymbol{x}\_1\boldsymbol{x}\_2$

对于这两个 case，无论你初始点设在哪里，Classical Newton 都是一步即可收敛

##### $f(\boldsymbol{x}) = 100(\boldsymbol{x}\_2 - \boldsymbol{x}\_1^2)^2 + (1 - \boldsymbol{x}\_1)^2$

其最优值出现在 (1, 1) 点，利用 Classical Newton + backtrack line search ($\hat{\alpha} = 1, \lambda = 0.3, c\_1 = 1\times 10^{-4}$)

* 初始点为 (0.6, 0.6)，收敛过程如下图所示，以 0.001 为 gradient norm 的阈值，共迭代 10 步

  <img style="width:80%" src="/resource/NNP/09-newton/rosen1.png" />

* 初始点为 (-1.2, 1)，收敛过程如下图所示，以 0.001 为 gradient norm 的阈值，共迭代 21 步

  <img style="width:80%" src="/resource/NNP/09-newton/rosen2.png" />

----------

从这几例子可以看出，对比 steepest descent，Classical Newton 收敛所需的步数要少了很多。

