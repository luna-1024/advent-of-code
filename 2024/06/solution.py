#!/usr/bin/env python3

from collections import *

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(lines):
    
    position = None
    
    lines = list(lines)
    maxy, maxx = len(lines), len(lines[0])
    
    grid = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                grid.add((y, x))
            elif c == '^':
                assert position is None
                position = (y, x)
            else:
                assert c == '.'
                
    direc = 0
    positions = defaultdict(set)
    positions[position].add(direc)
    while True:
        dy, dx = DIRECTIONS[direc]
        check = position[0] + dy, position[1] + dx
        if not (check[0] in range(maxy) and check[1] in range(maxx)):
            break
        if check in grid:
            direc = (direc + 1) % len(DIRECTIONS)
            continue
        if direc in positions[check]:
            break
        positions[check].add(direc)
        position = check

    print(len(positions))


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
