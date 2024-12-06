#!/usr/bin/env python3

from collections import *
from tqdm import tqdm

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
                start_position = (y, x)
            else:
                assert c == '.'
                
                
    def coverage(cgrid):
        position = start_position
        direc = 0
        positions = defaultdict(set)
        positions[position].add(direc)
        while True:
            dy, dx = DIRECTIONS[direc]
            check = position[0] + dy, position[1] + dx
            if not (check[0] in range(maxy) and check[1] in range(maxx)):
                return positions.keys()
            if check in cgrid:
                direc = (direc + 1) % len(DIRECTIONS)
                continue
            if direc in positions[check]:
                return None
            positions[check].add(direc)
            position = check

    loops_pos = 0
    for pos in tqdm(coverage(grid), unit='positions'):
        newgrid = grid | {pos}
        loops_pos += coverage(newgrid) is None

    print(loops_pos)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
