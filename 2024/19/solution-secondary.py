#!/usr/bin/env python3

from functools import cache

def solution(sections):
    towels, designs = sections
    towels = towels.split(', ')
    designs = designs.split('\n')

    @cache
    def is_possible(design):
        if design == '':
            return 1
        total = 0
        for t in towels:
            if design.startswith(t):
                total += is_possible(design.removeprefix(t))
        return total
    
    possible = sum(is_possible(design) for design in designs)
    print(possible)

if __name__ == '__main__':
    file_in = open('input.txt')
    sections = file_in.read().removesuffix('\n').split('\n\n')
    solution(sections)
