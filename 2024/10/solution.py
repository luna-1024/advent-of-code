#!/usr/bin/env python3

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(lines):
    grid = [[int(c) for c in line] for line in lines]
    maxy, maxx = len(grid), len(grid[0])

    
    def tops(y, x):
        h = grid[y][x]
        if h == 9:
            return set([(y, x)])
        
        subtops = set()
        for dy, dx in DIRECTIONS:
            ny, nx = y + dy, x + dx
            if ny in range(maxy) and nx in range(maxx) and grid[ny][nx] == h + 1:
                subtops |= tops(ny, nx)
        return subtops
        
    
    total = 0
    for y, line in enumerate(grid):
        for x, d in enumerate(line):
            if d == 0:
                total += len(tops(y, x))
    
    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
