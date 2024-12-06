#!/usr/bin/env python3

from functools import *

def solution(rules, updates):
    rules = set(tuple(int(p) for p in rule.split('|')) for rule in rules.split('\n'))
    updates = [[int(p) for p in rule.split(',')] for rule in updates.split('\n')]
    
    def sort_cmp(first, second):
        if first == second:
            return 0
        elif (first, second) in rules:
            return -1
        else: # Do not move if not invalidated by rules
            return 0
        
    rules_key = cmp_to_key(sort_cmp)
    
    update_total = 0
    for update in updates:
        fixed_update = sorted(update, key=rules_key)
        if fixed_update != update:
            assert len(fixed_update) % 2 == 1
            update_total += fixed_update[len(fixed_update) // 2]
    
    print(update_total)


if __name__ == '__main__':
    file_in = open('input.txt')
    sec1, sec2 = file_in.read().strip().split('\n\n')
    solution(sec1, sec2)
