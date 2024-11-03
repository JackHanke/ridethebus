# Formalism and Simplification of Round 2 Procedure

## Problem

Consider a permutation $\pi$ of $n$ elements. An observer is given the first element of the permutation $\pi_1$, and is tasked with predicting if $\pi_2$ is greater than $\pi_1$. If the prediction is correct, he is then tasked with predicting if $\pi_3$ is greater than $\pi_2$. This process continues with each successful prediction. If $\pi_n$ is correctly predicted, the observer repeats the task with a new permutation $\pi'$. If $\pi'_n$ is correctly predicted, the boserver repeats the task with a new permutation. This repeats until an incorrect prediction.   

The obserever has the knowledge that he is sampling from a permutation on $n$ elements, but does not know which permutation. He also has access to all sampled elements. What is the expected number of predictions the observer will get correct before an incorrect prediction, for a given $n$? 

## Solution

Let $X_n$ be the random variable representing the number of correct predictions before an incorrect prediction.

The process can also be thought of as making random hops from the ordered list $1$ to $n$, where one marks spots that have already been visited.

$\mathbb{P}(X_n=0) = \frac{(n-2-k)!}{n!}s_{k,n}$

where $s_{k,n}$ is the number of ways to guess $k$ draws from an $n$-deck correctly before failure.

TODO fix indexes for below

Conjecture: We have:

$$s_{k,n} = ns_{k-1,n-1} + a_{k,n}$$

where 

$$a_{k,n} = a_{k,n-1} + \binom{\lfloor \frac{n+1}{2} \rfloor +k-1}{k}$$

and $a_{k,0} = 0$ for all $k$.

$\mathbb{P}(X_n=0) = \frac{1}{n(n-1)}\lfloor \frac{(n-1)^2}{4} \rfloor$

$\mathbb{P}(X_n=1) = ?$

<!-- $\mathbb{E}(X_2)=10$ found numerically and you should probably double check this -->

$n! - \sum_{k \leq n-2}s_{k,n}$ is [OEIS A144188](https://oeis.org/search?q=5%2C+16%2C+62%2C+286&language=english&go=Search)

$\mathbb{E}(X_n) = \sum_{k \geq 0}k \mathbb{P}(X_n=k) = \sum_{k \geq 0} k \frac{(n-2-k)!}{n!} s_{k,n}$

$\lim_{n \to \infty} \mathbb{E}(X_n) =?$
