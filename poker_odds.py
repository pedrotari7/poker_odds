from itertools import combinations, product
from collections import Counter
from math import factorial

values = ['8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']

def binom(x, y):
    return factorial(x)/float(factorial(y)*factorial(x-y))

## Census Method

def is_straight(v):
    return len(v) == len(set(v)) and (all(_ in values[:5] for _ in v) or all(_ in values[1:6] for _ in v) or all(_ in values[2:7] for _ in v))

cards = product(values*2, suits)

total = 0.0

nothing, pair, twopair, threek, full_house, fourk, fivek, straight, flush, straight_flush = 0,0,0,0,0,0,0,0,0,0

for hand in combinations(cards, 5):
    total += 1
    v, s = zip(*hand)
    v_count, s_count = Counter(v), Counter(s)
    if 5 in s_count.values():
        if is_straight(v):
            straight_flush += 1
        else:
            flush += 1
    elif is_straight(v):
        straight += 1
    elif 5 in v_count.values():
        fivek += 1
    elif 4 in v_count.values():
        fourk += 1
    elif 3 in v_count.values():
        if 2 in v_count.values():
            full_house += 1
        else:
            threek += 1
    elif 2 in v_count.values():
        if Counter(v_count.values())[2] == 2:
            twopair += 1
        else:
            pair += 1
    else:
        nothing += 1


## Combinatorial Method

## Straight Flush
_straight_flush = binom(3,1)*binom(4,1)*binom(2,1)**5
print 'straight flush: ', straight_flush, _straight_flush, straight_flush/total, _straight_flush/binom(56,5), straight_flush==_straight_flush

## Flush
_flush = binom(4,1)*binom(14,5) - _straight_flush
print 'flush: ', flush, _flush, flush/total, _flush/binom(56,5), flush==_flush

## Straight
_straight = binom(3,1)*binom(8,1)**5 - _straight_flush
print 'straight: ', straight, _straight, straight/total, _straight/binom(56,5), straight==_straight

## Five of a kind
_fivek = binom(7,1)*binom(8,5)
print 'five of a kind: ', fivek, _fivek, fivek/total, _fivek/binom(56,5), fivek==_fivek

## Four of a kind
_fourk = binom(7,1)*binom(8,4)*binom(48,1)
print 'four of a kind: ', fourk, _fourk, fourk/total, _fourk/binom(56,5), fourk==_fourk

## Full House
_full_house = binom(7,1)*binom(8,3)*binom(6,1)*binom(8,2)
print 'full house: ', full_house, _full_house, full_house/total, _full_house/binom(56,5), full_house==_full_house

## Three of a kind
_threek = binom(7,1)*binom(8,3)*binom(48,2) - _full_house
print 'three of a kind: ', threek, _threek, threek/total, _threek/binom(56,5), threek==_threek

## Two Pair
_twopair = binom(7,1)*binom(8,2)*binom(6,1)*binom(8,2)*binom(40,1) - binom(4,1)*binom(7,1)*binom(2,2)*binom(6,1)*binom(2,2)*binom(10,1)
print 'two pair: ', twopair, _twopair, twopair/total, _twopair/binom(56,5), twopair==_twopair

## Pair
_pair = binom(7,1)*binom(8,2)*binom(6,1)*binom(8,1)*binom(5,1)*binom(8,1)*binom(4,1)*binom(8,1) - binom(7,1)*binom(2,2)*binom(10,3)
print 'pair: ', pair, _pair, pair/total, _pair/binom(56,5), pair==_pair

## Nothing
_nothing = binom(56,5) - _pair - _twopair - _threek - _full_house - _fourk - _fivek - _straight - _flush - _straight_flush
print 'nothing: ', nothing, _nothing, nothing/total, _nothing/binom(56,5), nothing==_nothing