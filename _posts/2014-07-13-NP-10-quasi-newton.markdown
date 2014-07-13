---
layout: post
title: 10 - Quasi Newton Method
categories: nnumop
tags: NPTEL, numerical optimization, quasi newton
---

前一篇文章中提到了 Classical Newton 的诸多问题，针对这些问题有了 Quasi Newton Method，Quasi Newton 指的是一类算法，其基本思想是在每步迭代的时候不直接计算 Hessian matrix $H^k$，而是得到它的一个近似，假设以 $B^k$ 表示，这样每步迭代时优化的并且这一近似
