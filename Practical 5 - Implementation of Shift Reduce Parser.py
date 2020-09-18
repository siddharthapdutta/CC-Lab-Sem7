# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:13:45 2020
Implementation of shift reduce parser
E -> E + E
E -> E * E
E -> ( E )
E -> id
@author: Siddhartha
"""


PRODS = {'E': ['E+E', 'E*E', '(E)', 'id']}  # Grammar Production Rules
STACK = ['$']  # Initial Stack Data Structure


# Reduce Method for Shift Reduce Parser
def reduce():
    string = ""
    flag = -1
    for i in range(len(STACK)-1, 0, -1):
        string = STACK[i] + string
        for symbol, prod in PRODS.items():
            if string in prod:
                flag = symbol
                break
        if flag != -1:
            break

    if flag != -1:
        for i in range(len(string)):
            STACK.pop()
        STACK.append(flag)
        return True, string
    else:
        return False, None


# Shift Method for Shift Reduce Parser
def shift(symbol):
    STACK.append(symbol)
    return True


# Formatting Printing of Intermediate Steps
def print_action(inp, action, symbol):
    print('{:<10}'.format(''.join(STACK)), end='')
    print('{:>10}'.format(inp), end='\t')
    print('{:<15}'.format('{} -> {}'.format(action, symbol)))


if __name__ == '__main__':
    inp = input('Enter input string: ')  # (id*id)*id
    inp += '$'

    print('\n{:<10}{:>10}\t{:<15}'.format('STACK', 'INPUT', 'ACTION'))

    # Shift Reduce Parsing
    for i in range(len(inp)):
        if inp[i] != '$':
            if shift(inp[i]):
                print_action(inp[i+1:], 'Shift', inp[i])
            red = True
            while red:  # Recursive Reduce
                red, string = reduce()
                if red:
                    print_action(inp[i+1:], 'Reduce', string)
