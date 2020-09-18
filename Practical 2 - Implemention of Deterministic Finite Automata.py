# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:25:01 2020
Implemention of Deterministic Finite Automata
@author: Siddhartha
"""
#%%
def dfa(Q, S, q, transitions, F):
    def string(string):
        dfa_state = q
        for ch in string:
            print(ch, end=': q')
            print(dfa_state, end=' -> q')
            try:
                dfa_state = transitions[dfa_state][ch]
            except:             # Undefined Transitions
                return False
            print(dfa_state)

        if dfa_state in F:
            return True
        else:
            return False
    return string

if __name__ == '__main__':
    N = int(input("Enter number of states: "))
    Q = ['q'+str(i) for i in range(N)]
    print("States are:", *Q)
    
    q = int(input("Enter initial state: "))
    F = list(map(int, input("Enter final state(s): ").strip().split(' ')))
    S = list(input("Enter set of symbols: ").strip().split(' '))
    
    print("Enter transition table:")
    print("State\t", end='')
    print(*S, sep=' ')
    
    transitions = []
    for state in Q:
        print(state, end='\t') 
        inp = list(map(int,input().strip().split(' ')))
        transitions.append({key: value for key, value in zip(S, inp)})
    
    string = input('Enter input string: ').strip()
    print('\n\nInput String: ', string)
    print('Transitions')
    automata = dfa(Q, S, q, transitions, F)
    if (automata(string)):
        print('\nAccepted!')
    else:
        print('\nNot Accepted!')    
