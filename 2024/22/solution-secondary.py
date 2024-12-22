#!/usr/bin/env python3

from collections import *
from itertools import *

MOD = 2**24
STEPS = 2000

def advance_secret(n):
    n ^= (n << 6) % MOD
    n ^= (n >> 5) % MOD
    n ^= (n << 11) % MOD
    return n

def build_firstmap(n):
    first = Counter()
    rec = deque([n % 10])
    for _ in range(STEPS):
        n = advance_secret(n)
        curprice = n % 10
        rec.append(curprice)
        if len(rec) == 5:
            diffs = rec[1]-rec[0], rec[2]-rec[1], rec[3]-rec[2], rec[4]-rec[3]
            if diffs not in first:
                first[diffs] = curprice
            rec.popleft()
    return first

def solution(lines):
    numbers = [int(line) for line in lines]
    firstmaps = [build_firstmap(number) for number in numbers]
    
    total = Counter()
    for fmap in firstmaps:
        total += fmap

    best_seq = max(total, key=total.get)
    print(total[best_seq])

if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
