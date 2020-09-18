# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:40:26 2020
Acceptance of String by DFA

DFA1
Accepts a string starting and ending with 'a'

DFA2
L = {a^n b^m | n mod 2 = 0, m >= 1}
L = (aa)*b+

@author: Siddhartha
"""
#%%
def dfa1(string):
    if string[0] == 'a' and string[-1] == 'a':
        return True
    return False


# Transition Function for q0
def q0(inp):
    if inp == 'a':
        dfa = 1
    elif inp == 'b':
        dfa = 3
    else:
        dfa = -1
    return dfa

# Transition Function for q1
def q1(inp):
    if inp == 'a':
        dfa = 2
    elif inp == 'b':
        dfa = 4
    else:
        dfa = -1
    return dfa

# Transition Function for q2
def q2(inp):
    if inp == 'a':
        dfa = 1
    elif inp == 'b':
        dfa = 3
    else:
        dfa = -1
    return dfa

# Transition Function for q3
def q3(inp):
    if inp == 'a':
        dfa = 4
    elif inp == 'b':
        dfa = 3
    else:
        dfa = -1
    return dfa

def dfa2(string):
    dfa = 0
    for ch in string:
        if dfa == 0:    # Starting State
            dfa = q0(ch)
        elif dfa == 1:
            dfa = q1(ch)
        elif dfa == 2:
            dfa = q2(ch)
        elif dfa == 3:
            dfa = q3(ch)
        elif dfa == 4:  # Reached Trap State
            return False
        else:
            return False
    if dfa == 3:        # String Reached Final State
        return True
    return False


if __name__ == '__main__':
    string1 = input("Enter input string for DFA1: ")
    if (dfa1(string1)):
        print('Accepted!')
    else:
        print('Not Accepted!')
    
    string2 = input("Enter input string for DFA2: ")
    if (dfa2(string2)):
        print('Accepted!')
    else:
        print('Not Accepted!')
