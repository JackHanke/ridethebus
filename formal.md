# Formalism and Simplification of Round 2 Procedure

## Problem

Consider a permutation $\pi$ of $n$ elements. An observer is given the first element of the permutation $\pi_1$, and is tasked with predicting if $\pi_2$ is greater than $\pi_1$. If the prediction is correct, he is then tasked with predicting if $\pi_3$ is greater than $\pi_2$. This process continues with each successful prediction. If $\pi_n$ is correctly predicted, the observer repeats the task with a new permutation $\pi'$. If $\pi'_n$ is correctly predicted, the boserver repeats the task with a new permutation. This repeats until an incorrect prediction.   

The obserever has the knowledge that he is sampling from a permutation on $n$ elements, but does not know which permutation. He also has access to all sampled elements. What is the expected number of predictions the observer will get correct before an incorrect prediction, for a given $n$? 

## Solution

Let $X_n$ be the random variable representing the number of correct predictions before an incorrect prediction.

Note that we have for $k=qn+r$ that $\mathbb{P}(X_n = k) = (1-p)^q \mathbb{P}(X_n = r),$
where $p = \mathbb{P}(X_n < n). $ 

$\mathbb{E}(X_2)=10$ 



