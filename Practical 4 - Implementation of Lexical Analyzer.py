# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:11:51 2020
Implementation of Lexical Analyzer
@author: Siddhartha
"""


def isOperator(ch):
    operators = ['+', '-', '*', '/', '>', '<', '=']
    if ch in operators:
        return True
    return False


def isKeyword(word):
    keywords = ['auto', 'break', 'case', 'char', 'const', 'continue',
                'default', 'do', 'double', 'else', 'enum', 'extern', 'float',
                'for', 'goto', 'if', 'int', 'long', 'register', 'return',
                'short', 'signed', 'sizeof', 'static', 'struct', 'switch',
                'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
    if word in keywords:
        return True
    return False


if __name__ == '__main__':
    program = open('program.c', 'r')

    for line in program:
        buffer = ''
        for ch in line:
            if isOperator(ch):
                print(f'{ch} is operator.')
            elif ch.isalnum():
                buffer += ch
            elif ch == ' ' or ch == '\n' or ch in ['(', ')']:
                if buffer != '':
                    if isKeyword(buffer):
                        print(f'{buffer} is keyword.')
                    else:
                        print(f'{buffer} is identifier.')
                    buffer = ''
