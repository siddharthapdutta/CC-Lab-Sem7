# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:11:13 2020
Write a program to find the
first and follow of a grammar
@author: Siddhartha
"""


PRODS = dict()
FIRST = dict()
FOLLOW = dict()


def first(ch):
    global first_ch
    rhs = PRODS[ch]
    for pro in rhs:
        if pro[0].islower():                    # If terminal
            first_ch += pro[0]
            return
        else:
            first(pro[0])                       # First of non-terminal


def follow(ch):
    global follow_ch
    for lhs, rhs in PRODS.items():
        for pro in rhs:
            if ch in pro:
                if pro[-1] == ch:               # Non-terminal is last in RHS
                    follow_ch += FOLLOW[lhs]    # Follow is equal to LHS follow
                    return
                else:                           # Non-terminal is not last
                    index = pro.find(ch)
                    if pro[index+1].islower():
                        follow_ch += pro[index+1]
                    else:                       # Follow is first of symbol
                        follow_ch += FIRST[pro[index+1]]
                        return


if __name__ == '__main__':
    # User Input for Grammar's Production Rules
    N = int(input("Enter the number of productions: "))
    print('Enter production rules for grammar')
    for _ in range(N):
        production = input().split(' = ')
        if production[0] in PRODS:
            PRODS[production[0]].append(production[1])
        else:
            PRODS[production[0]] = [production[1]]

    # Finding First
    for lhs in PRODS.keys():
        first_ch = ''
        first(lhs)
        FIRST[lhs] = first_ch

    # Finding Follow
    for lhs in PRODS.keys():
        follow_ch = ''
        follow(lhs)
        if len(follow_ch) == 0:
            FOLLOW[lhs] = '$'
        else:
            FOLLOW[lhs] = follow_ch

    # Printing First & Follow of Symbols in Grammar
    print('\n{:^8}{:^8}{:^8}'.format('Symbol', 'FIRST', 'FOLLOW'))
    for symbol in PRODS.keys():
        print('{:^8}'.format(symbol), end='')
        print('{:^8}'.format(FIRST[symbol]), end='')
        print('{:^8}'.format(FOLLOW[symbol]))
