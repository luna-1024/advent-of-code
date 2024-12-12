#!/usr/bin/env python3

from functools import cache
import math

@cache
def n_update(stone, steps):
    if steps == 0:
        return 1
    newstones = update(stone)
    total = 0
    for newstone in newstones:
        total += n_update(newstone, steps - 1)
    return total

def update(stone):
    if stone == 0:
        return [1]
    digits = int(math.floor(math.log10(stone))) + 1
    if digits % 2 == 0:
        dv = 10 ** (digits // 2)
        return [stone // dv, stone % dv]
    return [stone * 2024]

def solution(lines):
    stones = [int(n) for n in next(lines).split(' ')]
    
    total = sum(n_update(stone, 75) for stone in stones)
    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
