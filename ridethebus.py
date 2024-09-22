from math import perm
from random import shuffle

# round 1 can be evaluated symbolically
def round_1():
    def round_1_prob_of_loss_at_k(k):
        denom = 52
        prob = 1
        for round_num in range(k-1):
            prob *= ((denom+1)//2)/denom
            denom -= 1
        prob *= (denom//2)/denom
        return prob

    def round_1_p():
        tot = 0
        for round_num in range(1,52+1):
            tot += round_1_prob_of_loss_at_k(round_num)
        return tot

    def round_1_e():
        tot = 0
        for round_num in range(1,52+1):
            tot += round_num*round_1_prob_of_loss_at_k(round_num)
        return tot

    p = round_1_p()
    print(f'p = {p}')
    e = round_1_e()
    print(f'e = {e}')
    expectation = ((e*p)+52*(1-p))/(p**2)
    print(f'Expectation Round 1 for Draw of first loss = {expectation}')
    return expectation

# round 4 can be evaluated symbolically
def round_4():
    def round_4_prob_of_loss_at_k(k):
        denom = 52
        prob = 1
        for round_num in range(k-1):
            prob *= ((denom+4)//4)/denom
            denom -= 1
        prob *= (1-((denom+4)//4)/denom)
        return prob

    round_4_prob_of_loss_at_k(7)

    def round_4_p():
        tot = 0
        for round_num in range(1,52+1):
            tot += round_4_prob_of_loss_at_k(round_num)
        return tot

    def round_4_e():
        tot = 0
        for round_num in range(1,52+1):
            tot += round_num*round_4_prob_of_loss_at_k(round_num)
        return tot

    p = round_4_p()
    print(f'p = {p}')
    e = round_4_e()
    print(f'e = {e}')
    expectation = ((e*p)+52*(1-p))/(p**2)
    print(f'Expectation Round 4 for Draw of first loss = {expectation}')
    return expectation

# round 2 requires simulation
def round_2(num_games, verbose=False):
    def play_round_2(verbose=verbose):
        game_over = False
        num_cards_drawn = 0
        
        deck = [i+1 for i in range(1,13+1)]
        game_deck = deck + deck + deck + deck
        shuffle(game_deck)
        pile = []
        pile.append(game_deck.pop())

        def guess(pile_arr):
            top_card_val = pile_arr[-1]
            x_v = 0
            for card in pile_arr[:-1]:
                if card <= top_card_val: x_v +=1
            numerator = 4*top_card_val - 5 - x_v
            prob = numerator/(52-len(pile_arr))
            if prob >= 0.5: return 'lower'
            if prob < 0.5: return 'higher'

        while not game_over:
            if len(game_deck) > 0:
                if verbose: print(f'game deck = {game_deck}')
                if verbose: print(f'pile = {pile}')
                optimal_guess = guess(pile)
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
                gamedeck = deck + deck + deck + deck
                shuffle(game_deck)
                pile = []
                pile.append(game_deck.pop())

    mean_val = 0
    for game in range(num_games):
        val = play_round_2(verbose=verbose)
        mean_val += val/num_games
        if (game % (num_games//10)) == 1: 
            print(f'Mean after {game} games in round 2 = {mean_val*num_games/game}')
    print(f'Mean over {num_games} games in round 2 = {mean_val}')
    return mean_val

# round 4 requires simulation
def round_3(num_games, verbose=False):
    def play_round_3(verbose=verbose):
        game_over = False
        num_cards_drawn = 0
        
        deck = [i+1 for i in range(1,13+1)]
        game_deck = deck + deck + deck + deck
        shuffle(game_deck)
        pile = []
        pile.append(game_deck.pop())
        pile.append(game_deck.pop())

        def guess(pile_arr):
            low_card_val = min((pile_arr[-2], pile_arr[-1]))
            high_card_val = max((pile_arr[-2], pile_arr[-1]))
            x_nm = 0
            for card in pile_arr[:-1]:
                if card <= high_card_val and low_card_val <= card: x_nm +=1
            numerator = 4*(high_card_val-low_card_val+1) - x_nm
            prob = numerator/(52-len(pile_arr))
            if prob >= 0.5: return 'inside'
            if prob < 0.5: return 'outside'

        while not game_over:
            if len(game_deck) > 0:
                if verbose: print(f'game deck = {game_deck}')
                if verbose: print(f'pile = {pile}')
                optimal_guess = guess(pile)
                if verbose: print(f'optimal guess = {optimal_guess}')
                drawn_card = game_deck.pop()
                if verbose: print(f'drawn card = {drawn_card}')
                num_cards_drawn += 1
                pile.append(drawn_card)
                if ((pile[-2] <= pile[-1]) and optimal_guess=='inside') or \
                    ((pile[-2] > pile[-1]) and optimal_guess=='outside'):
                    if verbose: print(f'Game Over')
                    game_over = True
                    return num_cards_drawn
            else:
                game_deck = deck + deck + deck + deck
                shuffle(game_deck)
                pile = []
                pile.append(game_deck.pop())
                pile.append(game_deck.pop())

    mean_val = 0
    for game in range(num_games):
        val = play_round_3(verbose=verbose)
        mean_val += val/num_games
        if (game % (num_games//10)) == 1: 
            print(f'Mean after {game} games in round 3 = {mean_val*num_games/game}')
    print(f'Mean over {num_games} games in round 3 = {mean_val}')
    return mean_val

# round_1()
round_2(num_games=5000000, verbose=False)
# round_3(num_games=5000000, verbose=False)
# round_4()