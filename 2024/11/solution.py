#!/usr/bin/env python3

import math

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
    
    for _ in range(25):
        newstones = []
        for stone in stones:
            newstones.extend(update(stone))
        stones = newstones
    
    print(len(stones))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
