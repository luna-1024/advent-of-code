#!/usr/bin/env python3

from itertools import *

def solution(rules, updates):
    rules = set(tuple(int(p) for p in rule.split('|')) for rule in rules.split('\n'))
    updates = [[int(p) for p in rule.split(',')] for rule in updates.split('\n')]
    
    update_total = 0
    for update in updates:
        valid = True
        for first, second in combinations(update, 2):
            if (second, first) in rules:
                valid = False
                break
        if valid:
            assert len(update) % 2 == 1
            update_total += update[len(update) // 2]
    
    print(update_total)


if __name__ == '__main__':
    file_in = open('input.txt')
    sec1, sec2 = file_in.read().strip().split('\n\n')
    solution(sec1, sec2)
