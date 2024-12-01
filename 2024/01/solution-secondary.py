#!/usr/bin/env python3

from collections import *

def solution(lines):
    
    left, right = zip(*[map(int, line.split('   ')) for line in lines])
    rd = defaultdict(int, Counter(right))
    
    total = sum(rd[n]*n for n in left)
    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
