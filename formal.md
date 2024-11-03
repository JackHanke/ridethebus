# Formalism and Simplification of Round 2 Procedure

## Problem

Consider a permutation $\pi$ of $n$ elements. An observer is given the first element of the permutation $\pi_1$, and is tasked with predicting if $\pi_2$ is greater than $\pi_1$. If the prediction is correct, he is then tasked with predicting if $\pi_3$ is greater than $\pi_2$. This process continues with each successful prediction. If $\pi_n$ is correctly predicted, the observer repeats the task with a new permutation $\pi'$. If $\pi'_n$ is correctly predicted, the boserver repeats the task with a new permutation. This repeats until an incorrect prediction.   

The obserever has the knowledge that he is sampling from a permutation on $n$ elements, but does not know which permutation. He also has access to all sampled elements. What is the expected number of predictions the observer will get correct before an incorrect prediction, for a given $n$? 

## Solution

Let $X_n$ be the random variable representing the number of correct predictions before an incorrect prediction.

The process can also be thought of as making random hops from the ordered list $1$ to $n$, where one marks spots

$\mathbb{E}(X_2)=10$ 

$\mathbb{P}(X_n=1) = \frac{1}{n(n-1)}\lfloor \frac{(n-1)^2}{4} \rfloor$

$\mathbb{P}(X_n=2) = ?$

$\mathbb{P}(X_n=n)$ is [OEIS A144188](https://oeis.org/search?q=5%2C+16%2C+62%2C+286&language=english&go=Search)



