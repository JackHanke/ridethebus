# Math behind Ride the Bus 
A summary of the rules to *Ride the Bus* can be found [here](https://www.wikihow.com/Play-Ride-the-Bus). 

## Round 1
Round 1 consists of guessing the color of the suit of the next card. If there are $x$ red cards and $y$ black cards already drawn, we have a $\mathbb{P}(\text{Choose Red, Get Red})=\frac{26-x}{52-x-y}$.

A simple heuristic for optimal play is to pick the color you have seen less of throughout the round.

If we let $X_1$ be the number of cards drawn before a loss, including the losing draw, in round 1, where all players play optimally, we then have

$$\mathbb{E}(X_1) =\frac{26}{52}1 + \frac{26}{52}\frac{25}{51}2 + \frac{26}{52}\frac{26}{51}\frac{25}{50}3 + \frac{26}{52}\frac{26}{51}\frac{25}{50}\frac{24}{49}4 + \frac{26}{52}\frac{26}{51}\frac{25}{50}\frac{25}{49}\frac{24}{48}5 +\dots$$

$$\mathbb{P}(X_1=k, k\in[1,52], k \text{ odd}) = \frac{(52-k)!}{52!}\frac{(26!)^2}{(26-\frac{k-1}{2})!(25-\frac{k-1}{2})!}$$

$$\mathbb{P}(X_1=k, k\in[1,52], k \text{ even}) = \frac{(52-k)!}{52!}\frac{(26!)^2}{(26-\frac{k}{2}-1)!(26-\frac{k}{2}+1)!} + $$

Let 

$$p = \sum_{k=1}^{52} \mathbb{P}(X_1=k)=0.9999999999999977\dots$$
$$e = \sum_{k=1}^{52} k\mathbb{P}(X_1=k)=2.0133486570488612\dots$$

The code for calculating the values for $e$ and $p$ can be found in `ridethebus.py`.

After $52$ cards are drawn, the deck is reshuffled and play continues with a full deck, so we write draw $k$ as $k=52n+r, (n,r)\in\mathbb{N}$, then
$$\mathbb{P}(X_1=k) = (1-p)^n\mathbb{P}(X_{i}=r)$$

$$\mathbb{E}(X_1) = \sum_{k=1}^{52} k\mathbb{P}(X_1=k) + \sum_{k=53}^{104} k\mathbb{P}(X_1=k) + \dots$$

$$\mathbb{E}(X_1) = e + (1-p)(52 + e) + (1-p)^2 (52*2 + e) \dots = e + \sum_{m \geq 1}(1-p)^m (52m+e)$$
$$\mathbb{E}(X_1) = \frac{e}{p} + 52\sum_{m \geq 1}m (1-p)^m  = \frac{52(1-p)+ep}{p^2} = 2.013348657048987 \dots$$


## Round 2
Round 2 consists of first drawing a card, and then each player guesses whether the next card drawn is higher or lower than the previous card. The value encodings of the cards are tradtional ace-high, meaning we can think of the cards as the integers $2$ through $14$.

If we let $v$ be the numerical value of the top card, and let $x(v)$ be the number of cards less than or equal to $v$ in the pile and let $y(v)$ be the number of cards above $v$ in the pile, then the probability that the next card drawn is less than or equal to $v$ is $\frac{(4v-5-x(v))}{(52-x(v)-y(v)-1)}$.

Simulations found in the `ridethebus.py` file give $E(X_2) \approx 3.728$ over 5,000,000 games.

## Round 3
Round 3 consists of first drawing two cards, and then each player guesses whether the next card drawn is between the last two cards or outside.
Let $n \leq m$ be the value of two cards. Also let $x(n,m)$ be the number of cards in the pile in $[n,m]$ including the cards of value $n$ and $m$ and similarly $y(n,m)$ not in $[n,m]$. Then the probability that the next card drawn is in $[n,m]$ is $\frac{4(m-n+1)-x(n,m)}{52-x(n,m)-y(n,m)}$.



Simulations found in the `ridethebus.py` file give $E(X_4) \approx 1.953$ over 5,000,000 games.

## Round 4
Round 4 consists of players guessing the suit of the next card drawn. Let $a,b,c,d$ be the number of diamonds, hearts, spades, and clubs drawn already, picking diamonds results in a prob of success of $\frac{13-a}{52-a-b-c-d}$.

A simple heuristic for optimal play is to choose the suit you have seen drawn the least.

If we let $X_4$ be the number of cards drawn before a loss, including the losing draw, in round 4, where all players play optimally, we then have

$$\mathbb{E}(X_4) =\frac{52-13}{52}1 + \frac{13}{52}\frac{51-13}{51}2 + \frac{13}{52}\frac{13}{51}\frac{50-13}{50}3 + \frac{13}{52}\frac{13}{51}\frac{13}{50}\frac{49-13}{49}4 + \dots$$

Let 

$$p = \sum_{k=1}^{52} \mathbb{P}(X_4=k)\approx 1$$
$$e = \sum_{k=1}^{52} k\mathbb{P}(X_4=k)=1.3621612249862824$$

As $p$ is very close to $1$, $e$ is an excellent approximation for $\mathbb{E}(X_4)$.
