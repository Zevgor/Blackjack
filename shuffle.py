import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
random.shuffle(mydeck)

def deal(numhands, n=5, deck=mydeck):
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

test = deal(4)

print (test)


def deal_sequentially(numhands, n=5, deck=mydeck):
    hands = []
    for i in range(numhands):
        hand = []
        for j in range(n):
            hand.append(deck[j*numhands + i])
        hands.append(hand)
    return hands

test2 = deal_sequentially(4)

print (test2)