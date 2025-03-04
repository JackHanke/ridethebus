import itertools
from random import shuffle
from copy import deepcopy
from math import factorial, floor
from scipy.special import binom

def test_perm(perm):
    # optimal guess for given seen pile of a total pile length n
    def guess(pile_arr, n):
        top_card_val = pile_arr[-1]
        x_v = 0
        for card in pile_arr[:-1]:
            if card < top_card_val: x_v += 1
        numerator = top_card_val - x_v - 1 
        prob = numerator/(n-len(pile_arr))
        if prob >= 0.5: return 'lower'
        if prob < 0.5: return 'higher'

    k = 0
    stop = False
    while not stop and (k <= len(perm)-2):
        guessed_action = guess(perm[:k+1], len(perm))
        if (guessed_action == 'lower' and perm[k] < perm[k+1]) or \
            (guessed_action == 'higher' and perm[k] > perm[k+1]):
            stop = True
        if not stop: k += 1

    return k

# returns row n of s_{n,k}(n-2-k)! values for 0<=k<=n, adjusts for 
def counts_perm_lst(n):
    counts_list = [0 for _ in range(n)] # number of failures 
    for perm in itertools.permutations([i for i in range(1,n+1)]):
        index = test_perm(perm)
        counts_list[index] += 1
    return counts_list

# returns row n of s_{n,k} values for 0<=k<=n, adjusts for 
def counts_distinct_perm_lst(n):
    counts_lst = counts_perm_lst(n)
    distincts = []
    for k, val in enumerate(counts_lst):
        if n-2-k >0: distinct_val = int(val/factorial(n-2-k))
        else: distinct_val = val
        distincts.append(distinct_val)
    return distincts

# returns array of permutations of length n that fail at index k (after k draws)
def k_index_perms_lst(n, k):
    k_index_perm_lst = []
    for perm in itertools.permutations([i for i in range(1,n+1)]):
        index = test_perm(perm)
        if index == k: k_index_perm_lst.append(perm)
    return k_index_perm_lst

# returns array of distinct subpermutations of permutations of length n that fail at index k (after k draws)
def k_index_subperms_lst(n, k):
    k_index_subperms_lst = []
    fail_at_list = [0 for _ in range(n)] # number of failures 
    for perm in itertools.permutations([i for i in range(1,n+1)]):
        index = test_perm(perm)
        if index == k: 
            sub_perm = perm[:(k+2)]
            if sub_perm not in k_index_subperms_lst: k_index_subperms_lst.append(sub_perm)
    return k_index_subperms_lst

def true_s(n,k): return len(k_index_subperms_lst(n,k))

# returns counts of sub permutations that have the same first_kay elements. for example, [4,3,1,2] and [4,3,2,1]
# if first_kay == k+2, then all values are 1
def group_by(n, k, first_kay):
    sub_perms = k_index_subperms_lst(n,k)
    freq = {}
    for sub_perm in sub_perms:
        first_kay_of_perm = tuple(sub_perm[:first_kay])
        try:
            freq[first_kay_of_perm] += 1
        except KeyError:
            freq[first_kay_of_perm] = 1
    return freq

if __name__ == '__main__':
    # for n in range(2, 7):
    #     arr = counts_distinct_perm_lst(n)
    #     print(f'row {n} = {arr}')
    n,k = 7,2
    dict_ = group_by(n,k,first_kay=3)
    for key, val in dict_.items():
        print(key, val)

# for n_ in range(3, 50):
#     n = 20*n_
#     # print(f'P(X_{n} = 1) = {s(1,n)/ (n*(n-1)*(n-2))}')
#     print(f'b({n}) = {b(n)/ (n*(n-1)*(n-2))}')

# for n in range(10): print(f'b({n}) = {b(n)}')

# oeis_lst = [1,1,2,5,16,62,286,1519,9184,62000,463964,3800684,
#  33911424,326678010,3385261194,37492199549,
#  442541571936,5539379635136,73368335117584,
#  1024178393797764,15041551052243448,
#  231665680071392900,3736363255881557460,
#  62935656581952683960]



    def a_seq(n,k):
        if n == 0: return 0
        return a_seq(n-1,k) + int(binom(((n+1)//2)+k-1,k))
        
    def a_arr():
        for k in range(5):
            row_str = ''
            for n in range(7):
                row_str += str(a_seq(n,k)) + ' '
            row_str
            print(row_str)

    def b(n):
        if n <= 0: return 0
        return b(n-1) + int(binom(((n+1)//2)+1, 2))

    def s_conj(k,n, test=False):
        if k-2 >= n: return 'Undefined' # TODO should be a raise probably
        elif k == 0: return ((n-1)**2)//4
        elif k == 1: return (n * (((n-2)**2)//4)) - b(n-4) # TODO just a conjecture

        if test:
            for k in range(2):
                for n in range(2, 10):
                    val = s(k,n)
                    print(f's({k},{n}) = {val}')
