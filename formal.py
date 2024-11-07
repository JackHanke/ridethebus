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

def test(verbose = False):
    special_index = 4 # this is X_n = special_index
    for n in range(special_index+2, 10):
    # for n in range(6, 7):
        special_index_perm_lst = []
        fail_at_list = [0 for k in range(n)] # number of failures 
        for perm in itertools.permutations([i for i in range(1,n+1)]):
            index = test_perm(perm)
            if index == special_index: special_index_perm_lst.append(perm)
            fail_at_list[index] += 1
        
        for index, val in enumerate(fail_at_list):
            if index == special_index: 
                print(f'Num perms of length {n} fail at position {index} = {val} (Prob = {val/factorial(n-special_index-2)})')

        # this for loop is for counting the unique permutations of the first special_index+2 cards
        # these make up the terms that together form the value of s_{special_index, n}
        sub_perms = []
        for perm in special_index_perm_lst:
            if perm[:(special_index+2)] not in sub_perms: sub_perms.append(perm[:(special_index+2)])
            # if verbose: print(perm)
        
        for i, sub_perm in enumerate(sub_perms):
            if verbose: print(f'{i+1} is {sub_perm}')
        
# test(verbose=False)

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

def s(k,n, test=False):
    if k-2 >= n: return 'Undefined' # TODO should be a raise probably
    elif k == 0: return ((n-1)**2)//4
    elif k == 1: return (n * (((n-2)**2)//4)) - b(n-4)

    if test:
        for k in range(2):
            for n in range(2, 10):
                val = s(k,n)
                print(f's({k},{n}) = {val}')


for n_ in range(3, 50):
    n = 20*n_
    # print(f'P(X_{n} = 1) = {s(1,n)/ (n*(n-1)*(n-2))}')
    print(f'b({n}) = {b(n)/ (n*(n-1)*(n-2))}')

# for n in range(10): print(f'b({n}) = {b(n)}')

# oeis_lst = [1,1,2,5,16,62,286,1519,9184,62000,463964,3800684,
#  33911424,326678010,3385261194,37492199549,
#  442541571936,5539379635136,73368335117584,
#  1024178393797764,15041551052243448,
#  231665680071392900,3736363255881557460,
#  62935656581952683960]
