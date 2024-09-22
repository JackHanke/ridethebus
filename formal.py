from math import perm
from random import shuffle

def proc(n, num_games, verbose=False):
    def play_round(verbose=verbose):
        game_over = False
        num_cards_drawn = 0
        
        game_deck = [i for i in range(n)]
        shuffle(game_deck)
        pile = []
        pile.append(game_deck.pop())

        def guess(pile_arr, n):
            top_card_val = pile_arr[-1]
            x_v = 0
            for card in pile_arr[:-1]:
                if card <= top_card_val: x_v += 1
            numerator = top_card_val - x_v
            prob = numerator/(n-len(pile_arr))
            if prob >= 0.5: return 'lower'
            if prob < 0.5: return 'higher'

        while not game_over:
            if len(game_deck) > 0:
                if verbose: print(f'game deck = {game_deck}')
                if verbose: print(f'pile = {pile}')
                optimal_guess = guess(pile, n)
                if verbose: print(f'optimal guess = {optimal_guess}')
                drawn_card = game_deck.pop()
                if verbose: print(f'drawn card = {drawn_card}')
                num_cards_drawn += 1
                pile.append(drawn_card)
                if ((pile[-2] <= pile[-1]) and optimal_guess=='lower') or \
                    ((pile[-2] > pile[-1]) and optimal_guess=='higher'):
                    if verbose: print(f'Game Over')
                    game_over = True
                    return num_cards_drawn
            else:
                game_deck = [i for i in range(n)]
                shuffle(game_deck)
                pile = []
                pile.append(game_deck.pop())

    mean_val = 0
    for game in range(num_games):
        val = play_round(verbose=verbose)
        mean_val += val/num_games
        if (game % (num_games//10)) == 1 and verbose: 
            print(f'Mean after {game} games in round 2 = {mean_val*num_games/game}')
    if verbose: print(f'Mean over {num_games} games in round 2 = {mean_val}')
    return mean_val

for n in range(3,4):
    val = proc(n=n, num_games=1000, verbose=False)
    print(f'Expectation for permutation of length {n} = {val}')



