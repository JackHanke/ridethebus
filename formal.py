from random import shuffle
import itertools
from copy import deepcopy

def test_perm(perm):

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
        # print(perm)
        # print(perm[:k+1])
        # print(guessed_action)
        # print(k)
        # print(perm[k])
        # print(perm[k+1])
        if (guessed_action == 'lower' and perm[k] < perm[k+1]) or \
            (guessed_action == 'higher' and perm[k] > perm[k+1]):
            # print((guessed_action == 'lower' and perm[k] < perm[k+1]))
            # print((guessed_action == 'higher' and perm[k] > perm[k+1]))
            # print('stopped!')
            stop = True
        if not stop: k += 1
        # input()
    # print(k)

    return k

def test()
    for n in range(3, 7):
        fail_at_list = [0 for k in range(n)] # number of failures 
        for perm in itertools.permutations([i for i in range(1,n+1)]):
            index = test_perm(perm)
            fail_at_list[index] += 1
        
        for index, val in enumerate(fail_at_list):
            print(f'Perms of length {n} fail at position {index} = {val}')

