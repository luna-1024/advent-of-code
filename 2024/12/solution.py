#!/usr/bin/env python3

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(lines):
    grid = list(lines)
    maxy, maxx = len(grid), len(grid[0])
    
    def fullregion(y, x):
        ty = grid[y][x]
        points = set()
        scan = set([(y, x)])
        while len(scan) > 0:
            nextscan = set()
            for y, x in scan:
                points.add((y, x))
                for dy, dx in DIRECTIONS:
                    ny, nx = y + dy, x + dx
                    if ny in range(maxy) and nx in range(maxx) and grid[ny][nx] == ty:
                        pt = ny, nx
                        if pt not in points:
                            nextscan.add(pt)
            scan = nextscan
        return points
    
    mapped = set()
    
    def cost_and_mark(y, x):
        nonlocal mapped
        assert (y, x) not in mapped
        points = fullregion(y, x)
        area = len(points)
        perim = 0
        for y, x in points:
            for dy, dx in DIRECTIONS:
                ck = y + dy, x + dx
                if ck not in points:
                    perim += 1
        mapped |= points
        return area * perim
    
    total = 0
    for y in range(maxy):
        for x in range(maxx):
            if (y, x) not in mapped:
                total += cost_and_mark(y, x)
    print(total)


if __name__ == '__main__':
    file_in = open('input.txt')
    lines = (line.strip() for line in file_in.readlines())
    solution(lines)
