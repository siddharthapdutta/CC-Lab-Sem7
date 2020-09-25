# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:17:00 2020
Implementation of intermediate code
generation phase of compiler
@author: Siddhartha
"""


def generate_ic(instructions):
    output = []
    for op, arg1, arg2, res in instructions:
        output.append('MOV R0, ' + arg1 + '\n')
        if op == '+':
            output.append('ADD R0, ' + arg2 + '\n')
        elif op == '-':
            output.append('SUB R0, ' + arg2 + '\n')
        elif op == '*':
            output.append('MUL R0, ' + arg2 + '\n')
        elif op == '/':
            output.append('DIV R0, ' + arg2 + '\n')
        elif op == '=':
            pass
        output.append('MOV ' + res + ', R0' + '\n')
    return output


if __name__ == '__main__':
    in_file = open('input.txt', 'r')
    instrs = [line.strip().split(' ') for line in in_file.readlines()]

    out = generate_ic(instrs)
    out_file = open('ic_output.txt', 'w')
    out_file.writelines(out)

    in_file.close()
    out_file.close()
