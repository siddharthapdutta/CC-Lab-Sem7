# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:08:27 2020
Implementation of top-down parser
Recursive-descent parser
@author: Siddhartha
"""


def match(target):
    global i, inp
    if (inp[i] == target):
        i += 1
        return True
    else:
        raise Exception


def F():
    global i, inp
    if inp[i] == '(':
        match('(')
        E()
        match(')')
    elif inp[i].isalpha():
        match(inp[i])


def T_():
    global i, inp
    if inp[i] == '*':
        match('*')
        F()
        T_()
    else:
        return


def T():
    global i, inp
    F()
    T_()


def E_():
    global i, inp
    if inp[i] == '+':
        match('+')
        T()
        E_()
    else:
        return


def E():
    global i, inp
    try:
        T()
        E_()
    except Exception:
        return


if __name__ == '__main__':
    print('Recursive Descent Parser')
    print('E  -> TE\'')
    print('E\' -> +TE\' | ε')
    print('T  -> FT\'')
    print('T\' -> *FT\' | ε')
    print('F  -> (E)  | id')
    inp = input('Enter input string: ')  # 'a+(b*c)'
    inp += '$'
    i = 0
    E()
    if inp[i] == '$':
        print('Accepted!')
    else:
        print('Not Accepted!')
