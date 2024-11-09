# Formalism and Simplification of Round 2 Procedure

## Problem

Consider a permutation $\pi$ of $n\geq2$ elements. An observer is given the first element of the permutation $\pi_1$, and is tasked with predicting if $\pi_2$ is greater than $\pi_1$. The observer has the knowledge that he is sampling from a permutation on $n$ elements, but does not know which permutation, as well as a memory of all sampled elements.

If the prediction of the relative value of $\pi_2$ is correct, they are then tasked with predicting if $\pi_3$ is greater than $\pi_2$. This process continues with each successful prediction. 

Let the random variable $X_n$ be the number of correct predictions before an incorrect prediction or the end of the permutation.
 
Compute $\mathbb{P}(X_n=k)$ and  $$\mathbb{E}(X_n)=\sum_{k \leq n-2}k\mathbb{}\mathbb{P}(X_n=k).$$

## Solution

Write $$\mathbb{P}(X_n=k) = \frac{(n-2-k)!}{n!}s_{n,k}$$

where $s_{n, k}$ is the number of ways to guess $k$ draws correctly from an $n$-deck before failing at the $(k+1)$-th draw. 


|$s_{n,k}$ |0|1|2|3|4|
|-|-|-|-|-|-|
|2|0| | | | | 
|3|1|0| | | |
|4|2|4|0| | |
|5|4|9|16|0| |
|6|6|22|42|74|0|
|7|9|37|119|223|393|
|8|12|64|226|720|1348|
|9|16|94|438|1525|4860|

We have $s_{n,0} = \lfloor \frac{(n-1)^2}{4} \rfloor$, and so $\mathbb{P}(X_n=0) = \frac{1}{n(n-1)}\lfloor \frac{(n-1)^2}{4} \rfloor$.

Conjecture: $s_{n,1} = ns_{n-1,0} - b_{n-4}$ where $b_n = b_{n-1} + \binom{\lfloor \frac{n+1}{2} \rfloor +1}{2}$ and $b_0 = 0$.

## Notes
$n! - \sum_{k \leq n-2}s_{n,k}(n-k)!$ is [OEIS A144188](https://oeis.org/search?q=5%2C+16%2C+62%2C+286&language=english&go=Search).

The process can also be thought of as making random hops from the ordered list $1$ to $n$, removoing spots that have been visited.
