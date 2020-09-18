# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:24:10 2020
Implementation of Infix to Postfix
@author: Siddhartha
"""

PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
STACK = []


def infixToPostfix(infix):
    postfix = ''
    for ch in infix:
        if ch.isalnum():
            postfix += ch               # Append Operands to Expression
        elif ch == '(':
            STACK.append(ch)            # Open ( Should be Pushed to Stack
        elif ch == ')':                 # Closing ) Condition
            while len(STACK) != 0 and STACK[-1] != '(':
                postfix += STACK.pop()
            STACK.pop()                 # Pop Corresponding Open (
        else:
            '''
            Operand with lower precedence cannot be on top of
            operand with higher precendence
            '''
            while len(STACK) != 0 and STACK[-1] != '(' \
                    and PRECEDENCE[ch] <= PRECEDENCE[STACK[-1]]:
                postfix += STACK.pop()
            STACK.append(ch)

    while len(STACK) != 0:              # Pop all Remaining from Stack
        postfix += STACK.pop()

    return postfix


if __name__ == '__main__':
    infix_expression = input("Enter infix expression: ")  #'x^y/(5*z)+2'
    postfix_expression = infixToPostfix(infix_expression)
    print('Infix Expression:', infix_expression)
    print('Postfix Expression:', postfix_expression)
